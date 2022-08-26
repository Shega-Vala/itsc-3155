
first = int(input("Please enter first number: ")) #promp msg for user to enter a number and store it
second = int(input("Please enter second number: "))#promp 2nd msg for user to enter a number and store it
result = ""
for i in range(first+1, second): #loop throug btw user input numbers
    if i%7==0 and i%5!=0:  # check if the numbers are divisible by 7 and not divisible by 5
        result += str(i)+","
result = result[:-1]
print(result) # prompt the result
