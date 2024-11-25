import unittest
from ip_calc import calculate_network_id, calculate_broadcast_address, find_common_subnet

class TestIPCalculator(unittest.TestCase):
    def test_calculate_network_id(self):
        # Test network ID calculation
        self.assertEqual(calculate_network_id("192.168.4.75", "255.255.255.224"), "192.168.4.64")

    def test_calculate_broadcast_address(self):
        # Test broadcast address calculation
        self.assertEqual(calculate_broadcast_address("192.168.4.64", 27), "192.168.4.95")

    def test_find_common_subnet(self):
        # Test finding the smallest common subnet for two IPs
        subnet = find_common_subnet("192.168.4.75", "192.168.3.100")
        self.assertEqual(str(subnet), "192.168.0.0/21")
