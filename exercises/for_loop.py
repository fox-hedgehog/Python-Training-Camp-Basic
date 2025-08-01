"""
练习: for循环

描述：
计算从1到n的所有整数之和。

请补全下面的函数，使用for循环计算从1到n的所有整数之和。
"""

def sum_numbers(n):
    """
    计算从1到n的所有整数之和
    
    参数:
    - n: 正整数
    
    返回:
    - 从1到n的所有整数之和
    """
    # 请在下方编写代码
    res = 0
    for i in range(n+1):
        res += i
    return res