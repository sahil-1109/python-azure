today = input("Which day is today?")
print(today)
if(today.isnumeric() == False):
    if(isinstance(today,str)):
        print('nice')
else:
   print('aww')