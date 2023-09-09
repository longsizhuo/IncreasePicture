import os
import GUI
import functions
if not GUI or not functions:
    print("Please run this script in the root folder of this project.")
    exit(1)
# 获取当前脚本所在的文件夹的绝对路径
current_folder = os.path.dirname(os.path.abspath(__file__))
"""
如果GUI失效，就用这个，自己调整一下引用
# # Path to the input image, the picture is fromhttps://pixabay.com/zh/vectors/logo-template-heart-red-decor-5413944/
# input_image_path = "example.png"
# output_image_path = "output.png"
# if input_image_path.endswith(".png"):
#     size = resize_image(input_image_path, output_image_path)
# else:
#     size = increase_image_size(input_image_path, output_image_path)
# aim_size = int(input(f"Do u want to reduce ur pic_size? The size is {size}MB now. If it is, Enter the size of the image\n "
#                      "If not, just leave it blank. \n"
#                      "Size you want(in MB): \n"
#                      ))
# if aim_size:
#     resize_image_to_target_size("output.png", output_image_path, aim_size)
"""

