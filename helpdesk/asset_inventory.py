"""
Asset Inventory Tool
-----------------------
A simple command-line asset tracker for helpdesk use — add, view,
update, and remove IT assets (laptops, monitors, etc.), stored
locally as JSON. Includes CSV export for reporting.

Usage:
    python asset_inventory.py
"""

import json
import csv
import os
from datetime import datetime

DATA_FILE = "asset_inventory.json"


def load_assets() -> list[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_assets(assets: list[dict]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=2)


def add_asset(assets: list[dict]) -> None:
    print("\n--- Add New Asset ---")
    asset_id = input("Asset ID (e.g. LAP-001): ").strip()

    if any(a["asset_id"] == asset_id for a in assets):
        print("An asset with this ID already exists.\n")
        return

    asset = {
        "asset_id": asset_id,
        "type": input("Type (e.g. Laptop, Monitor, Phone): ").strip(),
        "assigned_to": input("Assigned to (name or 'Unassigned'): ").strip(),
        "location": input("Location: ").strip(),
        "status": input("Status (Active/Repair/Retired): ").strip(),
        "date_added": datetime.now().strftime("%Y-%m-%d"),
    }
    assets.append(asset)
    save_assets(assets)
    print(f"Asset '{asset_id}' added.\n")


def view_assets(assets: list[dict]) -> None:
    if not assets:
        print("\nNo assets found.\n")
        return

    print("\n" + "=" * 90)
    print(f"{'ID':<10}{'Type':<12}{'Assigned To':<18}{'Location':<15}{'Status':<12}{'Added':<12}")
    print("=" * 90)
    for a in assets:
        print(f"{a['asset_id']:<10}{a['type']:<12}{a['assigned_to']:<18}"
              f"{a['location']:<15}{a['status']:<12}{a['date_added']:<12}")
    print("=" * 90 + f"\nTotal assets: {len(assets)}\n")


def update_asset(assets: list[dict]) -> None:
    asset_id = input("\nEnter Asset ID to update: ").strip()
    for a in assets:
        if a["asset_id"] == asset_id:
            print("Leave blank to keep current value.")
            new_status = input(f"Status [{a['status']}]: ").strip()
            new_assigned = input(f"Assigned to [{a['assigned_to']}]: ").strip()
            new_location = input(f"Location [{a['location']}]: ").strip()

            if new_status:
                a["status"] = new_status
            if new_assigned:
                a["assigned_to"] = new_assigned
            if new_location:
                a["location"] = new_location

            save_assets(assets)
            print(f"Asset '{asset_id}' updated.\n")
            return
    print("Asset ID not found.\n")


def remove_asset(assets: list[dict]) -> None:
    asset_id = input("\nEnter Asset ID to remove: ").strip()
    for a in assets:
        if a["asset_id"] == asset_id:
            confirm = input(f"Remove '{asset_id}' ({a['type']})? (y/n): ").strip().lower()
            if confirm == "y":
                assets.remove(a)
                save_assets(assets)
                print(f"Asset '{asset_id}' removed.\n")
            else:
                print("Cancelled.\n")
            return
    print("Asset ID not found.\n")


def export_csv(assets: list[dict]) -> None:
    if not assets:
        print("\nNo assets to export.\n")
        return

    filename = f"asset_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=assets[0].keys())
        writer.writeheader()
        writer.writerows(assets)
    print(f"\nExported {len(assets)} assets to '{filename}'.\n")


def main():
    assets = load_assets()

    menu = """
Asset Inventory Tool
1. View all assets
2. Add new asset
3. Update asset
4. Remove asset
5. Export to CSV
6. Quit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_assets(assets)
        elif choice == "2":
            add_asset(assets)
        elif choice == "3":
            update_asset(assets)
        elif choice == "4":
            remove_asset(assets)
        elif choice == "5":
            export_csv(assets)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-6.\n")


if __name__ == "__main__":
    main()