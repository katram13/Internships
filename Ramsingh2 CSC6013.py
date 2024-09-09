#class Person from lecture
class Person:
    def __init__(self, nickname, name, familyName, age):
        self.nickname = nickname
        self.name = name
        self.famN = familyName
        self.age = age
    def getNickname(self):
        return self.nickname
    def getName(self):
        return self.name
    def getFullName(self):
        return self.name+" "+self.famN
    def getFamilyName(self):
        return self.famN
    def getAge(self):
        return self.age

def main():
    #creating the stack
    s = []
    
    #opening the file
    with open("people.csv", "r") as text:
        #created for loop so we can append info to stack
        for people in text:
            s.append(people.strip())
            
    #printing stack for visibility
    print(s)

    #starting while loop to repeatedly ask the user for int numbers 1 - 4
    while True:
        x = int(input("Please choose a number from 1 - 4: "))

        if len(s) < x:
            print("The number you entered is too large.")
            print("This is the length of the stack: ", len(s))
            if len(s) == 0:
                break
            
        elif len(s) >= x:
            
            #starting if statements
            if x == 1:
                if s:
                    s.pop()#popping 1 time since user entered 1
                    if s:
                        print(s[len(s)-1])#printing index 0 from stack for who is left at the top of stack
                    else:
                        print("The stack is empty.")
                else:
                    print("The stack is empty.")
            #do i start using elifs here?
            elif x == 2:
                if s:
                    s.pop()#popping twice
                    s.pop()
                    if s:
                        print(s[len(s)-1])
                    else:
                        print("The stack is empty.")
                else:
                    print("The stack is empty.")

            elif x == 3:
                if s:
                    s.pop()#popping 3 times
                    s.pop()
                    s.pop()
                    if s:            
                        print(s[len(s)-1])
                    else:
                        print("The stack is empty.")
                else:
                    print("The stack is empty.")

            elif x == 4:
                if s:
                    s.pop()#popping 4 times
                    s.pop()
                    s.pop()
                    s.pop()
                    if s:
                        print(s[len(s)-1])
                    else:
                        print("The stack is empty.")
                else:
                    print("The stack is empty.")
                
        #to tell user to pick another number
        else:
            print("You did not choose a number from 1 - 4.")

main()
