# 图片转化为 base64 编码并写入剪贴板。

# 导入 base64、os、pyperclip 模块。
import base64
import os
import pyperclip

def image_to_base64_with_clipboard(image_path):
    """
    将图片转换为 Base64 编码，将编码复制到剪贴板，并将编码写入同名的 .txt 文件。
    :param image_path: 图片的路径。
    """
    try:
        # 读取图片并编码
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()

        # 复制到剪贴板
        pyperclip.copy(encoded_string)

        # 写入同名的 .txt 文件
        base_name = os.path.splitext(image_path)[0]
        txt_file_path = base_name + ".txt"
        with open(txt_file_path, "w") as text_file:
            text_file.write(encoded_string)

        return f"Base64 编码已复制到剪贴板并写入到 {txt_file_path}"
    except Exception as e:
        return f"发生错误: {e}"

# 示例使用方法
# Example usage:
image_path = input("请输入您的图片路径: ")
result = image_to_base64_with_clipboard(image_path)
print(result)

# 按下回车键退出。
input("按回车键退出...")