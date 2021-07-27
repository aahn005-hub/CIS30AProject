text_file = open('Tracker.txt', 'w')

class Tracker():        #defined a class called Tracker to describe income and budget
    expenses = []
    
    def userBudget(self):
        self.income = int(input('What is your monthly income?: '))
        self.budget = int(input('What is your monthly budget?: '))
        self.saving = int(input('What is your saving goals?: '))
        
    def print(self):
        if self.income < self.budget:
            print('ERROR, budget cannot be bigger than income.')
        else:
            print('\nIncome:', self.income)
            print('Budget:', self.budget)
            print('Saving goals:', self.saving)
            
    def Expenses(self):             #make a list of expenses.
        num = int(input('\nHow many expenses do you have?: '))
        self.addExpenses(num)

    def addExpenses(self,num):      #inputs costs of expenses
        for i in range(num):
            expense = int(input('\nInput costs of all your expenses (Input each cost and then press enter): '))
            self.expenses.append(expense)

    def total(self):                #outputs user's starting income, budget, saving goal, and total expense     
        self.subtotal = sum(self.expenses)
        self.netIncome = self.income - self.budget
        print('\n-------------------------------')
        print('Income: ' ,self.income)
        print('Budget: ', self.budget)
        print('Saving goal', self.saving)
        print('Total Expense Cost:',self.subtotal)
        self.subtotal = sum(self.expenses)
        self.netBudget = self.budget - self.subtotal
        if self.budget < self.subtotal:                 #determines if expense surpasses budget
            print('\n-------------------------------')
            print('EXPENSES HAS SURPASSED BUDGET')
        else:
            print('\n-------------------------------')
            print('Budget is now:', self.netBudget)

        self.netTotal = self.netIncome + self.netBudget
        print('Leftover Income: ', self.netTotal)
        if self.netTotal >= self.saving:               #determines if saving goals were achieved. 
            print('You achieved your saving goals!')
        else:
            print('You have not achieved your saving goals. Start saving!')
       
    def textFile(self):                #outputs user's starting income, budget, saving goal, and total expense     
        self.subtotal = sum(self.expenses)
        self.netIncome = self.income - self.budget
        text_file.write('-------------------------------')
        text_file.write('\nIncome: ' +str(self.income))
        text_file.write('\nBudget: '+ str(self.budget))
        text_file.write('\nSaving goal: '+ str(self.saving))
        text_file.write('\nTotal Expense Cost: '+str(self.subtotal))
        self.subtotal = sum(self.expenses)
        self.netBudget = self.budget - self.subtotal
        if self.budget < self.subtotal:                 #determines if expense surpasses budget
            text_file.write('\n-------------------------------')
            text_file.write('\nEXPENSES HAS SURPASSED BUDGET')
        else:
            text_file.write('\n-------------------------------')
            text_file.write('\nBudget is now: '+ str(self.netBudget))

        self.netTotal = self.netIncome + self.netBudget
        text_file.write('\nLeftover Income: '+ str(self.netTotal))

        if self.netBudget >= self.saving:               #determines if saving goals were achieved. 
            text_file.write('\nYou achieved your saving goals!')
        else:
            text_file.write('\nYou have not achieved your saving goals. Start saving!')


choosing = 'Y'
while choosing == 'Y':  #allows user to modify any inputs after displaying tracker
    user = Tracker()
    user.userBudget()
    user.Expenses()
    user.total()
    user.textFile()
    
    choosing = input('\nRemodify inputs? (Y for yes, N for no: )').upper()
    
text_file.close()    



