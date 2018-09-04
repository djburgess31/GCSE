#insertion=input("numbers").split()
#for z in range (len(insertion)):
#    insertion[z]=int(insertion[z])
insertion = [6, 4, 5, 7, 3, 8, 3]
place=0
while place < len(insertion)-1:
    if insertion[place] > insertion[place+1]:
        insertion[place], insertion[place+1] = insertion[place+1], insertion[place]
    y=place
    while insertion[y] < insertion[y-1]:
        insertion[y], insertion[y-1] = insertion[y-1], insertion[y]
        y=y-1
    place=place+1
print(insertion)

