import pickle
import os
import pathlib
class Account :
    AccNo = 0
    Name = ''
    Deposit=0
    PIN=0
    Mobile_No =0
    Address=''
    p=0
    
    def createAccount(self):
        self.AccNo= int(input("Enter the account no : "))
        self.Name = input("Enter the account holder name : ")
        self.PIN=int(input("Enter PIN For Your Account : "))
        self.Deposit = int(input("Enter The Initial Amount To Deposit : "))
        self.Mobile_No=int(input("Enter Mobile No. :"))
        print("\n\n\t\t\tAccount Created\n\n")

def intro():
    print("\t\t\t\t\t\t* WELCOME TO VJTI ATM *")
    input()

def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)        

def Deposit(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :

            if item.AccNo == num:
                n=0
                while n<3:
                    pin =int(input("\n\tEnter Your PIN No. : "))
                    if item.PIN ==pin:
                        amount = int(input("\t\nEnter the amount to deposit : "))
                        item.Deposit += amount
                        print("\t\nDeposit Successfull.")
                        break
                    else:
                        print("\t\tWrong PIN.")    
                        n=n+1
                else:
                    print("You Have entered Wrong PIN for 3 times. \n\tACCOUNT SUSPENDED TEMPORARY.")        
            else:
                print("\tAccount doesn't Exist. ")    

    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

def Withdraw(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.AccNo == num :
                n=0
                while n<3:
                    pin =int(input("\n\tEnter Your PIN No. : "))
                    if item.PIN ==pin:
                        amount = int(input("\tEnter the amount to Withdraw : "))
                        if amount <= item.Deposit :
                            item.Deposit -= amount
                            print("\t\nCollect Your Cash")
                        else:
                            print("\n\tYou cannot withdraw larger Amount than your Current Balance.\n")
                        break
                    else:
                        print("\t\tWrong PIN.")    
                        n=n+1
                else:
                    print("You Have entered Wrong PIN for 3 times. \n\tACCOUNT SUSPENDED TEMPORARY.")        
            else:
                print("\tAccount doesn't Exist. ")        
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

def balanceInquiry(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.AccNo == num :
                n=0
                while n<3:
                    pin =int(input("\n\tEnter Your PIN No. : "))
                    if item.PIN ==pin:
                        print("\n\tYour account Balance is = ",item.Deposit)
                        found = True
                        break
                    else:
                        print("\t\tWrong PIN.")    
                        n=n+1
                else:
                    print("You Have entered Wrong PIN for 3 times. \n\tACCOUNT SUSPENDED TEMPORARY.")        
            else:
                print("\tAccount doesn't Exist. ")
    else :
        print("No records to Search")

def PINchange(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.AccNo == num:
                n=0
                while n<3:
                    pin =int(input("\n\tEnter Your PIN No. : "))
                    if item.PIN ==pin:
                        NewPIN=int(input("\t\nEnter New PIN No. : "))
                        item.PIN=NewPIN
                        print("\t\nPIN Changed Successfully")
                        break
                    else:
                        print("\t\tWrong PIN.")    
                        n=n+1
                else:
                    print("You Have entered Wrong PIN for 3 times. \n\tACCOUNT SUSPENDED TEMPORARY.")        
            else:
                print("\tAccount doesn't Exist. ")
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


intro()
print("\t\t- MAIN MENU -\n")
print("\t1. CREATE NEW ACCOUNT")
print("\t2. DEPOSIT AMOUNT")
print("\t3. WITHDRAW AMOUNT")
print("\t4. BALANCE ENQUIRY")
print("\t5. PIN Change ")
print("\t6. EXIT")
print("\tSelect Your Option (1-6) ")
ch = int(input())
def AccNum():
    num = int(input("\tEnter The Account No. : "))
    return num
    
if ch == 1:
    writeAccount()
if 1<ch<6:
    num = AccNum()
    if ch ==2:
        Deposit(num)
    if ch == 3:
        Withdraw(num)
    if ch == 4:
        balanceInquiry(num)
    if ch == 5:
        PINchange(num)
if ch == 6:
    print("\tThanks for using VJTI ATM ")
if ch<=0 or ch>=7:
    print("\tInvalid choice")
