#输入仅可能由P、Q、and、or、not、空格组成，且不含其他字符的合式公式字符串
#有且仅有一个合式公式为真，若s1为真，返回1；若s2为真，返回2；若无法确定，返回0
def truth(s1:str,s2:str):
    for P in [0,1]:
        for Q in [0,1]:
            if eval(s1)==1:
                if eval(s2)==1:
                    return 2
            if eval(s2)==1:
                if eval(s1)==1:
                    return 1    
    return 0
#这是一些已通过的测试样例
def main():
    s1= 'P and Q'
    s2= 'not Q'
    print(truth(s1,s2))
    s2= 'not Q'
    print(truth(s1,s2))
if __name__ == "__main__":
    main()    