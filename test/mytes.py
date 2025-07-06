import struct
import marshal


def get_pyc_version(pyc_file):
    with open(pyc_file, 'rb') as f:
        # 读取前4个字节，这是 magic number
        magic_number = f.read(4)

        # 读取接下来的4个字节，这是 timestamp
        timestamp = f.read(4)

        # 读取接下来的4个字节（Python 3.7 及以上版本），这是 source size
        if len(magic_number) == 4:
            source_size = f.read(4)

        # 读取接下来的4个字节，这是编译版本信息
        version_info = f.read(4)

        # 将 version_info 转换为整数
        version = struct.unpack('<I', version_info)[0]

        # 获取 Python 版本
        python_version = f"{version >> 16}.{version & 0xFFFF}"

        return python_version


# 示例用法
# pyc-magic ./__pycache__/my_module.cpython-39.pyc
pyc_file = '/Users/chunyunluo/Downloads/tools/app/helper/backstagehelper.pyc'
print(f"编译版本: {get_pyc_version(pyc_file)}")