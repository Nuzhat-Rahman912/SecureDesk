"""
Subnet Calculator
-------------------
Calculates network details from an IP address and CIDR notation or
subnet mask — network address, broadcast address, usable host range,
number of usable hosts, and subnet mask.

Usage:
    python subnet_calculator.py
"""

import ipaddress


def parse_input(user_input: str) -> ipaddress.IPv4Network | None:
    try:
        # strict=False allows host bits to be set (e.g. 192.168.1.5/24)
        network = ipaddress.ip_network(user_input, strict=False)
        return network
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


def print_report(network: ipaddress.IPv4Network) -> None:
    total_addresses = network.num_addresses
    usable_hosts = max(total_addresses - 2, 0) if network.prefixlen < 31 else total_addresses

    print("\n" + "=" * 45)
    print(" SUBNET CALCULATOR REPORT")
    print("=" * 45)
    print(f"Network Address     : {network.network_address}")
    print(f"Broadcast Address   : {network.broadcast_address}")
    print(f"Subnet Mask         : {network.netmask}")
    print(f"CIDR Notation       : /{network.prefixlen}")
    print(f"Wildcard Mask       : {network.hostmask}")
    print(f"Total Addresses     : {total_addresses}")
    print(f"Usable Host Range   : ", end="")

    if network.prefixlen < 31:
        hosts = list(network.hosts())
        if hosts:
            print(f"{hosts[0]} - {hosts[-1]}")
        else:
            print("None")
    else:
        print("N/A (point-to-point or single host subnet)")

    print(f"Usable Hosts        : {usable_hosts}")
    print(f"Is Private          : {network.is_private}")
    print("=" * 45 + "\n")


def main():
    print("Subnet Calculator")
    print("Enter an IP with CIDR notation (e.g. 192.168.1.0/24)")
    print("or with a subnet mask (e.g. 192.168.1.0/255.255.255.0)")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter network: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if not user_input:
            print("Please enter a value.\n")
            continue

        network = parse_input(user_input)
        if network:
            print_report(network)


if __name__ == "__main__":
    main()