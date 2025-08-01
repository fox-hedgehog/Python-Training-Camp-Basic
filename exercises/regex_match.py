"""
练习: 正则表达式匹配

在本练习中，你将练习使用Python的正则表达式来处理文本匹配和提取。
"""
import re

def find_emails(text):
    """
    从文本中提取所有的电子邮件地址。
    
    参数:
        text (str): 要搜索的文本
        
    返回:
        list: 文本中找到的所有电子邮件地址的列表
    """
    # 实现你的代码: 使用正则表达式查找所有邮箱地址
    # 邮箱格式通常为: username@domain.com
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)


def is_valid_phone_number(phone):
    """
    验证字符串是否为有效的中国手机号码。
    有效的手机号码应该:
    1. 长度为11位
    2. 以1开头
    3. 第二位是3-9之间的数字
    4. 全部由数字组成
    
    参数:
        phone (str): 要验证的电话号码字符串
        
    返回:
        bool: 如果是有效的手机号码则返回True，否则返回False
    """
    # 实现你的代码: 验证手机号码是否合法
    pattern = r'^1[3-9]\d{9}$'
    return re.fullmatch(pattern, phone) is not None


def extract_urls(text):
    """
    从文本中提取所有的URL链接。
    
    参数:
        text (str): 要搜索的文本
        
    返回:
        list: 文本中找到的所有URL的列表
    """
    # 实现你的代码: 使用正则表达式提取所有URL
    # 需要考虑http://和https://开头的URL
    url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?'
    return re.findall(url_pattern, text)