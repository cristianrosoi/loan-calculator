from classes.bankConditions import BankConditions

class Credit(BankConditions):
    # Initialize the Credit class
    # and extending the BankConditions Class
    # meaning BankConditions methods will be available
    # in the Credit class as well
    # with the client information
    # @param Client: Dictionary
    def __init__(self, income, needToBorrow):
        self.income = income
        self.needToBorrow = needToBorrow

    def printInfo(self):
        print('Income: ' + self.income)
        print('Need to borrow: ' + self.needToBorrow)

    def isClientEligible(self):
        return float(self.needToBorrow) / float(self.income) <= self.loanEligibilityLevel 
    
    def setLoanPeriod(self, loanPeriod):
        self.loanPeriod = loanPeriod 
