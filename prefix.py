

def operation(op, a, b):
    op_to_func = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    if op not in op_to_func:
        return -1

    return op_to_func[op](a, b)

if __name__ == '__main__':
    print(
        operation('+', 5, 4)
    )
