#This programsays Hello and asks for my name

print ('Hello')
print ('Type your name: ') #ask  for their name

myName = input()
print('It is a pleasure to meet you' + ' ' + myName)
print('The lenght of your name is: ')
print(len(myName))#Print the lenght of the string myName len() Prints the lenght of a string
print('What is your age')#ask for their age
myAge= input()
print('You will be ' + str(int(myAge)+1)+ ' in a year')#int() converts myAge to int data, str() converts all the values in brackets to a string
