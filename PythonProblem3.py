input1 = int(input("Enter number of elements you want in list :"))
list_ = []


def reverse_Lists():
    return_list = list_.copy()
    '''This return_list is initially a copy of main list_, but we'll change the elements with logic mentioned below -'''
    length = len(list_)
    '''
    This function will reverse 1st & last and 2nd and 2nd last and so on...
    The numbers of elements in list is odd or even doesn't matter.
    * if It's even then all elements will be reversed
    * if it's odd then all elements except middle one will be reversed.
    So, this function will be useful for all lists.
    {NB: No need to do anything with the middle element of the list.}
    '''
    for iteration in range(int((length - 1)/2)):

        # talking element from list --
        start_element = list_[iteration]
        last_element = list_[length - (iteration+1)]

        # updating the return_list --
        '''That return list, which was initially a copy that will be modified with logic mentioned below --'''
        return_list[iteration] = last_element
        return_list[length - (iteration+1)] = start_element

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

# Method 3 --
print("Method 3 :", reverse_Lists())
