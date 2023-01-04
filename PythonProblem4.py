
# Problem 4--

list_ = []
index_ = []
'''creating a empy list of index, we gonna use it in future for extracting elements from list_(inside of for loop)'''

ask_element = int(input("Enter the number of elements in the list you want :"))

'''This for loop will add/fill index list'''
for r in range(ask_element):
    index_.append(r)

for i in range(ask_element):
    add_elements = int(input("Enter element :"))
    list_.append(add_elements)


print("The List :", list_)
for iteration, index in zip(list_, index_):
    """
    This while loop will allows you to stay at a iteration until it becomes a palindrome by the next else loop,
    when it becomes a palindrome it'll enter in the if loop and print and break the while loop. Same will be done for 
    other elements also.
    """
    while True:

        if str(iteration) == str(iteration)[::-1]:
            print(f"The number {iteration} is the next palindrome list element {list_[index]}.")

            '''With list[index] we extract elements with proper indexing'''
            break
        else:
            iteration += 1
