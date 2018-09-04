def merge():
    merge1count = 0
    merge2count = 0
    done = []
    while (merge1count < len(merge1)) and (merge2count < len(merge2)):
        if merge1[merge1count] < merge2[merge2count]:
            done.append(merge1[merge1count])
            merge1count = merge1count + 1
        else:
            done.append(merge2[merge2count])
            merge2count = merge2count + 1
    if merge1count == len(merge1):
        for x in range(((len(merge2)) - merge2count)):
            done.append(merge2[merge2count])
            merge2count = merge2count + 1
    if merge2count == len(merge2):
        for x in range(((len(merge1)) - merge1count)):
            done.append(merge1[merge1count])
            merge1count = merge1count + 1
    return done

numbers=input("Numbers").split()
for z in range (len(numbers)):
    numbers[z]=int(numbers[z])
merge_arr=[]
for z in range (len(numbers)):
    merge_arr.append([numbers[z]])
print(merge_arr)
while len(merge_arr) > 1:
    tomerge = len(merge_arr)
    if len(merge_arr) % 2 is not 0:
        tomerge=tomerge-1
    print(tomerge)
    y=0
    temp=[]
    while y < tomerge-1:
        merge1=merge_arr[y]
        merge2=merge_arr[y+1]
        done=merge()
        print(done)
        temp.append(done)
        y=y+2
    if tomerge is not len(merge_arr):
        temp.append(merge_arr[len(merge_arr)-1])
    merge_arr=temp
    print(merge_arr)
print(merge_arr)