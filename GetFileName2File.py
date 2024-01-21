# 获取文件夹下所有文件名，到一个文件内。

# 导入 os 模块。
import os

# 问用户输入文件夹和文件的位置。
folder = input("请输入要获取文件名的文件夹的位置：")
if not folder:
    folder = os.getcwd()
filename = input("请输入要保存文件名的文件的文件名（默认是“files.txt”）：")
if not filename:
    filename = "files.txt"
path = input("请输入要保存文件名的文件的存放的位置（默认是“t:\X\”）：")
if not path:
    path = "t:\\X\\"

# 拼接文件的完整路径。
file = os.path.join(path, filename)

# 打开文件。遍历文件夹下的所有文件和子文件夹。
with open(file, "w") as f:
    for root, dirs, files in os.walk(folder):
        for name in files:
            f.write(os.path.join(root, name) + "\n")

# 按下回车键退出。
input("按回车键退出...")