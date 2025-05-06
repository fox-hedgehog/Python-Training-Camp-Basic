"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 复制原字典以避免修改原始数据
    sd = students_dict.copy()
    op = operation
    
    if op == "add":
        name, score = args
        if name in sd:
            raise ValueError(f"学生 '{name}' 已存在，不能重复添加")
        sd[name] = score
        return sd
    
    elif op == "update":
        name, score = args
        if name not in sd:
            raise ValueError(f"学生 '{name}' 不存在，无法更新")
        sd[name] = score
        return sd

    elif op == "remove":
        name, = args
        if name not in sd:
            raise ValueError(f"学生 '{name}' 不存在，无法删除")
        del sd[name]
        return sd

    elif op == "get":
        name, = args
        return sd.get(name, None)

    else:
        raise ValueError(f"未知的操作类型: {op}")