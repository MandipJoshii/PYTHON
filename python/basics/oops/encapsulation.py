import json




class bankAccount:
    def __init__(bank,user,account):
        bank.user = user
        bank.__account = account

    def deposite(bank,amt):
        bank.__account += amt

    def display_accountBalance(bank):
        return bank.__account   

try:
    with open("getBalance.json","r") as f:
        content = f.read().strip()
        if content:
            balance = json.loads(content)["balance"]
        else:
            balance = 0    
except (FileNotFoundError,json.JSONDecodeError):
 balance = 0
acc = bankAccount("x",balance)


while True:
    
    print(f"YOUR CURRENT BALANCE: {acc.display_accountBalance()}")


    deposite = input("DO YOU WANT TO DEPOSITE MONEY IN YOUR ACCOUNT (Yes/No): ").lower()

    if deposite != "yes":
        print("DATA SAVED SUCCESSFULLY")
        break

    else:
        amount = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSITE: "))
        acc.deposite(amount)
    print(f"YOUR NEW BALANCE: {acc.display_accountBalance()}")

    with open("getBalance.json", "w") as f:
        json.dump({"balance": acc.display_accountBalance()}, f, indent=4)




