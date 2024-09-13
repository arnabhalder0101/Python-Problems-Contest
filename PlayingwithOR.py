# Your code here
N = int(input())
len_li = []
size_li = []
arr_list = []

for i in range(N):
    length, size = map(int, input().split())
    size_li.append(size)
    len_li.append(length)

    arr = list(int(j) for j in input().split())
    arr_list.append(arr)

for i in range(N):
    arr = arr_list[i]
    size = size_li[i]
    newList = []

    count = 0
    for j in range(len_li[i] - (size_li[i] - 1)):
        newList.append(arr[j:(size + j)])

    for k in range(len(newList)):
        v = 0
        for l in range(len(newList[k])):
            v |= newList[k][l]

        if (v % 2) != 0:
            count += 1

    print(count)
