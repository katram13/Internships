#KATYA RAMSINGH#

#REMINDERS:
#At the end of the program, the program must print a statement with:
#-a rough chart of the set up modeled on the one from slide 16
#-all of the solo option profit amounts
#-the balanced amount and the amount of each variable included
#-a final conclusion stating the best option and its profit.


import numpy as np
def main():
    variable = int(input("Please enter the number of variables: "))
    coefficients = list(map(float,input("Enter the coefficients of each variable for the objective function; separate each value by a space (for example: 3000 2000 2000): ").split()))
    print("Coefficients: ", coefficients)
    A = input("Enter the data for the square matrix stating the constraints. Separate each row with a semicolon: ")
    A = [list(map(float, row.split())) for row in A.split(';')]
    print("Maxtrix: ", A)
    b = list(map(float,input("Enter the constraint limits; separate each value by a space (for example: 3000 2000 2000): ").split()))
    
    def print_data(A,b, coefficients):
        print("'CONSTRAINTS' 'AVAILABLE'")
        for i in range(variable):
            print(A[i],b[i])
        print("'COEFFICIENTS' ", coefficients)       

    print_data(A,b, coefficients)

    def calc_solo(A,b):
        Ratios = []
        for k in range(variable):
            Ratio_row = []
            for j in range(variable):
                ratio = b[j]/A[j][k]
                Ratio_row.append(ratio)
            Ratios.append(Ratio_row)
        print("Ratios before sort: ", Ratios)
        for row in Ratios:
            row.sort()
        print("Ratios after sort: ", Ratios)
        return Ratios

    Ratios = calc_solo(A,b)

    def variable_only(A, b, coefficients, Ratios):
        for i in range(variable):
            profit = Ratios[i][0] * coefficients[i]
            print(f"This is the profit for variable {i + 1}: $", profit)

    variable_only(A, b, coefficients, Ratios)

    #computing the linear equation system Ax = b
    def balanced_ans(A, b, coefficients):
        A = np.array(A)
        inv_A = np.linalg.inv(A)
        b = np.array(b)
        x = np.linalg.inv(A).dot(b)
        balanced_profit = np.dot(coefficients, x)
        print("The solution of Ax = b is: ", x)
        print("The best possile balanced profit is: $", balanced_profit)
    balanced_ans(A, b, coefficients)
        

main()


##OUTPUT##
#Please enter the number of variables: 2
#Enter the coefficients of each variable for the objective function; separate each value by a space (for example: 3000 2000 2000): 50 40
#Coefficients:  [50.0, 40.0]
#Enter the data for the square matrix stating the constraints. Separate each row with a semicolon: 1 1.5;2 1
#Maxtrix:  [[1.0, 1.5], [2.0, 1.0]]
#Enter the constraint limits; separate each value by a space (for example: 3000 2000 2000): 750 1000

##ROUGH TABLE##
#'CONSTRAINTS' 'AVAILABLE'
#[1.0, 1.5] 750.0
#[2.0, 1.0] 1000.0
#'COEFFICIENTS'  [50.0, 40.0]

#Ratios before sort:  [[750.0, 500.0], [500.0, 1000.0]]
#Ratios after sort:  [[500.0, 750.0], [500.0, 1000.0]]
#This is the profit for variable 1:  $25000.0
#This is the profit for variable 2:  $20000.0
#The solution of Ax = b is:  [300. 200.]
#The best possible balanced profit is:  $23000.0

    
