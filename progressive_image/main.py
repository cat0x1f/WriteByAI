import os
from PIL import Image

def convert_to_progressive_jpg(folder_path, output_folder):
    """
    将文件夹中的所有图片转换为渐进式 JPEG 格式。

    :param folder_path: 输入图片所在文件夹路径
    :param output_folder: 转换后图片保存的文件夹路径
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        input_path = os.path.join(folder_path, filename)

        # 检查文件是否为图片
        try:
            with Image.open(input_path) as img:
                # 构造输出路径
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")

                # 转换为渐进式 JPEG
                img = img.convert("RGB")  # 确保是 RGB 模式
                img.save(output_path, "JPEG", progressive=True)
                print(f"转换成功: {filename} -> {output_path}")
        except Exception as e:
            print(f"无法转换文件 {filename}: {e}")

# 示例使用
if __name__ == "__main__":
    input_folder = "./input_images"  # 输入图片文件夹路径
    output_folder = "./output_images"  # 输出图片文件夹路径

    convert_to_progressive_jpg(input_folder, output_folder)
