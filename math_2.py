#以下代码段实现用真值表验证两个最多含有三个命题变元的合式公式pre、s是否满足：pre能推出s
def isargument3(pre, s):
    w = 'P Q R '
    for u in pre:
        w = w + u + ''
    w = w + '|=' + s
    print(w)
    truth = {1, 0}
    for P in truth:
        for Q in truth:
            for R in truth:
                pv = []
                for pk in pre:
                    pv = pv + [int(eval(pk))]
                f = int(eval(s))
                t = [P, Q, R] + pv + [f]
                for num in t:
                    print(num, end='')
                    print(' ', end='')
                print('\n', end='')
    return


pre = ['P ', '(not Q) or ((not P) or R) ']
s = '(not Q) or R'
isargument3(pre, s)