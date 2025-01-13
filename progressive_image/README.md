# 图片转换为渐进式 JPEG 格式工具

此工具可以将指定文件夹中的所有图片文件批量转换为渐进式 JPEG 格式，适用于任何支持 `Pillow` 库的 Python 环境。

## 功能

- 将文件夹中的所有图片转换为渐进式 JPEG 格式。
- 支持常见图片格式（如 PNG、JPEG、BMP 等）。
- 转换后的图片保存在指定的输出文件夹中。

## 安装

1. 确保已安装 Python 3.x 版本。
2. 使用 `pip` 安装 `Pillow` 库：

```bash
pip install pillow
```

## 使用方法

1. 下载脚本，并将其保存到本地。
2. 创建一个文件夹，将待转换的图片放入该文件夹。
3. 在脚本中修改输入输出路径：
    - `input_folder`: 输入图片文件夹的路径。
    - `output_folder`: 输出转换后图片的文件夹路径。

4. 运行脚本：
5. 转换后的图片会保存在指定的输出文件夹中。

## 示例

假设你有一个名为 `input_images` 的文件夹，里面有若干图片，转换后的图片将保存到 `output_images` 文件夹。

```python
input_folder = "./input_images"  # 输入文件夹路径
output_folder = "./output_images"  # 输出文件夹路径

convert_to_progressive_jpg(input_folder, output_folder)
```

## 注意事项

- 如果输入文件夹中的某些文件无法打开或不是图片格式，脚本会跳过这些文件并输出相应的错误信息。
- 请确保输出文件夹存在，脚本会自动创建它（如果它不存在）。
