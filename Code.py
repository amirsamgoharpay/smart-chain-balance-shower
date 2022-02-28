import requests
import json
key = "" # pls add your api key from https://bscscan.com/
url = "https://api.bscscan.com/api"

def bnbbalance(x):
    res = requests.get(f"{url}?module=account&action=balance&address={x}&apikey={key}", headers={"Accept": "application/json"})
    resjson = res.json()
    results = int(resjson["result"])/1E+18
    return f"you have : {str(results)} bnb on {add} wallet"

  


add = str(input("address : ")) 

balance = bnbbalance(add)



# you can use this code as module in python just use import filename
# then you can use bnbbalance with this code 
'''
import filename
balance = filename.bnbbalance(address)
'''
