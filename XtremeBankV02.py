from datetime import datetime

simdi = datetime.now()


def infocustomer():
    userinfo = {"Ahmet": 0, "Zeynep": 5000, "Alberto": 0}
    return userinfo


amountbanks = infocustomer()


def pascustomer():
    user = {"Ahmet": "1234", "Zeynep": "4321", "Alberto": "4422"}
    return user


usersdic = pascustomer()


def customeractivities():
    sozluk = {"Zeynep": {"Zeynep's Withdrawls": " ", "Zeynep's Deposits": " ", "Zeynep's Transfers": " "},
              "Ahmet": {"Ahmet's Withdrawls": " ", "Ahmet's Deposits": " ", "Ahmet's Transfers": " "},
              "Alberto": {"Alberto's Withdrawls": " ", "Alberto's Deposits": " ", "Alberto's Transfers": " "}}
    return sozluk


sozluk1 = customeractivities()


def entry():
    simdi = datetime.now()
    print("    --- Welcome to Xtreme Bank V.0.2 ---")
    print(" -------------------------------------")
    print("/                                       \\")
    print("                ISTANBUL                  ")
    print("|                                        |")
    print("            ", simdi.strftime("%Y-%m-%d %H:%M"))
    print("\\                                        /")
    print("  -------------------------------------")
    print("1. Login \n2. Exit")
    userchoice = input(">>>")
    while True:
        if userchoice == "1":
            print("What do you want to login as:\n1.Admin \n2.User \n3.Go Back")
            userchoice2 = input(">>>")
            if userchoice2 == "1":
                loginadmin()
                adminservices()
            if userchoice2 == "2":
                loginuser()
                services()
                break
            if userchoice2 == "3":
                entry()
            else:
                userchoice2 = input("Please enter valid number")
        if userchoice == "2":
            print("Exited")
            break
        else:
            userchoice = input("Please enter valid number")


def loginadmin():
    global username
    complete = False
    admin = {"Ibrahim": "1122"}

    while not complete:
        username = input("Username:")
        password = input("Password:")

        if not username in admin:  # check to see if user does not exists
            print("Input username again!")
            continue
        if password == admin[username]:  # check to see if password match
            print(" Welcome", username, "!")
            complete = True
        else:
            print("Input password again")


def adminservices():
    print("Please enter the number of the service:")
    print("1. Add User\n2. Remove User \n3. Display All Users \n 4. Admin Exit")
    num = int(input(">>>"))
    while True:
        if num == 1:
            adduser()
            break
        if num == 2:
            removeuser()
            break
        if num == 3:
            displayusers()
            break
        if num == 4:
            entry()
            break

        else:
            num = int(input("Please enter valid number"))


def adduser():
    print("Access Granted")
    newusername = input("Please enter the new user name: ")
    newuserpassword = input("Please enter the new user password: ")
    usersdic[newusername] = newuserpassword
    print(f"{newusername} added.")
    adminservices()


def removeuser():
    print("Access Granted")
    removeusername = input("Please remove the user name: ")
    while True:
        if removeusername in usersdic:
            del usersdic[removeusername]
            print(removeusername + " was removed.")
            break
        else:
            removeusername = input("Please enter a valid name for remove: ")
    adminservices()


def displayusers():
    for a, b in usersdic.items():
        print(a, b)
    adminservices()


def loginuser():
    global username
    complete = False
    user = {"Ahmet": "1234", "Zeynep": "4321", "Alberto": "4321"}
    while not complete:
        username = input("Username:")
        password = input("Password:")
        if not username in usersdic.keys():  # check to see if user does not exists
            print("Input username again!")
            continue
        if password == usersdic[username]:  # check to see if password match
            print(" Welcome", username, "!")
            complete = True
        else:
            print("Input password again")


def services():
    print("Please enter the number of the service:")
    print("1. Withdraw Money\n2. Deposit Money\n3. Transfer Money\n4. My Account Information\n5. Logout")
    num = int(input(">>>"))
    while True:
        if num == 1:
            WithdrawMoney()
            break
        if num == 2:
            DepositMoney()
            break
        if num == 3:
            TransferMoney()
            break
        if num == 4:
            AccountInformation()
            break
        if num == 5:
            Logout()
            break
        else:
            num = int(input("Please enter valid number"))


def WithdrawMoney():
    withdrawn = int(input("Please enter the amount you want to withdraw:"))
    if amountbanks[username] >= withdrawn:
        amountbanks[username] -= withdrawn
        tarih_saat = datetime.now()
        kayit = f"{tarih_saat}: {withdrawn} TL para çekildi."
        withdrawls_kaydet(kayit)
        print(f"{withdrawn} TL withdrawn from your account\nGoing back to main menu...")
        services()
    else:
        print(f"you don't have {withdrawn} TL in your account\nGoing back to main menu...")
        services()


def DepositMoney():
    deposit = int(input("Please enter the amount you want to drop:"))
    amountbanks[username] += deposit
    tarih_saat1 = datetime.now()
    kayit = f"{tarih_saat1}: {deposit} TL para yatırıldı."
    deposit_kaydet(kayit)
    print(f"{deposit} TL added to your account\nGoing back to main menu...")
    services()


def TransferMoney():
    transferisim = input(
        "Warning:If you want to abort transfer please enter abort. \n Please enter the name of the user you want transfer money to:")
    while True:
        if transferisim == "abort":
            services()
        if transferisim == username:
            print("Please enter a name that is not your own name")
            transferisim = input(
                "Warning:If you want to abort transfer please enter abort. \n Please enter the name of the user you want transfer money to:")
            continue
        if transferisim in amountbanks.keys():
            transferred = int(input("Please enter the amount you want to transfer:"))
            if amountbanks[username] >= transferred:
                amountbanks[username] -= transferred
                amountbanks[transferisim] += transferred
                print(f"Money transferred successuffly!\nGoing back to main menu...")
                tarih_saat1 = datetime.now()
                kayit = f"{tarih_saat1}: Transferred to {transferisim} {transferred} TL "
                transfer_kaydet(kayit)
                kayit2 = f"{tarih_saat1}: Transferred to me from {username} {transferred} TL  "
                if transferisim == "Zeynep":
                    with open("zeyneptransfers.txt", "a") as dosya1:
                        dosya1.write(kayit2)
                    with open("zeyneptransfers.txt", "r") as dosya1:
                        icerik = dosya1.readlines()
                        sozluk1["Zeynep"]["Zeynep's Transfers"] = icerik
                if transferisim == "Ahmet":
                    with open("ahmettransfers.txt", "a") as dosya1:
                        dosya1.write(kayit2)
                    with open("ahmettransfers.txt", "r") as dosya1:
                        icerik = dosya1.readlines()
                        sozluk1["Ahmet"]["Ahmet's Transfers"] = icerik
                if transferisim == "Alberto":
                    with open("albertotransfers.txt", "a") as dosya1:
                        dosya1.write(kayit2)
                    with open("albertotransfers.txt", "r") as dosya1:
                        icerik = dosya1.readlines()
                        sozluk1["Alberto"]["Alberto's Transfers"] = icerik

                print(f"{transferred} TL transferred to your account\nGoing back to main menu...")
                services()
            else:
                print("Sorry!, you don't have the entered amount\nGoing back to main menu...")
                print("1. Go back to main menu\n2. Transfer again")
                num = int(input(">>>"))
                while True:
                    if num == 1:
                        services()
                        break
                    if num == 2:
                        TransferMoney()
                        break
                    else:
                        num = input("Please enter valid number")
        else:
            transferisim = input("Please enter valid name: ")


def withdrawls_kaydet(kayit):
    if username == "Zeynep":
        with open("zeynepwithdrawls.txt", "a") as dosya1:
            dosya1.write(kayit)
        with open("zeynepwithdrawls.txt", "r") as dosya1:
            icerik = dosya1.readlines()
            sozluk1["Zeynep"]["Zeynep's Withdrawls"] = icerik
    if username == "Ahmet":
        with open("ahmetwithdrawls.txt", "a") as dosya1:
            dosya1.write(kayit)
        with open("ahmetwithdrawls.txt", "r") as dosya1:
            icerik = dosya1.readlines()
            sozluk1["Ahmet"]["Ahmet's Withdrawls"] = icerik
    if username == "Alberto":
        with open("albertowithdrawls.txt", "a") as dosya1:
            dosya1.write(kayit)
        with open("albertowithdrawls.txt", "r") as dosya1:
            icerik = dosya1.readlines()
            sozluk1["Alberto"]["Alberto's Withdrawls"] = icerik


def deposit_kaydet(kayit):
    if username == "Zeynep":
        with open("zeynepdeposits.txt", "a") as dosya1:
            dosya1.write(kayit)
        with open("zeynepdeposits.txt", "r") as dosya1:
            icerik = dosya1.readlines()
            sozluk1["Zeynep"]["Zeynep's Deposits"] = icerik
    if username == "Ahmet":
        with open("ahmetdeposits.txt", "a") as dosya1:
            dosya1.write(kayit)
        with open("ahmetdeposits.txt", "r") as dosya1:
            icerik = dosya1.readlines()
            sozluk1["Ahmet"]["Ahmet's Deposits"] = icerik
    if username == "Alberto":
        with open("albertodeposits.txt", "a") as dosya1:
            dosya1.write(kayit)
        with open("albertodeposits.txt", "r") as dosya1:
            icerik = dosya1.readlines()
            sozluk1["Alberto"]["Alberto's Deposits"] = icerik


def transfer_kaydet(kayit):
    if username == "Zeynep":
        with open("zeyneptransfers.txt", "a") as dosya1:
            dosya1.write(kayit)
        with open("zeyneptransfers.txt", "r") as dosya1:
            icerik = dosya1.readlines()
            sozluk1["Zeynep"]["Zeynep's Transfers"] = icerik
    if username == "Ahmet":
        with open("ahmettransfers.txt", "a") as dosya1:
            dosya1.write(kayit)
        with open("ahmettransfers.txt", "r") as dosya1:
            icerik = dosya1.readlines()
            sozluk1["Ahmet"]["Ahmet's Transfers"] = icerik
    if username == "Alberto":
        with open("albertotransfers.txt", "a") as dosya1:
            dosya1.write(kayit)
        with open("albertotransfers.txt", "r") as dosya1:
            icerik = dosya1.readlines()
            sozluk1["Alberto"]["Alberto's Transfers"] = icerik


def AccountInformation():
    user = {"Ahmet": "1234", "Zeynep": "4321", "Alberto": "4422"}

    print(f"Your Name:{username}\nYour Password:{user[username]}\nYour Amount(TL): {amountbanks[username]}")
    print("User's Activities Reports:")
    if username == "Zeynep":
        for anahtar, deger in sozluk1["Zeynep"].items():
            print(anahtar)
            print(deger)
            print()
    if username == "Ahmet":
        for anahtar, deger in sozluk1["Ahmet"].items():
            print(anahtar)
            print(deger)
            print()
    if username == "Alberto":
        for anahtar, deger in sozluk1["Alberto"].items():
            print(anahtar)
            print(deger)
            print()

    print("Going back to main menu...")
    services()


def Logout():
    print(f"Good Bye {username} !")
    entry()


entry()

#######################################################



