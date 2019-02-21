import unittest
import random
from nose.plugins.attrib import attr
from app.pentair import Packet, Pump

PAYLOAD_HEADER  = 0xA5
SRC             = 0x21
DST             = 0x60
GET_PUMP_STATUS = 0x07
REMOTE_CONTROL  = 0x04
ON              = 0xFF
PUMP_PROGRAM    = 0x01
SET             = 0x02
RPM             = 0xC4
VERSION         = 0x00

class TestPumpMethods(unittest.TestCase):

    @attr('messy')
    def test_power_on(self):
        Pump(1).power = True
        self.assertEqual(Pump(1).power, True)

    @attr('messy')
    def test_power_off(self):
        Pump(1).power = False
        self.assertEqual(Pump(1).power, False)

    @attr('messy')
    def test_set_rpm(self):
        for rpm in [3000, 2500, 2000, 1100]:
            with self.subTest(rpm=rpm):
                Pump(1).rpm = rpm
                self.assertEqual(Pump(1).rpm, rpm)
                # Ugly formula below is best-fit polynomial to manually collected data.
                # Across the usable rpm range, deviation stays <100 watts
                self.assertAlmostEqual(Pump(1).watts, 0.0004*(rpm**2)-0.8*rpm+611, delta=100)

    @attr('messy')
    def test_programs(self):
        for x in range(1,4):
            Pump(1).program = x
            self.assertEqual(Pump(1).program, x)

    def test_program_1(self):
        rpm = random.randint(2000,3000)
        Pump(1).program_1 = rpm
        self.assertEqual(Pump(1).program_1, rpm)
        Pump(1).program_1 = 1115 # Should be 750, if we can set minimum better
        self.assertEqual(Pump(1).program_1, 1115)

    def test_program_2(self):
        rpm = random.randint(2000,3000)
        Pump(1).program_2 = rpm
        self.assertEqual(Pump(1).program_2, rpm)
        Pump(1).program_2 = 1500
        self.assertEqual(Pump(1).program_2, 1500)

    def test_program_3(self):
        rpm = random.randint(2000,3000)
        Pump(1).program_3 = rpm
        self.assertEqual(Pump(1).program_3, rpm)
        Pump(1).program_3 = 2350
        self.assertEqual(Pump(1).program_3, 2350)

    def test_program_4(self):
        rpm = random.randint(2000,3000)
        Pump(1).program_4 = rpm
        self.assertEqual(Pump(1).program_4, rpm)
        Pump(1).program_4 = 3110
        self.assertEqual(Pump(1).program_4, 3110)

    def test_ramp(self):
        Pump(1).ramp = 100
        self.assertEqual(Pump(1).ramp, 100)
        Pump(1).ramp = 200
        self.assertEqual(Pump(1).ramp, 200)

    def test_celsius(self):
        Pump(1).celsius = 1
        self.assertEqual(Pump(1).fahrenheit, 0)
        self.assertEqual(Pump(1).celsius, 1)
        Pump(1).celsius = 0
        self.assertEqual(Pump(1).fahrenheit, 1)
        self.assertEqual(Pump(1).celsius, 0)

    def test_fahrenheit(self):
        Pump(1).fahrenheit = 1
        self.assertEqual(Pump(1).fahrenheit, 1)
        self.assertEqual(Pump(1).celsius, 0)
        Pump(1).fahrenheit = 0
        self.assertEqual(Pump(1).fahrenheit, 0)
        self.assertEqual(Pump(1).celsius, 1)

    def test_contrast(self):
        Pump(1).contrast = 1
        self.assertEqual(Pump(1).contrast, 1)
        Pump(1).contrast = 3
        self.assertEqual(Pump(1).contrast, 3)

    def test_address(self):
        Pump(1).address = 97
        self.assertEqual(Pump(2).address, 97)
        Pump(2).address = 96
        self.assertEqual(Pump(1).address, 96)

    def test_id(self):
        Pump(1).id = 2
        self.assertEqual(Pump(2).address, 97)
        self.assertEqual(Pump(2).id, 2)
        Pump(2).id = 1
        self.assertEqual(Pump(1).address, 96)
        self.assertEqual(Pump(1).id, 1)

    def test_ampm(self):
        Pump(1).ampm = False
        self.assertEqual(Pump(1).ampm, False)
        Pump(1).ampm = True
        self.assertEqual(Pump(1).ampm, True)

    def test_max_speed(self):
        Pump(1).max_speed = 3445
        self.assertEqual(Pump(1).max_speed, 3445)
        Pump(1).max_speed = 3450
        self.assertEqual(Pump(1).max_speed, 3450)

    def test_min_speed(self):
        Pump(1).min_speed = 1105
        self.assertEqual(Pump(1).min_speed, 1105)
        Pump(1).min_speed = 1100
        self.assertEqual(Pump(1).min_speed, 1100)

    def test_enable_password(self):
        Pump(1).password_enable = True
        self.assertEqual(Pump(1).password_enable, True)
        Pump(1).password_enable = False
        self.assertEqual(Pump(1).password_enable, False)

    def test_set_password_timeout(self):
        Pump(1).password_timeout = 360
        self.assertEqual(Pump(1).password_timeout, 360)
        Pump(1).password_timeout = 10
        self.assertEqual(Pump(1).password_timeout, 10)

    def test_set_password(self):
        Pump(1).password = 1235
        self.assertEqual(Pump(1).password, 1235)
        Pump(1).password = 1234
        self.assertEqual(Pump(1).password, 1234)

class TestSpeedMethods(unittest.TestCase):

    def test_mode(self):
        Pump(1).speed(1).mode = 0
        self.assertEqual(Pump(1).speed(1).mode, "MANUAL")
        Pump(1).speed(1).mode = "EGG_TIMER"
        self.assertEqual(Pump(1).speed(1).mode, "EGG_TIMER")
        Pump(1).speed(5).mode = "SCHEDULE"
        self.assertEqual(Pump(1).speed(5).mode, "SCHEDULE")
        Pump(1).speed(5).mode = 3
        self.assertEqual(Pump(1).speed(5).mode, "DISABLED")

    def test_rpm(self):
        Pump(1).speed(1).rpm = 2000
        self.assertEqual(Pump(1).speed(1).rpm, 2000)
        Pump(1).speed(1).rpm = 1100
        self.assertEqual(Pump(1).speed(1).rpm, 1100)

    def test_schedule_start(self):
        Pump(1).speed(1).schedule_start = [7, 1]
        self.assertEqual(Pump(1).speed(1).schedule_start, [7, 1])
        Pump(1).speed(1).schedule_start = [11, 0]
        self.assertEqual(Pump(1).speed(1).schedule_start, [11, 0])

    def test_schedule_end(self):
        Pump(1).speed(1).schedule_end = [7, 1]
        self.assertEqual(Pump(1).speed(1).schedule_end, [7, 1])
        Pump(1).speed(1).schedule_end = [18, 0]
        self.assertEqual(Pump(1).speed(1).schedule_end, [18, 0])

    def test_egg_timer(self):
        Pump(1).speed(1).egg_timer = [7, 1]
        self.assertEqual(Pump(1).speed(1).egg_timer, [7, 1])
        Pump(1).speed(1).egg_timer = [0, 10]
        self.assertEqual(Pump(1).speed(1).egg_timer, [0, 10])

class TestPacketMethods(unittest.TestCase):

### Data Length, because incoming data can have several formats

    def test_data_length_with_no_data(self):
        packet = Packet(dst=DST, action=GET_PUMP_STATUS)
        self.assertEqual(packet.data_length, 0)

    def test_data_length_with_single_data_byte(self):
        packet = Packet(dst=DST, action=REMOTE_CONTROL, data=ON)
        self.assertEqual(packet.data_length, 1)

    def test_data_length_with_single_data_byte_list(self):
        packet = Packet(dst=DST, action=REMOTE_CONTROL, data=[ON])
        self.assertEqual(packet.data_length, 1)

    def test_data_length_with_multiple_data_bytes(self):
        packet = Packet(dst=DST, action=PUMP_PROGRAM, data=[SET, RPM, 5, 220])
        self.assertEqual(packet.data_length, 4)

### Payload, as above, mostly checking various input format handling

    def test_payload_with_no_data(self):
        packet = Packet(dst=DST, action=GET_PUMP_STATUS)
        self.assertEqual(packet.payload, [PAYLOAD_HEADER, VERSION, DST, SRC, GET_PUMP_STATUS, 0])

    def test_payload_with_single_data_byte(self):
        packet = Packet(dst=DST, action=REMOTE_CONTROL, data=ON)
        self.assertEqual(packet.payload, [PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON])

    def test_payload_with_single_data_byte_list(self):
        packet = Packet(dst=DST, action=REMOTE_CONTROL, data=[ON])
        self.assertEqual(packet.payload, [PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON])

    def test_payload_with_multiple_data_bytes(self):
        packet = Packet(dst=DST, action=PUMP_PROGRAM, data=[SET, RPM, 5, 220])
        self.assertEqual(packet.payload, [PAYLOAD_HEADER, VERSION, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220])

### Checksums and Such

    def test_checkbytes(self):
        packet = Packet(dst=DST, action=PUMP_PROGRAM, data=[SET, RPM, 5, 220])
        self.assertEqual(packet.checkbytes, [2, 210])

    def test_checksum(self):
        packet = Packet(dst=DST, action=PUMP_PROGRAM, data=[SET, RPM, 5, 220])
        self.assertEqual(packet.checksum, 2*256 + 210)

### Key=Value Construction

    def test_kv_construction_no_data(self):
        packet = Packet(dst=DST, action=GET_PUMP_STATUS)
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, GET_PUMP_STATUS)
        self.assertEqual(packet.data_length, 0)
        self.assertEqual(packet.data, None)
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, GET_PUMP_STATUS, 0, 1, 45])

    def test_kv_construction_single_data_byte(self):
        packet = Packet(dst=DST, action=REMOTE_CONTROL, data=ON)
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, REMOTE_CONTROL)
        self.assertEqual(packet.data_length, 1)
        self.assertEqual(packet.data, [ON])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON, 2, 42])

    def test_kv_construction_single_data_byte_list(self):
        packet = Packet(dst=DST, action=REMOTE_CONTROL, data=[ON])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, REMOTE_CONTROL)
        self.assertEqual(packet.data_length, 1)
        self.assertEqual(packet.data, [ON])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON, 2, 42])

    def test_kv_construction_multiple_data_bytes(self):
        packet = Packet(dst=DST, action=PUMP_PROGRAM, data=[SET, RPM, 5, 220])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, PUMP_PROGRAM)
        self.assertEqual(packet.data_length, 4)
        self.assertEqual(packet.data, [SET, RPM, 5, 220])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220, 2, 210])

### Byte Construction, No Header, No Data

    def test_byte_construction_no_header_no_data_no_checksum(self):
        packet = Packet([DST, SRC, GET_PUMP_STATUS, 0])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, GET_PUMP_STATUS)
        self.assertEqual(packet.data_length, 0)
        self.assertEqual(packet.data, None)
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, GET_PUMP_STATUS, 0, 1, 45])

    def test_byte_construction_no_header_no_data_valid_checksum(self):
        packet = Packet([DST, SRC, GET_PUMP_STATUS, 0, 1, 45])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, GET_PUMP_STATUS)
        self.assertEqual(packet.data_length, 0)
        self.assertEqual(packet.data, None)
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, GET_PUMP_STATUS, 0, 1, 45])

    def test_byte_construction_no_header_no_data_invalid_checksum(self):
        with self.assertRaises(ValueError):
            Packet([DST, SRC, GET_PUMP_STATUS, 0, 1, 46])

### Byte Construction, With Header, No Data

    def test_byte_construction_with_header_no_data_no_checksum(self):
        packet = Packet([0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, GET_PUMP_STATUS, 0])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, GET_PUMP_STATUS)
        self.assertEqual(packet.data_length, 0)
        self.assertEqual(packet.data, None)
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, GET_PUMP_STATUS, 0, 1, 45])

    def test_byte_construction_with_header_no_data_valid_checksum(self):
        packet = Packet([0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, GET_PUMP_STATUS, 0, 1, 45])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, GET_PUMP_STATUS)
        self.assertEqual(packet.data_length, 0)
        self.assertEqual(packet.data, None)
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, GET_PUMP_STATUS, 0, 1, 45])

    def test_byte_construction_with_header_no_data_invalid_checksum(self):
        with self.assertRaises(ValueError):
            Packet([0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, GET_PUMP_STATUS, 0, 1, 46])

### Byte Construction, No Header, Single Data Byte

    def test_byte_construction_no_header_single_data_byte_no_checksum(self):
        packet = Packet([DST, SRC, REMOTE_CONTROL, 1, ON])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, REMOTE_CONTROL)
        self.assertEqual(packet.data_length, 1)
        self.assertEqual(packet.data, [ON])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON, 2, 42])

    def test_byte_construction_no_header_single_data_byte_valid_checksum(self):
        packet = Packet([DST, SRC, REMOTE_CONTROL, 1, ON, 2, 42])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, REMOTE_CONTROL)
        self.assertEqual(packet.data_length, 1)
        self.assertEqual(packet.data, [ON])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON, 2, 42])

    def test_byte_construction_no_header_single_data_byte_invalid_checksum(self):
        with self.assertRaises(ValueError):
            Packet([DST, SRC, REMOTE_CONTROL, 1, ON, 2, 43])

### Byte Construction, With Header, Single Data Byte

    def test_byte_construction_with_header_single_data_byte_no_checksum(self):
        packet = Packet([0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, REMOTE_CONTROL)
        self.assertEqual(packet.data_length, 1)
        self.assertEqual(packet.data, [ON])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON, 2, 42])

    def test_byte_construction_with_header_single_data_byte_valid_checksum(self):
        packet = Packet([0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON, 2, 42])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, REMOTE_CONTROL)
        self.assertEqual(packet.data_length, 1)
        self.assertEqual(packet.data, [ON])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON, 2, 42])

    def test_byte_construction_with_header_single_data_byte_invalid_checksum(self):
        with self.assertRaises(ValueError):
            Packet([0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, REMOTE_CONTROL, 1, ON, 2, 43])

### Byte Construction, No Header, Multiple Data Bytes

    def test_byte_construction_no_header_multiple_data_bytes_no_checksum(self):
        packet = Packet([DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, PUMP_PROGRAM)
        self.assertEqual(packet.data_length, 4)
        self.assertEqual(packet.data, [SET, RPM, 5, 220])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220, 2, 210])

    def test_byte_construction_no_header_multiple_data_bytes_valid_checksum(self):
        packet = Packet([DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220, 2, 210])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, PUMP_PROGRAM)
        self.assertEqual(packet.data_length, 4)
        self.assertEqual(packet.data, [SET, RPM, 5, 220])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220, 2, 210])

    def test_byte_construction_no_header_multiple_data_bytes_invalid_checksum(self):
        with self.assertRaises(ValueError):
            Packet([DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220, 2, 211])

### Byte Construction, With Header, Multiple Data Bytes

    def test_byte_construction_with_header_multiple_data_bytes_no_checksum(self):
        packet = Packet([0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, PUMP_PROGRAM)
        self.assertEqual(packet.data_length, 4)
        self.assertEqual(packet.data, [SET, RPM, 5, 220])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220, 2, 210])

    def test_byte_construction_with_header_multiple_data_bytes_valid_checksum(self):
        packet = Packet([0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220, 2, 210])
        self.assertEqual(packet.dst, DST)
        self.assertEqual(packet.src, SRC)
        self.assertEqual(packet.action, PUMP_PROGRAM)
        self.assertEqual(packet.data_length, 4)
        self.assertEqual(packet.data, [SET, RPM, 5, 220])
        self.assertEqual(packet.bytes, [0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220, 2, 210])

    def test_byte_construction_with_header_multiple_data_bytes_invalid_checksum(self):
        with self.assertRaises(ValueError):
            Packet([0xFF, 0x00, 0xFF, PAYLOAD_HEADER, VERSION, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220, 2, 211])
