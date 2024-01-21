# 复制文件夹内所有文件的文件名生成空文件。

# 导入 os 模块。
import os

# 询问用户文件夹位置。
source_folder = input("请输入源文件夹的绝对路径：")
target_folder = input("请输入目标文件夹的绝对路径：")

# 遍历源文件夹内的所有文件。
for file in os.listdir(source_folder):
    # 获取文件的完整路径。
    source_file = os.path.join(source_folder, file)
    # 判断是否是文件，如果是，则复制文件名。
    if os.path.isfile(source_file):
        # 获取文件名。
        file_name = os.path.basename(source_file)
        # 拼接目标文件的完整路径。
        target_file = os.path.join(target_folder, file_name)
        # 创建一个空文件。
        open(target_file, "w").close()
        # 打印提示信息。
        print(f"已复制 {file_name} 到 {target_folder}")

# 按下回车键退出。
input("按回车键退出...")