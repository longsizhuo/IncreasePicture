from PIL import Image
import os
import GUI


def increase_image_size(input_path, output_path, quality=95):
    """
    Increase the size of a JPEG image by increasing its quality.

    Parameters:
    - input_path: Path to the input JPEG image.
    - output_path: Path to save the output JPEG image.
    - quality: Quality of the output image (default is 95, max is 100).
    """
    with Image.open(input_path) as img:
        img.save(output_path, "JPEG", quality=quality)
        print(file_size_mb := os.path.getsize(output_path) / (1024 * 1024), "MB.")
        return file_size_mb


def resize_image(input_path, output_path, scale_factor=2):
    """
    Resize a PNG image by a scale factor.

    Parameters:
    - input_path: Path to the input PNG image.
    - output_path: Path to save the output PNG image.
    - scale_factor: Factor by which to resize the image (default is 2).
    """
    with Image.open(input_path) as img:
        new_dimensions = (int(img.width * scale_factor), int(img.height * scale_factor))
        resized_img = img.resize(new_dimensions, Image.LANCZOS)
        resized_img.save(output_path, "PNG", compress_level=0)
        print(file_size_mb := os.path.getsize(output_path) / (1024 * 1024), "MB.")

        return file_size_mb


def resize_image_to_target_size(input_path, output_path, target_size_mb=2):
    """
    Reduce a PNG image to be within a target file size.

    Parameters:
    - input_path: Path to the input PNG image.
    - output_path: Path to save the output PNG image.
    - target_size_mb: Target file size in megabytes (default is 2MB).
    """
    with Image.open(input_path) as img:
        # Initially save with no compression
        img.save(output_path, "PNG", compress_level=0)

        # Check file size
        file_size_mb = os.path.getsize(output_path) / (1024 * 1024)

        # Adjust compression level based on file size
        compress_level = 0
        while file_size_mb > target_size_mb and compress_level < 9:
            compress_level += 1
            img.save(output_path, "PNG", compress_level=compress_level)
            file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
        # Update progress bar
        if GUI.progress_bar:
            GUI.progress_bar['value'] = (compress_level / 9) * 100
            GUI.root.update_idletasks()  # Update GUI

        if file_size_mb > target_size_mb:
            print(f"Warning: Unable to reduce the image size to below {target_size_mb}MB.")
            GUI.warning_label.config(text=f"Warning: Unable to reduce the image size to below {target_size_mb}MB.")
        else:
            print(f"Image saved with size {file_size_mb:.2f}MB.")
            # result_label.config(text=f"Image saved with size {file_size_mb:.2f}MB.")
