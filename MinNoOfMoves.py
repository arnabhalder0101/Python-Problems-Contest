"""Minimum number of moves
Time Limit: 2, Memory Limit: 256000
You are standing on 0 on a number line. Your task is to reach N using a minimum number of moves. In one move you can take 2 or 3 steps left or right from the current position.
Input
The first line of the input contains an integer N.

Constraints
1 ≤ N ≤ 109
Output
Print the minimum number of moves required to reach N."""

def moves_to_N(Num):
    if Num == 1:
        return 2

    elif Num % 3 == 0:
        return Num // 3

    # elif Num % 5 == 0:
    #     return Num // 5 * 2

    elif Num % 2 == 0 and Num // 2 <= 2:
        return Num // 2

    else:
        i = 0
        while Num % 3 != 0:
            i += 1
            Num -= 1

        # m = moves_to_N(Num)
        if i == 1:
            return Num // 3 + 1
        elif i == 2:
            return moves_to_N(Num) + 1

inp = int(input())
print(moves_to_N(inp))
