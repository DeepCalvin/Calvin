import os

def checkNegativeNum(num):
    if num >= 0:
        return True
    else:
        return False

print("WELCOME TO CALTEASE BANK")

password = ""
incorrectPWcount = 1

first_time = input("\nIs this your first time using our service: ")

# First time using our service
if first_time.lower() == "yes" or first_time.lower() == "yep":

    # Variable
    bankCurrency = 0
    password="ILOVEYOU"
    print('\n\tYour password has been as "ILOVEYOU". You can change your password later. This is just your initrial password')

    f = open("CALTEASE_password.txt", "w+")
    f.write(password)
    f.close()

    pw = input("\nPlease enter your password here: ")

# User used our service before
else:
    if os.path.isfile("CALTEASE_password.txt"):
        f = open("CALTEASE_password.txt", "r")
        password=f.read()
        f.close()

        pw = input("\nPlease enter your password here: ")

    if not os.path.isfile("CALTEASE_password.txt"):
        print("\n\tError. Account password file not found. Recreating file...")

        password="ILOVEYOU"
        print("\n\tFile created")
        print('\n\tYour password has been as "ILOVEYOU". You can change your password later. This is just your initrial password')

        f = open("CALTEASE_password.txt", "w+")
        f.write(password)
        f.close()

        pw = input("\nPlease enter your password here: ")



# If password is incorrect
while pw != password:

    if incorrectPWcount==3:
        print("\n\tAuthorization failed")
        break

    print(f"\n\t Password authorization failed. {3-incorrectPWcount} attemps left.")
    pw = input("\nPlease enter your password here: ")
    incorrectPWcount+=1
        

# Password is correct
if pw == password:
    
    print("\n\tAuthorization succesful")

    # Main
    while True:
        print("\n1. Deposit\n2. Withdrawal\n3. Change password\n4. Exit")

        try:
            actions = int(input("\nEnter the number of actions here: "))

        except ValueError as err:
            print(f"\n\tError. Your input must be a number. Please try again later.")
            continue


        # Deoposit
        if actions==1:

            if os.path.isfile("CALTESE_bankInfo.txt") and first_time.lower() == "yes":

                f = open("CALTESE_bankInfo.txt", 'r')
                bankCurrencyNum = f.read()
                bankCurrency=eval(bankCurrencyNum)
                f.close()

                if bankCurrency==0:
                    bankCurrency=0
                    f = open("CALTESE_bankInfo.txt", 'w')
                    f.write(str(bankCurrency))
                    f.close()

                else: 
                    f = open("CALTESE_bankInfo.txt", 'r')
                    bankCurrencyNum = f.read()
                    bankCurrency=eval(bankCurrencyNum)
                    f.close()

            if os.path.isfile("CALTESE_bankInfo.txt"):
                f = open("CALTESE_bankInfo.txt", 'r')
                bankCurrencyNum = f.read()
                bankCurrency=eval(bankCurrencyNum)
                f.close()

            if not os.path.isfile("CALTESE_bankInfo.txt"):
                bankCurrency=0
                f = open("CALTESE_bankInfo.txt", 'w')
                f.write(str(bankCurrency))
                f.close()

                f = open("CALTESE_bankInfo.txt", 'r')
                bankCurrencyNum = f.read()
                bankCurrency=eval(bankCurrencyNum)
                f.close()

            try:
                depAmount = input("\nEnter the deposit amount here (If you did not enter anything, the initial deposit amount will be set as 100 NT): ")

            except ValueError as err2:
                print(f"\n\tError. {err2}")
                print("\n\tNothing has been deposited yet")
                continue

            if depAmount=="":
                depAmount="100"
                print("\n\tSince you did not enter anything, your initial deposit amount has been set as 100 NT: ")

            depositAmount = eval(depAmount)

            newBankCurrency = bankCurrency + depositAmount

            f = open("CALTESE_bankInfo.txt", 'w')
            f.write(str(newBankCurrency))
            f.close()

            print(f"\n\tSuccessfully deposited {depAmount} NT. Your bank account now has {newBankCurrency} NT")


        # Withdrawal
        elif actions == 2:

            if os.path.isfile("CALTESE_bankInfo.txt") and first_time.lower() == "yes":

                f = open("CALTESE_bankInfo.txt", 'r')
                bankCurrencyNum = f.read()
                bankCurrency=eval(bankCurrencyNum)
                f.close()

                if bankCurrency==0:
                    bankCurrency=0
                    f = open("CALTESE_bankInfo.txt", 'w')
                    f.write(str(bankCurrency))
                    f.close()

                else: 
                    f = open("CALTESE_bankInfo.txt", 'r')
                    bankCurrencyNum = f.read()
                    bankCurrency=eval(bankCurrencyNum)
                    f.close()

            if os.path.isfile("CALTESE_bankInfo.txt"):
                f = open("CALTESE_bankInfo.txt", 'r')
                bankCurrencyNum = f.read()
                bankCurrency=eval(bankCurrencyNum)
                f.close()

            if not os.path.isfile("CALTESE_bankInfo.txt"):
                bankCurrency=0
                f = open("CALTESE_bankInfo.txt", 'w')
                f.write(str(bankCurrency))
                f.close()

                f = open("CALTESE_bankInfo.txt", 'r')
                bankCurrencyNum = f.read()
                bankCurrency=eval(bankCurrencyNum)
                f.close()

            try:
                withd = int(input("\nEnter the withdraw amount here: "))

            except ValueError as err3:
                print(f"\n\tError. Your input must be a number. Please try again later.")
                continue

            amountLeft = bankCurrency-withd

            # If the bank account has enough money for withdraw
            if checkNegativeNum(amountLeft)==True:
                f = open("CALTESE_bankInfo.txt", 'w')
                f.write(str(amountLeft))
                f.close()

                print(f"\n\tSuccessfully withdrew {withd} NT. Your bank account now has {amountLeft} NT left")

            # If bank account don't have enough money for withdraw (Insifficient funds)
            else:
                print("\n\tInsufficient funds.")
                print("\n\tNo money has been withdrew yet.")
                continue


        # Change password
        elif actions == 3:
            newPW = input("\nEnter the new password here: ")
            
            if os.path.isfile("CALTEASE_password.txt"):
                f = open("CALTEASE_password.txt", "w")
                f.write(newPW)
                f.close()

                f = open("CALTEASE_password.txt", "r")
                password=f.read()
                f.close()

                print("\n\tPassword has been successfully changed")

            if not os.path.isfile("CALTEASE_password.txt"):
                print("\n\tError. Account password file not found. Recreating file...")
                print("\n\tFile created")

                f = open("CALTEASE_password.txt", "w+")
                f.write(newPW)
                f.close()

                f = open("CALTEASE_password.txt", "r")
                password=f.read()
                f.close()

                print("\n\tPassword has been successfully changed")

            pw = input("\nPlease enter your password here: ")

            # If password is incorrect
            incorrectPWcount=1
            while pw != password:

                if incorrectPWcount==3:
                    print("\n\tAuthorization failed")
                    break

                print(f"\n\tPassword authorization failed. {3-incorrectPWcount} attemps left.")
                pw = input("\nPlease enter your password here: ")
                incorrectPWcount+=1


        # Exit
        elif actions == 4:
            print("\n\tThank you for using our service. See you next time! Have a lovely day!")
            break

        # If invalid
        elif actions!=1 or actions!=2 or actions!=4:
            print("\n\tInvalid input. Please enter a number from 1~4 to select your action")



            












