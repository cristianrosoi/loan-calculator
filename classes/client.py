class Client:
    # Initialize the Client class
    # with the client information
    # @param firstName: string    
    # @param lastName: string    
    # @param age: string    
    # @param income: string    
    # @param needToBorrow: string    
    def __init__(self, firstName, lastName, age, income, needToBorrow):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.income = income
        self.needToBorrow = needToBorrow
    
    # Method to print all information
    # related to that Client
    def printClientInfo(self):
        print('Name: ' + self.firstName + ' ' + self.lastName)
        print('Age: ' + self.age)
        print('Income: ' + self.income)
        print('Need to borrow: ' + self.needToBorrow)

    # Method to update the Client Income
    # if for example the Client income will change
    # over time
    # @param newIncome: String
    def updateIncome(self, newIncome):
        self.income = newIncome
    
    # Method to update the Client needToBorrow
    # if the Client need will change
    # over time
    # @param newAmountToBorrow: String
    def updateBorrowNeed(self, newAmountToBorrow):
        self.needToBorrow = newAmountToBorrow


     