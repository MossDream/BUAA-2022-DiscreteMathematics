import numpy as np

def Produce(m, n):
    """
    随机生成符合条件的合式公式

    参数:
    - m: 变元数量
    - n: 公式复杂度

    返回值:
    - formula: 生成的合式公式字符串列表
    """

    # 定义联结词集合
    connectives = ['¬', '∧', '∨', '→', '↔', '⨁']
    # 定义变元集合
    all_values=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U' ,'V','W','X','Y','Z']
    # 随机生成变元集合
    values=[]
    cnt=m
    while(cnt>0):
        rand=np.random.randint(len(all_values))
        if(all_values[rand] not in values):
            values.append(all_values[rand])
            cnt-=1
    # 递归生成公式
    def generate_sub_formula(depth):
        if depth == 0:
            return values[np.random.randint(m)]
        
        connective = np.random.choice(connectives)
        if connective == '¬':
            sub_formula = generate_sub_formula(depth-1)
            return connective + sub_formula
        else:
            sub_formula1 = generate_sub_formula(depth-1)
            sub_formula2 = generate_sub_formula(depth-1)
            return '(' + sub_formula1 + ' ' + connective + ' ' + sub_formula2 + ')'

    result = list(generate_sub_formula(n))
    return result

def TrueOrNot(formula): 
    """
    判断合式公式的真值

    参数:
    - formula: 合式公式字符串

    返回值:
    - 0: 公式为永真式
    - 1: 公式为永假式
    - 2: 公式为可满足式
    """
    def to_reverse_polish(formula: str) -> list[str]:
        """
        将中缀表达式转换为逆波兰表达式
        
        参数:
        - formula: 中缀表达式字符串
         
        返回值:
        - output: 逆波兰表达式列表
        """
        #去除空格
        formula = formula.replace(' ', '')
        # 操作符栈
        stack = []
        # 逆波兰表达式结果
        output = []
        # 操作符优先级字典
        precedence = {
        '¬': 3,
        '∧': 2,
        '∨': 1,
        '→': 0,
        '↔': 0,
        '⨁': 0,
    }

        for token in formula:
            if token.isalpha():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif token in precedence:
                while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                    output.append(stack.pop())
                stack.append(token)
            else:
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output
    
    def evaluate_reverse_polish(expression: list[str], values: dict[str, bool]) -> bool:
        """
        计算逆波兰表达式的真值

        参数:
        - expression: 逆波兰表达式列表
        - values: 变元真值字典
        
        返回值:
        - result: 逆波兰表达式的真值
        """
        stack = []

        for token in expression:
            if token.isalpha():
                stack.append(values[token])
            elif token == '¬':
                stack.append(not stack.pop())
            elif token == '∧':
                right = stack.pop()
                left = stack.pop()
                stack.append(left and right)
            elif token == '∨':
                right = stack.pop()
                left = stack.pop()
                stack.append(left or right)
            elif token == '→':
                right = stack.pop()
                left = stack.pop()
                stack.append(not left or right)
            elif token == '↔':
                right = stack.pop()
                left = stack.pop()
                stack.append(left == right)
            elif token == '⨁':
                right = stack.pop()
                left = stack.pop()
                stack.append(left != right)

        return stack.pop()
    
    # 读取并构建变元集合
    variables = set()
    for c in formula:
        if c.isalpha():
            variables.add(c)
    variables = list(variables)
    # 生成所有可能的真值字典列表
    truth_values = list(np.ndindex((2,) * len(variables)))
    # 生成逆波兰表达式
    rp_formula = to_reverse_polish(formula)
    # 检查公式真值结果的列表
    truth_values_result = []
    # 计算公式真值情况
    for values in truth_values:
        values = dict(zip(variables, values))
        truth_values_result.append(evaluate_reverse_polish(rp_formula, values))
    # 判断公式真值情况
    cnt=0
    for result in truth_values_result:
        if result:
            cnt+=1
    if cnt==len(truth_values_result):
        return 0
    elif cnt==0:
        return 1
    else:
        return 2  
def EqualOrNot(formula1, formula2):
    """
    判断两个公式是否逻辑等价

    参数:
    - formula1: 公式1
    - formula2: 公式2

    返回值:
    - True: 公式1和公式2逻辑等价
    - False: 公式1和公式2不逻辑等价
    """
    def to_cnf(formula: str) -> str:
        """
        将合式公式转换为合取范式
        
        参数:
        - formula: 合式公式字符串

        返回值:
        - cnf: 合取范式字符串
        """
        variables = sorted(set(filter(str.isalpha, formula)))
        clauses = []
        for i in range(2 ** len(variables)):
            values = {variables[j]: bool(i & (1 << j)) for j in range(len(variables))}
            if evaluate(formula, values):
                clause = []
                for variable, value in values.items():
                    if value:
                        clause.append(variable)
                    else:
                        clause.append('¬' + variable)
                clauses.append(' ∧ '.join(clause))
        return ' ∨ '.join(clauses)

    def evaluate(formula: str, values: dict[str, bool]) -> bool:
        expression = to_reverse_polish(formula)
        return evaluate_reverse_polish(expression, values)


    def to_reverse_polish(formula: str) -> list[str]:
        stack = []
        output = []
        precedence = {
        '¬': 3,
        '∧': 2,
        '∨': 1,
        '→': 0,
        '↔': 0,
        '⨁': 0,
    }

        for token in formula:
            if token.isalpha():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif token in precedence:
                while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                    output.append(stack.pop())
                stack.append(token)
            else:
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output


    def evaluate_reverse_polish(expression: list[str], values: dict[str, bool]) -> bool:
        stack = []

        for token in expression:
            if token.isalpha():
                stack.append(values[token])
            elif token == '¬':
                stack.append(not stack.pop())
            elif token == '∧':
                right = stack.pop()
                left = stack.pop()
                stack.append(left and right)
            elif token == '∨':
                right = stack.pop()
                left = stack.pop()
                stack.append(left or right)
            elif token == '→':
                right = stack.pop()
                left = stack.pop()
                stack.append(not left or right)
            elif token == '↔':
                right = stack.pop()
                left = stack.pop()
                stack.append(left == right)
            elif token == '⨁':
                right = stack.pop()
                left = stack.pop()
                stack.append(left != right)

        return stack.pop()
    # 将两个公式转化为CNF
    cnf_formula1 = to_cnf(formula1)
    cnf_formula2 = to_cnf(formula2)
    # 判断两个公式是否逻辑等价
    if cnf_formula1 == cnf_formula2:
        return True
    else:
        return False
def main():
    print("这是第一个函数的测试:")
    m=int(input("请输入变元的个数(m的值):"))
    n=int(input("请输入公式的复杂度(n的值):"))
    print("随机生成的公式为:")
    print(Produce(m,n))
    print("--------------------")
    print("以下环节中,输入合式公式的要求是:")
    print("1.变元为26个小写字母和26个大写字母,即52个字母")
    print("2.联结词集合为{ ¬ , ∧ , ∨ , → , ↔ , ⨁ }")
    print("3.括号只能用小括号")
    print("4.其他字符只能是空格")
    print("--------------------")
    print("这是第二个函数的测试:")
    formula=input("请输入公式:")
    if(TrueOrNot(formula)==0):
        print("返回值为0,公式为永真式")
    elif(TrueOrNot(formula)==1):
        print("返回值为1,公式为永假式")
    else: 
        print("返回值为2,公式为可满足式")
    print("--------------------")
    print("这是第三个函数的测试:")
    formula1=input("请输入公式1:")
    formula2=input("请输入公式2:")
    if(EqualOrNot(formula1,formula2)):
        print("公式1和公式2逻辑等价")
    else:
        print("公式1和公式2不逻辑等价")
if __name__=="__main__":
    main()