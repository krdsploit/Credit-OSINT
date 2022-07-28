from attr import validate
from card_identifier.cardutils import validate_card
from card_identifier.card_type import identify_card_type
from card_identifier.card_issuer import identify_card_issuer
import ccard
from bank_card import BankCard
import colorama
from payment_card_identifier import CardIdentifier

banner = '''




░█████╗░░░░░░░░█████╗░░██████╗██╗███╗░░██╗████████╗
██╔══██╗░░░░░░██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝
██║░░╚═╝█████╗██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░
██║░░██╗╚════╝██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░
╚█████╔╝░░░░░░╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░
░╚════╝░░░░░░░░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░

[+] Title => C-OSINT [*]
[*] Coder => Krd-Pentester [*]
[*] Version => 0.1 [*] 


                '''


def menu():
    print("[1-] Credit Card Validation : ")
    print("[2-] Credit Card Type : ")
    print("[3-] Credit Card Issuer :")
    print("[4-] Credit Card Generator :")
    print("[5-] BankCard : ")
    print("[6-] Card Identify :")

    ya_choice = int(input("Choose Ya Option Buddy =>"))

    if ya_choice==1:
        valid()
    elif ya_choice==2:
        typer()
    elif ya_choice==3:
        issuer()

    elif ya_choice==4:

        creadit_gene()

    elif ya_choice==5:
        BnkCard()
    elif ya_choice==6:
        identifer()
  


def valid():
    from card_identifier.cardutils import validate_card
    Credit_card_numbers = input("Enter Your Credit Card Numbers => ")
    Validate = validate_card(Credit_card_numbers)
    print(Validate)
   


def typer():
    Credit_card_numbers = input("Enter Your Credit Card Numbers => ")
    Validate = identify_card_type(Credit_card_numbers)
    print(Validate)
    
    
def issuer():
    Credit_card_numbers = input("Enter Your Credit Card Numbers => ")
    Validate = identify_card_issuer(Credit_card_numbers)
    print(Validate)
   

def creadit_gene():
    print("[+] Master Card => ")
    print("[+] Visa Card => ")
    print("[+] Discover => ")
    print("[+] American Express => ")

    credit_type = int(input("===>"))

    if credit_type==1:
        mst()
    elif credit_type==2:
        vis()
    elif credit_type==3:
        disc()
    elif creadit_gene==4:
        american()



def mst():
    x = ccard.mastercard()
    print(x)



def vis():

    y = ccard.visa()
    print(y)

def disc():
    z = ccard.discover()
    print(z)

def american():
    a = ccard.americanexpress()
    print(a)


def BnkCard():

    bank_card_number = input("Bank Card Number ==>")
    bank_name = BankCard(bank_card_number)
    print(bank_name)


def identifer():
    import json
    bank_card_number = input("Bank Card Number ==>")
    ya_card = CardIdentifier.from_numbers(bank_card_number)
    print(ya_card)


if __name__ == "__main__":
    menu()
    creadit_gene