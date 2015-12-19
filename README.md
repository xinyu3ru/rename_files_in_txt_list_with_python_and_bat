# rename files in txt list with python and bat
#根据txt文件列表重命名文件，python版本和bat版本

最近从某网站下载了一批文档，但是文件是用数字串命名的文档（很多图书馆都这样吧），现在我也下载完了这些文件，也有这些文件的列表，但不能一个一个的把文件给重命名吧！所以。。。。。
###文件列表格式如下
>ts001003.pdf 世界科技全景百卷书(3)近代科技
  
  
>ts001004.pdf 世界科技全景百卷书(4)蒸汽机带来的革命
  
  
>ts001005.pdf 世界科技全景百卷书(5)现代科技

##一、使用bat脚本（windows系统默认可用）
  
  
脚本来源 [脚本之家terse](http://www.bathome.net/thread-15815-1-1.html)
  
要求文件放在d:/pdf文件夹下，文件后缀为.pdf,文件列表放在1.txt下面，txt保存为微软下的默认ANSI格式。
  
  
有需要的可以适当修改。
  
##二、使用python脚本（python 3.50）
  
要求文件放在普通文件夹下，文件后缀可以任意（不过后缀要和txt内的列表中文件后缀一样）,文件列表放在1.txt下面，txt保存为微软下的默认ANSI格式或者UTF无BOM格式。
  
1.txt文档要求每个文档一行，保存的时候必须为ANSI或者UTF无BOM格式，其他格式没事测试。
  
前面是列表文档名含后缀（就是网站上文件名，一串数字或者字母什么的），空一格，然后是文档的真名（不带后缀）
  
已作为博文发表于 [rublog](http://www.5169.info/motion/bat-he-python-pi-liang-zhong-ming-ming-wen-jian.html)