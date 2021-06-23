from __future__ import division

OPERATORS = set(['+', '-', '*', '/', '^', '(', ')'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# INFIX ===> POSTFIX
'''
1)Fix a priority level for each operator. For example, from high to low:
    3.    - (unary negation)
    2.    * /
    1.    + - (subtraction)
2) If the token is an operand, do not stack it. Pass it to the output.
3) If token is an operator or parenthesis:
    3.1) if it is '(', pusha
    3.2) if it is ')', pop until '('
    3.3) push the incoming operator if its priority > top operator; otherwise pop.
    *The popped stack elements will be written to output.
4) Pop the remainder of the stack and write to the output (except left parenthesis)
'''


def infix_to_postfix(formula):
    stack = []  # only pop when the coming op has priority
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[
                stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # left over
    while stack: output += stack.pop()
    print(output)
    return output


# INFIX ===> PREFIX

def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.pop()  # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[
                op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.append(ch)

    # left over
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append(op + b + a)
    print(exp_stack[-1])
    return exp_stack[-1]


'''
Scan the formula:
1) When the token is an operand, push into stack;
2) When an operator is encountered:
    2.1) If the operator is binary, then pop the stack twice
    2.2) If the operator is unary (e.g. unary minus), pop once
3) Perform the indicated operation on two poped numbers, and push the result back
4) The final result is the stack top.
'''


def evaluate_postfix(formula):
    stack = []
    for ch in formula:
        if ch not in OPERATORS:
            stack.append(float(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            c = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}[ch]
            stack.append(c)
    print(stack[-1])
    return stack[-1]


def evaluate_infix(formula):
    return evaluate_postfix(infix_to_postfix(formula))


'''
Whenever we see an operator following by two numbers,
we can compute the result.
'''


def evaluate_prefix(formula):
    exps = list(formula)
    while len(exps) > 1:
        for i in range(len(exps) - 2):
            if exps[i] in OPERATORS:
                if not exps[i + 1] in OPERATORS and not exps[
                                                            i + 2] in OPERATORS:
                    op, a, b = exps[i:i + 3]
                    a, b = map(float, [a, b])
                    c = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}[op]
                    exps = exps[:i] + [c] + exps[i + 3:]
                    break
        print(exps)
    return exps[-1]


def menu():
    print('\n#######################################################')
    print(' Infix To Postfix and Prefix conversion and evaluation')
    print(' Just Input your String Correctly ')
    print(' If you got any error please frist check your input')
    print('#######################################################')
    print('(1) Infix to Postfix')
    print('(2) Infix to Prefix')
    print('(3) Evaluate Infix')
    print('(4) Evaluate Postfix')
    print('(5) Evaluate Prefix')
    opt = input('Enter Option (1/2/3/4/5/6/7):\n ')
    if opt in ('1', '2', '3', '4', '5', '6', '7',):
        if (opt == '1'):
            what = input('\nEnter Infix String: ')
            print('Postfix String: ')
            infix_to_postfix(what)
        if (opt == '2'):
            what = input('\nEnter Infix String: ')
            print('Prefix String: ')
            infix_to_prefix(what)
        if (opt == '3'):
            what = input('\nEnter Infix String: ')
            print('Evaluate Infix is: ')
            evaluate_infix(what)
        if (opt == '4'):
            what = input('\nEnter Postfix String: ')
            print('Evaluate Postfix is: ')
            evaluate_postfix(what)
        if (opt == '5'):
            what = input('\nEnter Prefix String: ')
            print('Evaluate Prefix is: ')
            evaluate_prefix(what)


if __name__ == "__main__":
    menu()
