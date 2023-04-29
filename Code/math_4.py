#输入合式公式s1，判断s1，P是否能推出Q，若能，返回True；若不能，返回False
#s1为合式公式，且仅由P、Q、and、or、not、空格组成，且不含其他字符
def func(s1:str):
    for P in [0,1]:
        for Q in [0,1]:
            if eval(s1)==1 and eval('P')==1:
                if Q==0:
                    return False
    return True
def main():
    print(func('P and Q'))
    print(func('P or Q'))
    print(func('Q'))

if __name__ == "__main__":
    main()
