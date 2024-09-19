from PIL import Image
import os

def convert_image(input_path):
    # Supported output formats
    supported_formats = ['JPEG', 'PNG', 'BMP', 'GIF', 'TIFF']

    # Check if the file exists
    if not os.path.isfile(input_path):
        print("File not found. Please provide a valid image file path.")
        return

    try:
        # Attempt to open the image to validate it
        with Image.open(input_path) as img:
            # Get the input image format
            input_format = img.format
            print(f"The input image format is: {input_format}")

            # Present conversion options to the user (excluding current format)
            print("Select the format to convert the image into:")
            conversion_options = [fmt for fmt in supported_formats if fmt != input_format]

            for i, fmt in enumerate(conversion_options, 1):
                print(f"{i}. {fmt}")

            # Get the user's choice
            choice = int(input("Enter the number corresponding to the desired format: "))

            if 1 <= choice <= len(conversion_options):
                # Selected format
                selected_format = conversion_options[choice - 1]

                # Create the output file path
                base_name = os.path.splitext(input_path)[0]  # Remove original extension
                output_path = f"{base_name}.{selected_format.lower()}"

                # Convert and save the image
                img.save(output_path, selected_format)
                print(f"Image successfully converted to {selected_format} and saved as {output_path}.")
            else:
                print("Invalid choice. Please select a valid format number.")

    except IOError:
        print("Invalid image type. Please upload another image.")

# Example usage
input_path = input("Enter the path of the image file: ")
convert_image(input_path)