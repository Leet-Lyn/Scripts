# 从一个文件夹复制文件夹结构到另一个文件夹，但不复制文件。

# 导入 os 模块。
import os

# 询问源文件夹和目标文件夹的位置。
source = input("请输入源文件夹的位置：")
target = input("请输入目标文件夹的位置：")

# 遍历源文件夹的所有子文件夹和文件。
for root, dirs, files in os.walk(source):
    # 获取相对路径。
    relative_path = os.path.relpath(root, source)
    # 创建相同的子文件夹在目标文件夹。
    for dir in dirs:
        target_dir = os.path.join(target, relative_path, dir)
        os.makedirs(target_dir, exist_ok=True)
    # 不复制文件。

# 按下回车键退出。
input("按回车键退出...")