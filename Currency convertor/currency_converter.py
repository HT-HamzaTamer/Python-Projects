import requests

init_currency = input("enter the initial currency : ")
target_currency = input("enter the target currency : ")

while True :
    try :
        amount = float(input("enter the amount : "))
    except :
        print("the amount must be numeric value")
        continue

    if amount <= 0 :
        print("must be greater than 0")
        continue
    else:
        break


url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "Q2AoX9MWrE3GWW1RM9WvxsnnHsPELFB5"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if status_code != 200 :
    print("error, try again")
    quit()

result = response.json()

print(f"{amount} {init_currency} = {result["result"]} {target_currency}")