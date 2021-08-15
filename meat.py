def function():
    x = int(input("Enter a number from 1-9, 1 for Goat, 2 for Pig, 3 for Deer, 4 for Grizzly Bear, 5 for Leopard Seal, 6 for Cow, 7 for Moose, 8 for Bull, 9 for Bison: " ))
    y = int(input('Enter same number as before: '))
    lists = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = ['None','Goat', 'Pig', 'Deer', 'Grizzly Bear', 'Leopard Seal', 'Cow', 'Moose', 'Bull', 'Bison']
    return 'The ' + str(list2[y]) + ' is ' + str(lists[x] * 100) + ' pounds.'


print(function())