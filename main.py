import sys
from stack import Stack


def in2post(expr):
    if not isinstance(expr, str):
        raise ValueError("Input expression must be a string")

    # Remove any whitespace from the expression
    expr = expr.replace(" ", "")

    # Check if the expression is empty
    if len(expr) == 0:
        raise SyntaxError("Empty expression")

    # Initialize an empty stack and an empty output list
    stack = Stack()
    output = []

    # Operator precedence dictionary
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    # Process each character in the expression
    for char in expr:
        # If the character is an operand, append it to the output list
        if char.isalnum():
            output.append(char)
        # If the character is an opening parenthesis, push it onto the stack
        elif char == "(":
            stack.push(char)
        # If the character is a closing parenthesis, pop operators from the stack and append them to the output list
        # until an opening parenthesis is encountered
        elif char == ")":
            while not stack.is_empty() and stack.top() != "(":
                output.append(stack.pop())
            if stack.is_empty():
                raise SyntaxError("Mismatched parentheses")
            stack.pop()  # Discard the opening parenthesis
        # If the character is an operator, pop operators from the stack and append them to the output list
        # until an operator with lower precedence or an opening parenthesis is encountered
        elif char in precedence:
            while not stack.is_empty() and stack.top() != "(" and precedence[char] <= precedence.get(stack.top(), 0):
                output.append(stack.pop())
            stack.push(char)
        else:
            raise SyntaxError("Invalid character: " + char)

    # Pop any remaining operators from the stack and append them to the output list
    while not stack.is_empty():
        if stack.top() == "(":
            raise SyntaxError("Mismatched parentheses")
        output.append(stack.pop())

    # Return the postfix expression as a string
    return "".join(output)


def eval_postfix(expr):
    if not isinstance(expr, str):
        raise ValueError("Input expression must be a string")

    # Initialize an empty stack
    stack = Stack()

    # Process each character in the expression
    for char in expr:
        # If the character is an operand, push it onto the stack
        if char.isdigit():
            stack.push(int(char))
        # If the character is an operator, pop two operands from the stack,
        # perform the operation, and push the result back onto the stack
        elif char in "+-*/^":
            if stack.size() < 2:
                raise SyntaxError("Insufficient operands")
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, char)
            stack.push(result)
        else:
            raise SyntaxError("Invalid character: " + char)

    # After processing all characters, the stack should contain the final result
    if stack.size() == 1:
        return stack.pop()
    else:
        raise SyntaxError("Invalid expression")


def perform_operation(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "^":
        return operand1 ** operand2
    else:
        raise SyntaxError("Invalid operator: " + operator)


def main():
    
    # Open the input file
    with open("data.txt", "r") as input_file:
        expressions = input_file.readlines()
    # Open the output file
    with open("output.txt", "w") as output_file:
        for expr in expressions:
            expr = expr.strip()

            # Display the infix expression
            print("infix:", expr)

            try:
                # Convert infix to postfix
                postfix_expr = in2post(expr)

                # Print the postfix expression
                print("postfix:", postfix_expr)

                # Evaluate the postfix expression
                result = eval_postfix(postfix_expr)

                # Print the result
                print("answer:", float(result),"\n")

            except ValueError as ve:
                print("ValueError:", str(ve))
            except SyntaxError as se:
                print("SyntaxError:", str(se))



    
if __name__ == "__main__":
    # Open the input file
    with open("output.txt", "r") as out_file:
        expressions = out_file.readlines()
        for i in expressions:
            print(i)
    # Open the output file

    with open("output.txt", "w") as file:
        # Redirect the standard output to the output file
        # sys.stdout = file
    
        
        # Call the main function
        main()
