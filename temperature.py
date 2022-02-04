farhenieit = input('WHat is the temperature in Farhenieit?: ')
if farhenieit.isnumeric() == False :
    print('Value is not an number')
    exit()

farhenieit = int(farhenieit)

celsius =int((farhenieit - 32) * 5/9)
print('The temperature in celsius is: ' + str(celsius))