input1 = int(input("Enter number of elements you want in list :"))
list_ = []


def reverse_Lists():
    """
    Creating a return_list of 'anything', cause with blank list we're going to face indexing errors during inserting
    elements in return list. We'll change this list with 'pop' and 'insert' method.
    """
    return_list = ["anything"] * input1
    length = len(list_)

    for iteration in range(int((length - 1)/2)):
        start_element = list_[iteration]
        last_element = list_[length - (iteration+1)]
        '''Remove element with pop and insert updated element at that place with insert--'''
        return_list.pop(iteration)
        return_list.insert(iteration, last_element)
        return_list.pop(length - (iteration + 1))
        return_list.insert(length-(iteration+1), start_element)

    return_list.pop(int((length-1)/2))
    return_list.insert(int((length-1)/2), list_[int((length-1)/2)])
    return return_list


for i in range(input1):
    number_ = input(f"Enter {i}th element :")
    list_.append(number_)


print("Main List :", list_)

list_swap1 = list_[::-1]
print("Method 1 :", list_swap1)

# reverse function directly modifies the main list, so we made a new list and then changed that.
new_list = list_.copy()
new_list.reverse()
print("Method 2 :", new_list)
# this is the modified new list... if we worked with main list then we can't able to work further with that list.

# method 3 --
print("Method 3 :", reverse_Lists())
