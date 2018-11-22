import datetime
import sys
from classes.client import Client
from classes.credit import Credit

now = datetime.datetime.now()
line = '-----------------------------------------'

def getClientData():
    print(line)
    print('Credit Loan Application')
    print(line)
    print('Today: ' + now.strftime("%Y-%m-%d %H:%M"))
    print(line)
    print('Please input the needed information below! ')
    print(line)
    
    firstName = input('Client first name: ')
    lastName = input('Client last name: ')
    age = input('Client age: ')
    income = input('Client income: ')
    needToBorrow = input('Client need to borrow: ')

    return {
        'firstName': firstName,
        'lastName': lastName,
        'age': age,
        'income': income,
        'needToBorrow': needToBorrow
    }

def printActionOptions():
    print(line)
    print('Please select an option to continue')
    print('To select an option just type the option number, i.e. 6, and press enter')
    print(line)
    print('[1] Determine if client is eligible')
    print('[2] Set Loan Period')
    print('[3] Client Info')
    print('[4] Bank Conditions')
    print('[0] Exit Program')
    print(line)
    option = input('Select an option: ')
    continueProgram(option)

def continueAction():
    print('Type yes to go back')
    goBack = input('Go back? ')
    
    if(goBack == 'yes'):
        print('Return to option choise')
        printActionOptions()
    else:
        print('Exit program...')
        sys.exit()
    
def caseOption_1(option):
    if (option == '1'):
        eligibility = credit.isClientEligible()
        if (eligibility):
            levelOfIndebtness = float(clientData['needToBorrow']) / float(clientData['income']) * 100
            print(line)
            print(clientData['firstName'] + ' ' + clientData['lastName'] + ' is eligible with a level of indebtness of ' + "{0:.2f}".format(levelOfIndebtness) + " %")
            continueAction()

        else:
            print(line)
            print('Sorry, ' + clientData['firstName'] + ' ' + clientData['lastName'] + ' is not eligible!')
            continueAction()

def caseOption_2(option):
    if(option == '2'):
        loanPeriod = input('Client loan period should be (in months): ')
        credit.setLoanPeriod(loanPeriod)
        continueAction()

def caseOption_3(option):
    if(option == '3'):
        print(line)
        client.printClientInfo()
        print(line)
        continueAction()

def caseOption_4(option):
    if(option == '4'):
        print(line)
        credit.printBankConditions()
        print(line)
        continueAction()

def continueProgram(option):        
    if (option == '0'):
        print('Closing application...')
        print('Aplication closed.')
        sys.exit()
    else:
        caseOption_1(option)
        caseOption_2(option)
        caseOption_3(option)
        caseOption_4(option)


# Start the program
clientData = getClientData()

# create a new instace of the Client and Credit class
client = Client(clientData['firstName'], clientData['lastName'], clientData['age'], clientData['income'], clientData['needToBorrow'])
credit = Credit(clientData['income'], clientData['needToBorrow'])

printActionOptions()

# TODO Add a Method on Client class to update Client firstName
# TODO Add an Option to update Client firstName
# TODO Add a Method on Client class to update Client lastName
# TODO Add an Option to update Client lastName
# TODO Add a Method on Client class to update Client age
# TODO Add an Option to update Client age
# TODO Add an Option to update Client income
# TODO Add an Option to update Client need to borrow
# TODO Add a Method to Credit Class to calculate the credit details