import requests
import time
from colorama import Fore, Style
import json
from prettytable import PrettyTable
import validators


def banner():
    Banner =r"""
      ________     _____   ____________ 
     /  _/ __ \   /  _/ | / / ____/ __ \
     / // /_/ /   / //  |/ / /_  / / / /
   _/ // ____/  _/ // /|  / __/ / /_/ / 
  /___/_/      /___/_/ |_/_/    \____/  
  """
    print(f"{Banner}")
    print(" ..: Code von @ShinyFire geschrieben :..")
banner()

def menü():
    return input("Über welche IP-Adresse möchtest du Infos: ")

def datencheck(ip):
    count = 1
    anzahl = 2
    if validators.ipv4(ip) or validators.ipv6(ip):
        while count < anzahl:
            print(f"[{Fore.GREEN}INFO{Fore.RESET}] Daten über {ip} auslesen...")
            time.sleep(1)
            count += 1
        return True
    else:
        print(f"[{Fore.RED}!{Fore.RESET}] Bitte gebe eine gültige IP-Adresse ein.")
        return False

def infoget(ip):
    base_url = "https://ipinfo.io/"
    complet_url = base_url + ip
    try:
        response = requests.get(complet_url)
        if response.status_code == 200:
            data = response.json()
            table = PrettyTable()
            table.field_names = ["Feld", "Wert"]
            table.add_row(["IP", data.get('ip', 'N/A')])
            table.add_row(["Hostname", data.get('hostname', 'N/A')])
            table.add_row(["Region", data.get('region', 'N/A')])
            table.add_row(["Stadt", data.get('city', 'N/A')])
            table.add_row(["Land", data.get('country', 'N/A')])
            print(table)
        else:
            print(f"[{Fore.RED}FEHLER{Fore.RESET}] Fehler beim Abrufen der Daten: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{Fore.RED}FEHLER{Fore.RESET}] Fehler: {e}")

def main():
    ip = menü()
    if datencheck(ip):
        infoget(ip)

main()


