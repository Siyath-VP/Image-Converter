from PIL import Image
import os

def convert_image(input_path):
    supported_formats = ['JPEG', 'PNG', 'BMP', 'GIF', 'TIFF']

    if not os.path.isfile(input_path):
        print("File not found. Please provide a valid image file path.")
        return

    try:
        with Image.open(input_path) as img:
            input_format = img.format
            print(f"The input image format is: {input_format}")

            print("Select the format to convert the image into:")
            conversion_options = [fmt for fmt in supported_formats if fmt != input_format]

            for i, fmt in enumerate(conversion_options, 1):
                print(f"{i}. {fmt}")

            choice = int(input("Enter the number corresponding to the desired format: "))

            if 1 <= choice <= len(conversion_options):
                selected_format = conversion_options[choice - 1]

                base_name = os.path.splitext(input_path)[0]
                output_path = f"{base_name}.{selected_format.lower()}"

                img.save(output_path, selected_format)
                print(f"Image successfully converted to {selected_format} and saved as {output_path}.")
            else:
                print("Invalid choice. Please select a valid format number.")

    except IOError:
        print("Invalid image type. Please upload another image.")

input_path = input("Enter the path of the image file: ")
convert_image(input_path)
