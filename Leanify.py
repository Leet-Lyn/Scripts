# 用 Leanify 压缩文件。

# 导入 subprocess 模块。
import subprocess

# 定义 compress 函数。
def compress():
    path = input("请输入需压缩的文件位置（按回车键使用默认地址：t:\\XXX\\）：") or "t:\\XXX\\"  # 请输入需压缩的文件位置。
    subprocess.run(["d:\\ProApps\\Leanify\\Leanify.exe", path])  # 使用 Leanify 压缩

compress()  # 运行 compress 函数

# 按下回车键退出。
input("按回车键退出...")
