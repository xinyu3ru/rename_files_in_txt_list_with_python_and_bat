#!/bin/env python
# -*- coding: utf-8 -*-
"""从某网站下载了一批文档，但是文件是用数字串命名的文档（很多图书馆都这样吧），
也有文档列表，所以写了一个脚本来重命名批文件

"""
__author__ = 'rublog'
import os

#1.txt文档要求每个文档一行，保存的时候必须为ANSI格式，前面是列表文档名含后缀（就是网站上文件名，一串数字
#或者字母什么的），空一格，然后是文档的真名（不带后缀）
#get_list这个从1.txt文本文件中一行一行的读取文件，去掉换行符，然后调用doc_rename
#函数
def get_list():
    #尝试不同的编码来自知乎 十五
    #https://www.zhihu.com/question/30070752/answer/46684320
    decode_list=["utf-8",'gb18030', 'ISO-8859-2','gb2312',"gbk","Error" ]#编码集
    #GBK不如GB18030覆盖得好，容易出错，故首先尝试GB18030。
    for k in decode_list:#编码集循环
        try:
            book_list = open('1.txt', encoding=k)
            #打开路径中的文本
            line = book_list.readline()
            while line:
                if os.name == 'nt':
                    line = line.strip('\r\n')
                else:
                    line = line.strip('\n')
                doc_rename(line)
                line = book_list.readline()
            break#打开路径成功跳出编码匹配
        except:
            if k == "Error":#如果碰到这个程序终止运行
                print("had no way to decode")
                raise Exception("%s had no way to decode"%directions)
            continue
#重命名，构造完整的路径和后缀
def doc_rename(book_list_line):
    try:
        name_list = book_list_line.split(' ')
        list_name = name_list[0]
        cool_list = list_name.split('.')
        ext = cool_list[-1]
        current_folder = os.getcwd()
        real_name = name_list[1]
        real_name = os.path.join(current_folder, real_name)
        real_name_ext = real_name+'.'+ext
        os.rename(os.path.join(current_folder, list_name), real_name_ext)
        print('success')
    except:
        pass
    return 0
#据说高手都会写的主函数
if __name__ == '__main__':
    get_list()