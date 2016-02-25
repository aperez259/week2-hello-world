#Adam Perez

print('Hello world!')

print("Choose a language and I'll greet you in that language!")

print(' 1. Portuguese') # Shows the user if he tthe messagey will be in portuguese
print(' 2. Spanish') # Shows the user if he tthe messagey will be in spanish
print(' 3. French') # Shows the user if he tthe messagey will be in french

Language = input('')
if Language == '1': # if you type 1, you will receive a greeting in portuguese 
    print('Oi, mundo!')
if Language == '2': # if you type 2, you will receive this message in spanish
    print('Hola mundo!')
if Language == '3': # if you type 3, you will receive this message in french
    print ('Bonjour le monde')
elif Language > "3":
    print ('You did not enter a valid selection') # If you choose a number higher than 3, you will get this message, saying you didnt enter a valid selection
elif Language < '1':
    print ('You did not enter a valid selection') #if you choose a number less than 1, you will get this message, saying you didnt enter a valid selection
