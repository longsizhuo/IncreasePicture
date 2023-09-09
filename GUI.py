import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, ttk
import functions


# ---------------------------------------------GUI--------------------------------------------------
def select_input_image():
    global input_image_path
    input_image_path = filedialog.askopenfilename(title="Select Input Image",
                                                  filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    filename = os.path.basename(input_image_path)
    text = f"你的文件‘{filename}’初始为 {os.path.getsize(input_image_path) / (1024 * 1024):.2f}MB"
    input_label.config(text=text)


def process_image():
    input_image = input_image_path
    if not input_image:
        messagebox.showerror("Error", "Please select an input image.")
        return

    filename = os.path.basename(input_image)

    # 如果input的文件的文件夹中有output.png
    if os.path.exists(os.path.join(os.path.dirname(input_image), f"{filename}output.png")):
        os.remove(os.path.join(os.path.dirname(input_image), f"{filename}output.png"))

    output_image_path = os.path.join(os.path.dirname(input_image), f"{filename}_output.png")

    if input_image.endswith(".png"):
        size = functions.resize_image(input_image, output_image_path)
    else:
        size = functions.increase_image_size(input_image, output_image_path)

    aim_size_str = aim_size_entry.get()
    if aim_size_str:
        aim_size = float(aim_size_str)
        if aim_size:
            functions.resize_image_to_target_size(output_image_path, output_image_path, aim_size)
            size = os.path.getsize(output_image_path) / (1024 * 1024)

    result_label.config(text=f"现在是: {size:.2f}MB")


def input_and_process():
    select_input_image()
    process_image()


# GUI Setup
root = Tk()
root.title("图片体积调整\nImage Size Adjuster")

# resize the window
root.geometry("250x700")

# Input Image Selection
input_button = Button(root, text="选一张图片:\nSelect Input Image", command=input_and_process)
input_button.pack(pady=20)
input_label = Label(root, text="")
input_label.pack(pady=10)

# Aim Size Entry
aim_size_label = Label(root, text="目标体积:\nSize you want (in MB):")
aim_size_label.pack(pady=10)
aim_size_entry = Entry(root)
aim_size_entry.pack(pady=10)

# Process Button
process_button = Button(root, text="再运行一下:\nProcess Image", command=process_image)
process_button.pack(pady=20)

# Progress Bar
progress_label = Label(root, text="进度:\nProgress")
progress_label.pack(pady=10)
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Result Label
result_label = Label(root, text="")
result_label.pack(pady=20)

warning_label = Label(root, text="注意：\n")
warning_label.pack(pady=20)
root.mainloop()
