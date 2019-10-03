x = int(input("Select a number between 1 and 100: "))

for x in range (1,x+1):
    y = x % 3
    z= x % 5
    if y == 0 and z == 0:
        print ("fizzbuzz")
    elif y == 0:
        print ("fizz")
    elif z == 0:
        print ("buzz")
    else:
        print (x)