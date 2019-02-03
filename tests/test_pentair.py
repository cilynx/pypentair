import unittest
from app.pentair import Packet

PAYLOAD_HEADER  = 0xA5
SRC             = 0x21
DST             = 0x60
GET_PUMP_STATUS = 0x07
REMOTE_CONTROL  = 0x04
ON              = 0xFF
PUMP_PROGRAM    = 0x01
SET             = 0x02
RPM             = 0xC4

class TestPacketMethods(unittest.TestCase):


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


    def test_payload_with_no_data(self):
        packet = Packet(dst=DST, action=GET_PUMP_STATUS)
        self.assertEqual(packet.payload, [PAYLOAD_HEADER, DST, SRC, GET_PUMP_STATUS, 0])

    def test_payload_with_single_data_byte(self):
        packet = Packet(dst=DST, action=REMOTE_CONTROL, data=ON)
        self.assertEqual(packet.payload, [PAYLOAD_HEADER, DST, SRC, REMOTE_CONTROL, 1, ON])

    def test_payload_with_single_data_byte_list(self):
        packet = Packet(dst=DST, action=REMOTE_CONTROL, data=[ON])
        self.assertEqual(packet.payload, [PAYLOAD_HEADER, DST, SRC, REMOTE_CONTROL, 1, ON])

    def test_payload_with_multiple_data_bytes(self):
        packet = Packet(dst=DST, action=PUMP_PROGRAM, data=[SET, RPM, 5, 220])
        self.assertEqual(packet.payload, [PAYLOAD_HEADER, DST, SRC, PUMP_PROGRAM, 4, SET, RPM, 5, 220])
