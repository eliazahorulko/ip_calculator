import ipaddress

def calculate_network_id(ip_address, subnet_mask):
    # Split IP address and subnet mask into octets
    ip_octets = list(map(int, ip_address.split(".")))
    mask_octets = list(map(int, subnet_mask.split(".")))
    # Perform bitwise AND operation between IP and subnet mask
    network_octets = [ip_octets[i] & mask_octets[i] for i in range(4)]
    # Return the network ID as a string
    return ".".join(map(str, network_octets))

def calculate_broadcast_address(network_id, subnet_mask):
    # Create an IPv4Network object and calculate the broadcast address
    network = ipaddress.IPv4Network(f"{network_id}/{subnet_mask}", strict=False)
    return str(network.broadcast_address)

def find_common_subnet(ip1, ip2):
    # Convert IP addresses to IPv4Address objects
    ip1_obj = ipaddress.IPv4Address(ip1)
    ip2_obj = ipaddress.IPv4Address(ip2)
    # Start with the largest prefix length (most specific subnet)
    for prefix_len in range(32, -1, -1):
        # Create a subnet using the current prefix length
        network = ipaddress.IPv4Network(f"{ip1}/{prefix_len}", strict=False)
        # Check if the second IP address belongs to the subnet
        if ip2_obj in network:
            return network  # Return the smallest subnet that contains both IPs

