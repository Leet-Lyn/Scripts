# 对文件夹内所有文件名重命名。从某一字段开始至末尾删除。

# 导入 os 模块。
import os

# 询问用户文件夹的位置。
folder = input("请输入文件夹的位置：")
if folder == "":
    folder = os.path.abspath(".")
    
# 询问用户想要删除的字段。
field = input("请输入想要删除的字段，默认为“（Via：”。")
if field == "":
    field = "（Via："

# 遍历文件夹内所有文件。
for file in os.listdir(folder):
    # 如果文件名包含字段。
    if field in file:
        # 获取字段在文件名中的位置。
        index = file.index(field)
        # 获取文件名的前缀和后缀。
        prefix = file[:index]
        suffix = os.path.splitext(file)[1]
        # 生成新的文件名。
        new_file = prefix + suffix
        # 重命名文件。
        os.rename(os.path.join(folder, file), os.path.join(folder, new_file))
        # 打印重命名信息。
        print(f"已将 {file} 重命名为 {new_file}")
    else:
        # 如果文件名不包含字段，跳过。
        continue

# 按下回车键退出。
input("按回车键退出...")