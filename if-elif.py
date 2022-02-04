answer = input("Would you like to continue? : ")
if answer == 'yes' or answer == 'y' or answer == 'Y' or answer == 'YES':
    print('Continuing....')
    print('Completed!') 
elif answer == 'NO' or answer == 'no' or answer == 'n':
    print('Exiting')
else: 
    print('Please try again and respond with yes or no.')