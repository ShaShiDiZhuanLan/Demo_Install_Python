# 1、Python语言的应用 之 Demo_Install_Python
讲述如何在windows和linux上如何打包，单个文件、多个文件、多级目录、图标设置等
<BR/>
# 2、更新信息
开发者：沙振宇（沙师弟专栏） <BR/>
创建时间：2019-1-20<BR/>
CSDN博客名称：Python开发 之 Python3打包（windows/linux）详解 <BR/> 
CSDN博客地址：https://shazhenyu.blog.csdn.net/article/details/104054250 <BR/> 
<BR/> 
# 3、环境
Python版本：3.6.8 <BR/>
Windows版本：Windows 10 家庭中文版 64-bit (10.0, Build 18362) (18362.19h1_release.190318-1202) <BR/>
Linux版本：centos7.4 <BR/>
打包工具：https://pypi.org/project/PyInstaller/ <BR/>
 <BR/>
# 4、pyinstaller打包工具
pyinstaller -F *.py -n test -i test.ico<BR/>
常用可选项及说明：<BR/>
-F：打包后只生成单个exe格式文件；<BR/>
-D：默认选项，创建一个目录，包含exe文件以及大量依赖文件；<BR/>
-n：可选的项目(产生的spec的)名字.如果省略,第一个脚本的主文件名将作为spec的名字<BR/>
-w：不使用控制台；<BR/>
-p：添加搜索路径，让其找到对应的库；<BR/>
-i：改变生成程序的icon图标。<BR/>
