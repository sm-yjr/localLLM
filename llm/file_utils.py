import base64
import os
from typing import List, Dict

def encode_image_to_base64(file_path: str) -> str:
    """
    将图片文件转换为base64编码字符串

    Args:
        file_path (str): 图片文件的路径

    Returns:
        str: base64编码的字符串，格式为 "data:image/xxx;base64,..."
    """
    # 获取文件扩展名
    _, ext = os.path.splitext(file_path)
    ext = ext.lower().lstrip('.')
    
    # 设置MIME类型
    mime_types = {
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif',
        'bmp': 'image/bmp',
        'webp': 'image/webp'
    }
    mime_type = mime_types.get(ext, 'application/octet-stream')
    
    try:
        with open(file_path, 'rb') as image_file:
            # 读取文件并转换为base64
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:{mime_type};base64,{encoded_string}"
    except Exception as e:
        print(f"Error encoding image {file_path}: {str(e)}")
        return None

def process_uploaded_files(file_paths: List[str]) -> List[str]:
    """
    处理上传的图片文件列表，转换为base64编码

    Args:
        file_paths (List[str]): 图片文件路径列表

    Returns:
        List[str]: base64编码的图片列表
    """
    encoded_images = []
    for file_path in file_paths:
        encoded_image = encode_image_to_base64(file_path)
        if encoded_image:
            encoded_images.append(encoded_image)
    return encoded_images

def is_valid_image(file_path: str) -> bool:
    """
    检查文件是否为有效的图片文件

    Args:
        file_path (str): 文件路径

    Returns:
        bool: 如果是有效的图片文件返回True，否则返回False
    """
    valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    _, ext = os.path.splitext(file_path)
    return ext.lower() in valid_extensions

if __name__ == "__main__":
    # 测试代码
    test_image_path = "path/to/test/image.jpg"
    if os.path.exists(test_image_path):
        encoded = encode_image_to_base64(test_image_path)
        print(f"Encoded image length: {len(encoded) if encoded else 'Failed'}") 