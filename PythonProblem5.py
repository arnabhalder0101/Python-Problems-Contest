# Palindrome finder --
# if the number is less than 10, it's not eligible for getting next palindrome.
# if the number is greater than 10 then print next palindrome.

print("\t\t\t-- What is the next Palindrome --\n")
print("If the number is less than 10, it's not eligible for getting next palindrome.")
print("If the number is greater than 10 then print next palindrome.\n")

list_ = []
index_ = []
ask = int(input("Enter how many elements you want in your list :"))

for r in range(ask):
    index_.append(r)

for i in range(ask):
    ask_elements = int(input(f"Enter element {i+1} :"))
    list_.append(ask_elements)

for iteration, index in zip(list_, index_):

    while True:
        if iteration < 10:
            print(f"This list element {iteration} is less than 10. Not eligible for getting next palindrome.")
            break

        elif str(iteration) == str(iteration)[::-1]:
            print(f"The number {iteration} is the next palindrome of {list_[index]}.")
            break

        else:
            iteration += 1
