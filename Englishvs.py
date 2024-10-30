import requests
import time
from colorama import Fore, Style
import json
from prettytable import PrettyTable
import validators


def banner():
    Banner = r"""
      ________     _____   ____________ 
     /  _/ __ \   /  _/ | / / ____/ __ \
     / // /_/ /   / //  |/ / /_  / / / /
   _/ // ____/  _/ // /|  / __/ / /_/ / 
  /___/_/      /___/_/ |_/_/    \____/  V.1.0
  """
    print(f"{Banner}")
    print(" ..: Code by @ShinyFire written :..")


def menu():
    return input("Which IP address would you like information about: ")


def data_check(ip):
    if validators.ipv4(ip) or validators.ipv6(ip):
        print(f"[{Fore.GREEN}INFO{Fore.RESET}] Retrieving data for {ip}...")
        time.sleep(1)  
        return True
    else:
        print(f"[{Fore.RED}!{Fore.RESET}] Please enter a valid IP address.")
        return False


def info_get(ip):
    base_url = "https://ipinfo.io/"
    complete_url = base_url + ip
    try:
        response = requests.get(complete_url)
        if response.status_code == 200:
            data = response.json()
            table = PrettyTable()
            table.field_names = ["Field", "Value"]
            table.add_row(["IP", data.get('ip', 'N/A')])
            table.add_row(["Hostname", data.get('hostname', 'N/A')])
            table.add_row(["Region", data.get('region', 'N/A')])
            table.add_row(["City", data.get('city', 'N/A')])
            table.add_row(["Country", data.get('country', 'N/A')])
            print(table)
        else:
            print(f"[{Fore.RED}ERROR{Fore.RESET}] Error retrieving data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{Fore.RED}ERROR{Fore.RESET}] Error: {e}")


def main():
    banner()
    while True:
        ip = menu()
        if data_check(ip):
            info_get(ip)
        another_query = input("Would you like to query another IP address? (yes/no): ").strip().lower()
        if another_query != 'yes':
            print(f"{Fore.YELLOW}Exiting the program...{Fore.RESET}")
            break


if __name__ == "__main__":
    main()
