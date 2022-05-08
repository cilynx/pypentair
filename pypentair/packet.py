import serial

DEBUG = True

ERROR = 0xFF


class Style():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Fields():
    PREAMBLE_0 = 0
    PREAMBLE_1 = 1
    PREAMBLE_2 = 2
    HEADER = 3
    VERSION = 4
    DST = 5
    SRC = 6
    ACTION = 7
    DATA_LENGTH = 8
    DATA = 9


class RS485(serial.Serial):
    def __init__(self):
        super().__init__(port='/dev/ttyUSB0',
                         baudrate=9600,
                         parity=serial.PARITY_NONE,
                         stopbits=serial.STOPBITS_ONE,
                         bytesize=serial.EIGHTBITS,
                         timeout=1)

    def get_response(self):
        pbytes = []
        while True:
            for c in self.read():
                pbytes.append(c)
                if len(pbytes) > 4:
                    pbytes.pop(0)
                if pbytes == Packet.PREAMBLE + [Packet.HEADER]:
                    pbytes.extend(list(self.read(4)))  # Version, DST, SRC, Action
                    data_length = ord(self.read())
                    pbytes.append(data_length)
                    pbytes.extend(list(self.read(data_length)))  # Data
                    pbytes.extend(list(self.read(2)))            # Checksum
                    return Packet(pbytes)


rs485 = RS485()


class Packet():
    PREAMBLE = [0xFF, 0x00, 0xFF]
    HEADER = 0xA5
    VERSION = 0x00

    def __init__(self, *args, src=0x21, dst=None, action=None, data=None):
        if args != ():
            self.bytes = args
        else:
            self.dst = dst
            self.action = action
            self.src = src
            if isinstance(data, int):
                self.data = [data]
            else:
                self.data = data

    def send(self):
        rs485.write(bytearray(self.bytes))
        if DEBUG:
            print()
        if DEBUG:
            print(Style.OKGREEN + "Request: ", self.bytes, Style.ENDC)
        response = rs485.get_response()
        if DEBUG:
            print(Style.OKBLUE + "Response:", response.bytes, Style.ENDC)
        if response.action == self.action:
            return response
        elif response.action == ERROR:
            if DEBUG:
                print(Style.FAIL, "ERROR:", response.bytes[9], Style.ENDC)
            return response
        else:
            raise ValueError("This packet goes somewhere else =(")

    @property
    def bytes(self):
        return Packet.PREAMBLE + self.payload + self.checkbytes

    @bytes.setter
    def bytes(self, array):
        packet = array[0]
        if packet[0:5] != Packet.PREAMBLE + [Packet.HEADER] + [Packet.VERSION]:
            packet = Packet.PREAMBLE + [Packet.HEADER] + [Packet.VERSION] + packet

        payload_start = Fields.HEADER
        data_length = packet[Fields.DATA_LENGTH]
        data_end = payload_start + data_length + Fields.DATA - Fields.HEADER
        packet_length = len(packet)

        payload = packet[payload_start:data_end]

        if packet_length > data_length + Fields.DATA:
            read_checksum = 256 * packet[-2] + packet[-1]
            if read_checksum != sum(payload):
                raise ValueError("Provided checksum does not match calculated checksum")
                return False

        self.dst = packet[Fields.DST]
        self.src = packet[Fields.SRC]
        self.action = packet[Fields.ACTION]

        if data_end > Fields.DATA:
            self.data = packet[Fields.DATA:data_end]
        else:
            self.data = None

        return self.bytes

    @property
    def checksum(self):
        return sum(self.payload)

    @property
    def checkbytes(self):
        return list(self.checksum.to_bytes(2, byteorder='big'))

    @property
    def data_length(self):
        if self.data:
            return len(self.data)
        else:
            return 0

    @property
    def to_int(self):
        return(self.data[0] << 8 | self.data[1])

    @property
    def payload(self):
        if self.data_length:
            return [Packet.HEADER, Packet.VERSION, self.dst, self.src, self.action, self.data_length] + self.data
        else:
            return [Packet.HEADER, Packet.VERSION, self.dst, self.src, self.action, self.data_length]

#     def inspect(self):
#         print("   Destination:\t\t", pp(self.dst), lookup(ADDRESSES, self.dst))
#         print("   Source:\t\t", pp(self.src), lookup(ADDRESSES, self.src))
#         if self.dst == ADDRESSES['BROADCAST']:
#             print("   Action:\t\t", pp(self.action), lookup(BROADCAST_ACTIONS, self.action))
#         else:
#             print("   Action:\t\t", pp(self.action), lookup(ACTIONS, self.action))
#         print("   Data Length:\t\t", pp(self.data_length))
#         if self.data_length > 0:
#             print("   Data:\t\t", binascii.hexlify(bytearray(self.data)))
#
#         if self.action == ACTIONS['PUMP_STATUS'] and self.data_length > 0:
#             data = self.data
# #            print(data)
#             run = pp(data[PUMP_STATUS_FIELDS['RUN])
#             print("      Run:\t\t", run, "ON" if run == "0a" else "OFF" if run == "04" else "")
#             print("      Mode:\t\t", pp(data[PUMP_STATUS_FIELDS['MODE]))
#             print("      Drive State:\t", pp(data[PUMP_STATUS_FIELDS['DRIVE_STATE]))
#             watts_h = data[PUMP_STATUS_FIELDS['WATTS_H]
#             watts_l = data[PUMP_STATUS_FIELDS['WATTS_L]
#             print("      Watts_H:\t\t", pp(data[PUMP_STATUS_FIELDS['WATTS_H]))
#             print("      Watts_L:\t\t", pp(data[PUMP_STATUS_FIELDS['WATTS_L]))
#             print("         Watts:\t\t\t", watts_h*0x100+watts_l)
#             rpm_h = data[PUMP_STATUS_FIELDS['RPM_H]
#             rpm_l = data[PUMP_STATUS_FIELDS['RPM_L]
#             print("      RPM_H:\t\t", pp(data[PUMP_STATUS_FIELDS['RPM_H]))
#             print("      RPM_L:\t\t", pp(data[PUMP_STATUS_FIELDS['RPM_L]))
#             print("         RPM:\t\t\t", rpm_h*0x100+rpm_l)
#             print("      REMAINING_TIME_H:\t", data[PUMP_STATUS_FIELDS['REMAINING_TIME_H])
#             print("      REMAINING_TIME_M:\t", data[PUMP_STATUS_FIELDS['REMAINING_TIME_M])
#             print("      CLOCK_TIME_H:\t", data[PUMP_STATUS_FIELDS['CLOCK_TIME_H])
#             print("      CLOCK_TIME_M:\t", data[PUMP_STATUS_FIELDS['CLOCK_TIME_M])
