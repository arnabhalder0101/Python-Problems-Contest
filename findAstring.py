
def count_substring(string, sub_string):
    count = 0
    l = []
    length_sub = len(sub_string)
    for i in range(len(string) - 2):
        l.append(string[i:(i + length_sub)])
    for j in range(len(l)):
        if sub_string == l[j]:
            count += 1
    print(l)
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

