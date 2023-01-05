# Problem - 8
# This is a program which will create a wrong table and also find out where is the mistake & what should be the right value

import random
Index = []


def notcorrect(number):
    """This function will generate a wrong table for given number"""

    update_num = 0
    faulty_table = []
    for i in range(10):
        update_num = number * (i+1)
        faulty_table.append(update_num)

    '''Getting a random index fot poping a number from table and insert a wrong value.'''
    random_index = random.randint(2, 8)
    faulty_table.pop(random_index)
    '''Insert a number as per following logic -- It'll add either 1,2 or 3 in that correct number
    And will make it a faulty table.'''
    faulty_table.insert(random_index, (number * (random_index + 1)) + random.randint(1, 4))

    return faulty_table


def iscorrect(table, number):
    for i in range(len(table)):
        Index.append(i)
    ''' This below for loop will check the indexed number in the table is a divisor or not, for that proper index'''
    for item, indexing in zip(table, Index):
        if table[indexing] / number == (indexing + 1):
            pass
        else:
            print(f">>>Error found !! at {indexing + 1}th place. Error is {item} ")
            print(f">>>The correct number will be, {number}x{indexing+1} = {number*(indexing+1)}\n")


ask_num = int(input("Enter number to get faulty Table :"))

'''Calling pre-defined functions --'''

wrong_table = notcorrect(ask_num)
print("\nThe wrong table -", wrong_table, "\n")

iscorrect(wrong_table, ask_num)
