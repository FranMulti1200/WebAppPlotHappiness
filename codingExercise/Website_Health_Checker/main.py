import requests
import datetime
import csv


FILEPATH = "websites.txt"

def get_webs(filepath=FILEPATH):
    with open(filepath, "r") as webs_list:
        webs = webs_list.readlines()
    return webs

list_webs = get_webs(FILEPATH)

webs = []
for web in list_webs:
    web = web.strip('\n')
    webs.append(web)

print(f"Checking {len(webs)} websites...")
for item in webs:
    try:
        r = requests.get(item)
    except Exception:
        print(f"{item} - Offline - N/A")
        continue
    print(f"{item} - Online - {r.status_code}")

