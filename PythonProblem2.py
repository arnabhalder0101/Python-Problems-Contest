
n = input("Enter the main number :")
mn = int(input("Enter the minimum number of the range :"))
mx = int(input("Enter the maximum number of the range :"))


'''
if Remainder is 0 then that number is a divisor,
if remainder is not 0 then it's not a divisor of that number.
'''


def get_divisor(number, number2):
    if int(number) % int(number2) == 0:
        output = 'divisor'
        return output

    elif int(number) % int(number2) != 0:
        output1 = 'not divisor'
        return output1


if mn == mx:
    print("It's not a range")
    print(f'By the way, {mn} is {get_divisor(n, mn)} of {n}')
elif mn < mx:
    for i in range(mn, mx+1):
        print(f'{i} is {get_divisor(n, i)} of {n}')
elif mn > mx:
    print("Wrong Inputs !!")

