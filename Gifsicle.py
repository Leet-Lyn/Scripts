# 使用 gifsicle 命令来压缩 gif 文件。

# 导入模块。
import os
import subprocess
import imageio
import numpy as np

def get_color_count(gif_path):
    """
    获取 GIF 图像的颜色数量。
    :param gif_path: GIF 文件的路径
    :return: 颜色数量
    """
    try:
        reader = imageio.get_reader(gif_path)
        all_colors = set()
        for frame in reader:
            np_frame = np.array(frame)
            for row in range(np_frame.shape[0]):
                for col in range(np_frame.shape[1]):
                    pixel = np_frame[row, col]
                    # 检查像素是单一数值还是颜色元组
                    if pixel.shape == ():  # 单一数值
                        all_colors.add(pixel.item())  # 将numpy数值转换为Python标准数值
                    else:  # 颜色元组
                        all_colors.add(tuple(pixel))
        return len(all_colors)
    except Exception as e:
        print(f"无法处理文件 {gif_path}: {e}")
        return 256  # 返回默认值

def compress_gif(source_folder, target_folder):
    """
    遍历指定的源文件夹中的所有 GIF 文件，并使用 gifsicle 命令对它们进行压缩，
    如果 GIF 的颜色数量少于 256，调整为其自身颜色数量。
    然后将压缩后的文件保存到指定的目标文件夹，并在压缩成功后删除原文件。
    
    :param source_folder: 源文件夹路径
    :param target_folder: 目标文件夹路径
    """
    # 确保目标文件夹存在，如果不存在，则创建它
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for file in os.listdir(source_folder):
        if file.endswith(".gif"):
            source_file = os.path.join(source_folder, file)
            target_file = os.path.join(target_folder, file)

            # 获取 GIF 图片的颜色数量
            color_count = get_color_count(source_file)
            color_count = min(color_count, 256)  # 确保颜色数量不超过 256

            # 构建命令，将每个参数作为列表的一个元素
            command = ["gifsicle", "-O3", f"--colors={color_count}", "--lossy=80", source_file, "-o", target_file]
            result = subprocess.run(command)
            if result.returncode == 0:
                # 压缩成功，删除原文件
                os.remove(source_file)
                print(f"压缩 {file} 成功并保存至 {target_folder}，原文件已删除")
            else:
                print(f"压缩 {file} 失败")

if __name__ == "__main__":
    # 请求用户输入源文件夹和目标文件夹的路径
    source_folder = input("请输入源文件夹路径: ")
    target_folder = input("请输入目标文件夹路径: ")

    # 调用函数执行压缩操作
    compress_gif(source_folder, target_folder)
    # 等待用户按下回车键后退出
    input("按回车键退出...")