numbers=input("Numbers").split()
for z in range (len(numbers)):
    numbers[z]=int(numbers[z])
y=0
while y == 0:
    y=1
    for x in range (len(numbers)-1):
        print(numbers)
        if numbers[x] > numbers[x+1]:
            numbers[x], numbers[x+1] = numbers[x+1], numbers[x]
            y=0
