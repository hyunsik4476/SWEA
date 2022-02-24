# T = int(input())
T = 10
for tc in range(1, T+1):
    N = int(input())    # 입력의 길이
    mid_calc = input()
    rare_calc = []
    op_stack = []
    for i in range(N):
        if '0' <= mid_calc[i] <= '9':
            rare_calc.append(mid_calc[i])

        elif mid_calc[i] == '(':
            op_stack.append(mid_calc[i])
        elif mid_calc[i] == '+':
            if op_stack:
                while op_stack and op_stack[-1] != '(':
                    rare_calc.append(op_stack.pop())
                op_stack.append(mid_calc[i])
            else:
                op_stack.append(mid_calc[i])
        elif mid_calc[i] == '*':
            if op_stack:
                while op_stack[-1] != '(' and op_stack[-1] != '+':
                    rare_calc.append(op_stack.pop())
                op_stack.append(mid_calc[i])
            else:
                op_stack.append(mid_calc[i])
        elif mid_calc[i] == ')':
            while op_stack and op_stack[-1] != '(':
                rare_calc.append(op_stack.pop())
            if op_stack:
                op_stack.pop()
        # print(op_stack)
        # print(rare_calc)
    while op_stack:
        tmp = op_stack.pop()
        if tmp != '(':
            rare_calc.append(tmp)

    # print(rare_calc)
    N = len(rare_calc)
    calc_stack = []
    for j in range(N):
        if '0' <= rare_calc[j] <= '9':
            calc_stack.append(rare_calc[j])
        elif rare_calc[j] == '+':
            a = calc_stack.pop()
            b = calc_stack.pop()
            calc_stack.append(int(a) + int(b))
        elif rare_calc[j] == '*':
            a = calc_stack.pop()
            b = calc_stack.pop()
            calc_stack.append(int(a) * int(b))
    print(f'#{tc} {calc_stack[0]}')