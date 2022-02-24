T = int(input())

for tc in range(1, T+1):
    lst = list(input().split())
    N = len(lst)
    stack = []

    for alp in lst:
        if '0' <= alp <= '9':
            stack.append(alp)
        elif alp == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack[0]}')
            else:
                print(f'#{tc} error')
        else:
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                c = b + alp + a
                stack.append(str(eval(c)))
            else:
                print(f'#{tc} error')
                break
