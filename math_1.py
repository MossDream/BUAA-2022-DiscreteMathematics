# 实现一个函数terms(s:str),返回输入的合式公式中s的主析取范式中合取式的数量
# 如terms('P and not Q or R')返回5
# 如terms('P or Q or R')返回7
# 如terms('P and Q and R')返回1
def terms(s:str):
    count = 0
    for P in [True, False]:
        for Q in [True, False]:
            for R in [True, False]:
               if eval(s):
                    count += 1
    return count