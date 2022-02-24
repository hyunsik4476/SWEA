T = 10

for tc in range(1, T+1):
    N = int(input())
    infix = input()
    postfix = []
    stack = []
    isp = {'(': 0, '+': 1, '*': 2}
    osp = {'(': 3, '+': 1, '*': 2, ')': 1}

    for i in range(N):
        if '0' <= infix[i] <= '9':
            postfix.append(infix[i])
        elif infix[i] == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            if stack:
                while stack and osp[infix[i]] <= isp[stack[-1]]:   # 2 1. 1 2
                    postfix.append(stack.pop())
            stack.append((infix[i]))

    while stack:
        postfix.append(stack.pop())

    N = len(postfix)
    calc_stack = []
    for j in range(N):
        if '0' <= postfix[j] <= '9':
            calc_stack.append(postfix[j])
        elif postfix[j] == '+':
            a = calc_stack.pop()
            b = calc_stack.pop()
            calc_stack.append(int(a) + int(b))
        elif postfix[j] == '*':
            a = calc_stack.pop()
            b = calc_stack.pop()
            calc_stack.append(int(a) * int(b))
    print(f'#{tc} {calc_stack[0]}')