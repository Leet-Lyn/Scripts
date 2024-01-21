# 获取文件夹下所有文件夹名，到一个文件内。

# 导入 os 模块。
import os

# 询问用户输入文件夹和文件的位置。
folder = input("请输入要获取文件名的文件夹的位置：")
if not folder:
    folder = os.getcwd()
filename = input("请输入要保存文件名的文件的文件名（默认是“files.txt”）：")
if not filename:
    filename = "files.txt"
path = input("请输入要保存文件名的文件的存放的位置（默认是“t:\X\”）：")
if not path:
    path = "t:\\X\\"

output_path = os.path.join(path, filename)

# 遍历指定文件夹下的所有子文件夹，并将结果写入指定的输出文件。
with open(output_path, 'w') as f:
    for root, dirs, files in os.walk(folder):
        f.write(root + '\n')

# 按下回车键退出。
input("按回车键退出...")