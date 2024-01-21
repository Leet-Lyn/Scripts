# 用 ed2k hash 对文件夹下所有文件重命名为生成的 ed2k hash。

# 导入 hashlib 和 os 模块。
import hashlib
import os

# 定义一个函数，计算文件的 ed2k hash。
def ed2k_hash(file):
    # 定义一个常量，表示每个块的大小。
    CHUNK_SIZE = 9728000
    # 创建一个 MD4 对象。
    md4 = hashlib.new('md4')
    # 打开文件。
    with open(file, 'rb') as f:
        # 读取第一个块。
        chunk = f.read(CHUNK_SIZE)
        # 如果文件不为空。
        if chunk:
            # 创建一个列表，存储所有块的 MD4 哈希值。
            hashes = []
            # 循环读取剩余的块。
            while chunk:
                # 计算当前块的 MD4 哈希值，并添加到列表中。
                hashes.append(hashlib.new('md4', chunk).digest())
                # 读取下一个块。
                chunk = f.read(CHUNK_SIZE)
            # 如果只有一个块，直接返回它的 MD4 哈希值的十六进制表示。
            if len(hashes) == 1:
                return hashes[0].hex()
            # 否则，将所有块的 MD4 哈希值连接起来，再计算它们的 MD4 哈希值，并返回十六进制表示。
            else:
                md4.update(b''.join(hashes))
                return md4.hexdigest()
        # 如果文件为空，返回空字符串。
        else:
            return ''

# 提示用户输入源文件夹位置。
source_folder = input("请输入源文件夹位置（按回车键使用默认地址：t:\XXX\）：") or "t:\\XXX\\" 
# 遍历源文件夹下的所有文件。
for file in os.listdir(source_folder):
    # 获取文件的完整路径。
    file_path = os.path.join(source_folder, file)
    # 如果是文件，而不是文件夹。
    if os.path.isfile(file_path):
        # 计算文件的 ed2k hash。
        file_hash = ed2k_hash(file_path)
        # 如果 ed2k hash 不为空。
        if file_hash:
            # 获取文件的扩展名，并转换为小写。
            file_ext = os.path.splitext(file)[1].lower()
            # 获取文件的大小，并转换为字符串。
            file_size = str(os.path.getsize(file_path))
            # 生成新的文件名，为 ed2k hash 加上方括号，并在头部再加方括号和文件大小。
            new_file_name = '[' + file_size + ']' + '[' + file_hash + ']' + file_ext.lower()
            # 生成新的文件路径，为源文件夹加上新的文件名。
            new_file_path = os.path.join(source_folder, new_file_name)
            # 重命名文件。
            os.rename(file_path, new_file_path)
            # 打印重命名成功的信息。
            print(f'{file} 已重命名为 {new_file_name}')
        # 如果 ed2k hash 为空，跳过该文件，并打印跳过信息。
        else:
            print(f'{file} 是空文件，已跳过')
            
# 按下回车键退出。
input("按回车键退出...")