import numpy as np

def Produce(m, n):
    """
    生成符合条件的合式公式

    参数:
    - m: 变元数量
    - n: 公式复杂度

    返回值:
    - formula: 生成的合式公式
    """

    # 定义联结词集合
    connectives = ['¬', '∧', '∨', '→', '↔', '⨁']
    all_values=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U' ,'V','W','X','Y','Z']
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

    result = generate_sub_formula(n)
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
    # 检查公式真值
    for values in truth_values:
    
    
    # 构建联结词的等值演算规则
    connectives = {
        '¬': (lambda p: np.logical_not(p)),
        '∧': (lambda p, q: np.logical_and(p, q)),
        '∨': (lambda p, q: np.logical_or(p, q)),
        '→': (lambda p, q: np.logical_or(np.logical_not(p), q)),
        '↔': (lambda p, q: np.logical_or(np.logical_and(p, q), np.logical_and(np.logical_not(p), np.logical_not(q)))),
        '⨁': (lambda p, q: np.logical_xor(p, q))
    }
    #
    
    
    

    

def check_equivalence(formula1, formula2, m):
    """
    判断两个公式是否逻辑等价

    参数:
    - formula1: 公式1
    - formula2: 公式2
    - m: 变元数量

    返回值:
    - True: 公式1和公式2逻辑等价
    - False: 公式1和公式2不逻辑等价
    """

    # 生成所有可能的真值列表
    truth_values = list(np.ndindex((2,) * m))

    # 检查两个公式的真值是否一致
    for values in truth_values:
        result1 = TrueOrNot(formula1)
        result2 = TrueOrNot(formula2)
        if result1 != result2:
            return False

    return True
def main():
    print(Produce(4,4))
    print(Produce(4,4))
    print(Produce(4,4))
    print(Produce(4,4))
    print(TrueOrNot("(p ∨ q) ∧ (¬p ∨ q) ↔ (p ∨ q ∨ r)"))


if __name__=="__main__":
    main()