#Write your code below this line 👇\
#Get name
string = input("What is your name? ")
#Count number of characters minus spaces
print("Number of characters => " + str(len(string) - string.count(' ')))

#Instructor solution
# print(len(input("What is your name?")))