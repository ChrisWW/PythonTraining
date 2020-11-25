result = list(i for i in range(1, 101))
mylist =[]

for m in result:
    if m % 15 == 0:
        mylist.append(str("FizzBuzz"))
    elif m % 5 == 0:
        mylist.append(str("Buzz"))
    elif m % 3 == 0:
        mylist.append(str("Fizz"))
    else:
        mylist.append(str(m))

print(mylist)
