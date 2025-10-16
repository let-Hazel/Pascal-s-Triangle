
    # two astericks makes the power of
    # (a + b)**row_num
    # a = 1
    # b = 1

    # c = (a+b)**row_num
    # return c
    # triangle = []

    # first = [0]
    # last = [0]
    
    # return [1]

    # for i in range(1, rows + 1):
    #     spaces = " " * (rows - i)
    #     asterisks = "*" * (2 * i - 1)
    #     print(spaces + asterisks)
    # formula = (n -1 k - 1) + (n - 1 k)

def factorial(n):
    fact = 1

    try:
        n = int(n)
    except:
        raise ValueError("n not an integer")
    
    for i in range(1, n+1):
        if n < 0:
            return "input positive number"
        if n == 0:
            return 1
        else:
            fact *= i
    return fact


def generate_row(row_num, row_pos):
    """Generate a single row of Pascal's Triangle"""
    return factorial(row_num) // (factorial(row_pos) * factorial(row_num - row_pos))

def print_centered_triangle(rows):
    for n in range(rows):
        print(" " * (rows - n), end="")
        for k in range(n + 1):
            print(generate_row(n, k), end=" ")
        print()



# Example usage:
print_centered_triangle(5)
