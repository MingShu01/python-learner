import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def write_base64_to_file(base64_string, output_path):
    with open(output_path, "w") as text_file:
        text_file.write(base64_string)

# 使用方法
image_path = 'your_image.png'  # 请替换为你的图片路径
output_path = 'output.txt'  # 请替换为你想要写入的txt文件路径
base64_string = image_to_base64(image_path)
write_base64_to_file(base64_string, output_path)
