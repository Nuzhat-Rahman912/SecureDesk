"""
IP Information Lookup Tool
----------------------------
Looks up geolocation and network info for an IP address, or fetches
the user's own public IP if none is provided. Uses the free ip-api.com
service (no API key required, reasonable rate limits for personal use).

Usage:
    python ip_information.py
"""

import re
import requests

IP_API_URL = "http://ip-api.com/json/{ip}"


def is_valid_ip(ip: str) -> bool:
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    return all(0 <= int(octet) <= 255 for octet in ip.split('.'))


def get_own_public_ip() -> str:
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        return response.json()["ip"]
    except requests.RequestException as e:
        print(f"Error retrieving your public IP: {e}")
        return ""


def lookup_ip(ip: str) -> dict | None:
    try:
        response = requests.get(IP_API_URL.format(ip=ip), timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "fail":
            print(f"Lookup failed: {data.get('message', 'unknown error')}")
            return None
        return data
    except requests.RequestException as e:
        print(f"Error looking up IP: {e}")
        return None


def print_report(data: dict) -> None:
    print("\n" + "=" * 40)
    print(" IP INFORMATION REPORT")
    print("=" * 40)
    print(f"IP Address   : {data.get('query', 'N/A')}")
    print(f"Country      : {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
    print(f"Region       : {data.get('regionName', 'N/A')}")
    print(f"City         : {data.get('city', 'N/A')}")
    print(f"ZIP Code     : {data.get('zip', 'N/A')}")
    print(f"Latitude     : {data.get('lat', 'N/A')}")
    print(f"Longitude    : {data.get('lon', 'N/A')}")
    print(f"Timezone     : {data.get('timezone', 'N/A')}")
    print(f"ISP          : {data.get('isp', 'N/A')}")
    print(f"Organization : {data.get('org', 'N/A')}")
    print(f"AS           : {data.get('as', 'N/A')}")
    print("=" * 40 + "\n")


def main():
    print("IP Information Lookup Tool")
    print("Enter an IP address to look up, or press Enter to check your own public IP.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("IP address (or Enter for your own): ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if user_input == "":
            print("Fetching your public IP...")
            ip = get_own_public_ip()
            if not ip:
                continue
            print(f"Your public IP is: {ip}")
        else:
            if not is_valid_ip(user_input):
                print("Invalid IP address format. Try again (e.g. 8.8.8.8).\n")
                continue
            ip = user_input

        data = lookup_ip(ip)
        if data:
            print_report(data)


if __name__ == "__main__":
    main()