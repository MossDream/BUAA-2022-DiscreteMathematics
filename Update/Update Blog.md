## 更新日志 Update Blogs🐱‍🏍
### **2023/04/08** **April 8th , 2023**  
* 更新了 **[math_1.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_1.py)** 题目及参考代码文件  
* Update with **[math_1.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_1.py)** for reference code and question.  

### **2023/04/10** **April 10th , 2023**  
* 更新了 **[math_2.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_2.py)** 题目及参考代码文件  
* Update with **[math_2.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_2.py)** for reference code and question.

### **2023/04/14** **April 14th , 2023**  
* 更新了 **[math_3.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_3.py)** 题目及参考代码文件  
* Update with **[math_3.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_3.py)** for reference code and question.

### **2023/04/29** **April 29th , 2023**  
* 更新了 **[math_4.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_4.py)** 题目及参考代码文件  
* Update with **[math_4.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_4.py)** for reference code and question.

### **2023/05/19** **May 19th , 2023**  
* 更新了 **[math_last.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_last.py)** 题目及参考代码文件  
* Update with **[math_last.py](https://github.com/MossDream/Discrete-Mathematics-Python/blob/main/Code/math_last.py)** for reference code and question.
 
⚠**特别说明**  
最后一次文件是挑战题，具体要求如下：

----
通过Python语言，共三个函数（第三方库只能使用numpy），编程实现：  
**1.生成符合条件的合式公式，联结词集合{¬,∧,∨,→, ↔ ,⨁}，变元数量为m，公式复杂度为n；** 
```
def  Produce(m，n)
'''m变元数量    
n为公式复杂度   

“result为公式字符串列表'''  
Return result
```

**2.判断生成的公式是不是永真式，永假式，可满足式；**
```
def  TrueOrNot(m)     
'''m为公式字符串 

“result是整数结果类型，0代表永真式，1代表永假式，2代表可满足式'''   
Return result  
```
**3.判断生成的两个公式否是逻辑等价**。
```
def  EqualOrNot(m,n)    
'''m为公式字符串1,n为公式字符串2

result为True 或Fals'''  
Return result    
```

本题评分标准：  
1）若可以根据输入的m和n的随机生成正确的公式，则根据生成公式的多样性评分0～30分。  
2）输入k条测试公式，根据正确判断数得分(k0⁄k)*20，其中k为测试公式总数，k0为程序输出正确结果的公式数目；  
3）采用m对公式对程序进行测试，判断是否逻辑等价，m0为正确判断的数目。基于真值表的方法得分(m0⁄m)*30，基于等值演算的方法得分(m0⁄m)*50  
