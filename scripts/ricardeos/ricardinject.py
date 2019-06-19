import re
import requests
import json
import os

#onchain_abi = requests.post("https://mainnet.eos.dfuse.io/v1/chain/get_abi", json={"account_name": "eosio"})
#onchain_abi = requests.post("https://kylin.eos.dfuse.io/v1/chain/get_abi", json={"account_name": "eosio"})
onchain_abi = requests.post("https://jungle.eos.dfuse.io/v1/chain/get_abi", json={"account_name": "eosio"})


source = open("../../eosio.system/eosio.system.contracts.md").read()

split = re.compile(r"<h1 ")

entries = split.split(source)

matcher = re.compile(r'class="(.*)">(.*)</h1>(.*)', flags=re.MULTILINE|re.DOTALL)

mapping = {"contract": {}, "clause": []}

for entry in entries:
    res = matcher.match(entry)
    if res == None:
        # print("woahh, nothign amtched here", entry)
        continue

    section = res.group(1)
    name = res.group(2)
    ricardian = res.group(3).strip()

    if section == "contract":
        mapping["contract"][name] = ricardian
    elif section == "clause":
        mapping["clause"].append((name, ricardian))
    else:
        raise Exception(f"no such section {section}")


abi = onchain_abi.json()["abi"]


for act in abi["actions"]:
    ricardian = mapping["contract"].get(act["name"])
    if ricardian is not None:
        act["ricardian_contract"] = ricardian

for clause in mapping["clause"]:
    abi["ricardian_clauses"].append({"id": clause[0], "body": clause[1]})

print(json.dumps(abi))
