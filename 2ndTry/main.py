from stack import Stack

def precedence(operator):
    precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedence_dict.get(operator, 0)

def in2post(expr):
    if not isinstance(expr, str):
        raise ValueError("Input must be a string")

    stack = Stack()
    postfix = []
    tokens = expr.split()

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.top() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove the '('
        else:
            while not stack.is_empty() and precedence(stack.top()) >= precedence(token):
                postfix.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)

def eval_postfix(expr):
    stack = Stack()
    tokens = expr.split()

    for token in tokens:
        if token.isdigit():
            stack.push(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 / operand2)

    return stack.pop()

def main():
    with open('data.txt', 'r') as file:
        for line in file:
            infix_expr = line.strip()
            print(f"infix: {infix_expr}")
            try:
                postfix_expr = in2post(infix_expr)
                print(f"postfix: {postfix_expr}")
                result = eval_postfix(postfix_expr)
                print(f"answer: {result:.1f}\n")
            except (SyntaxError, ValueError):
                print("Invalid expression\n")

if __name__ == "__main__":
    main()
