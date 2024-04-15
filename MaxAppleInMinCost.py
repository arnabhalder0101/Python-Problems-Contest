"""
QUESTION:

Maximum apples at min cost
Time Limit: 2, Memory Limit: 256000
At some store, the price of one apple is 'a' rupees, but there's a special offer where you can buy two apples for 'b' rupees.

Maxim needs to buy exactly n apples. When purchasing two apples, he has the choice to buy them at the regular price or take advantage of the promotion.

What is the minimum amount of rupees Maxim should spend to buy n apples?

Input
Input consists of 3 integers - n, a, b.

Output
Print the minimum cost of buying n apples.
"""
# Your code here
inp = input().split()
intList = [int(i) for i in inp]
n = intList[0]
a= intList[1]
b = intList[2]

if a*2>b:
    cost = (n//2)*b+ (n%2)*a
    print(cost)
else:
    cost = n*a
    print(cost)
