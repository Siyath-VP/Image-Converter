# Image Format Converter

This Python application allows users to convert images from one format to another. The program automatically detects the input image format and presents the user with conversion options. If an invalid image type is uploaded, the program will prompt the user to upload another image.

## Features
- Automatically detects the image format.
- Presents conversion options excluding the current image format.
- Supports conversion to popular formats: **JPEG, PNG, BMP, GIF, and TIFF**.
- User-friendly messages for successful conversion and error handling.

## Prerequisites

Before using this application, make sure you have the following installed:

1. **Python 3.x**
2. **Pillow** library (for image processing)

### Installing Pillow

To install the required Pillow library, run the following command:
pip install Pillow

**Getting Started**
Follow these steps to use the Image Format Converter:

1. Clone the Repository or Download the Script
You can either clone this repository or download the image_converter.py file from the repository to your local machine.
git clone https://github.com/your-username/image-format-converter.git
2. Prepare an Image File
Ensure you have an image file you want to convert. The file can be in JPEG, PNG, BMP, GIF, or TIFF format.
3. Run the Program
To run the program, follow these steps:
Open a terminal or command prompt.
Navigate to the directory where the image_converter.py file is located.
Run the program using the following command:
python image_converter.py
4. Input the Image Path
Once you run the program, it will ask you to enter the path to the image file.
Example:
Enter the path of the image file: /path/to/your/image.jpg
Make sure to enter the full path to the image file you want to convert.
5. Select the Desired Format
The program will automatically detect the current format of the image and display conversion options. For example:

The input image format is: JPEG
Select the format to convert the image into:
1. PNG
2. BMP
3. GIF
4. TIFF
Enter the number corresponding to the desired format: 
Enter the number corresponding to the desired format (e.g., 1 for PNG).
The program will then convert the image and save the output in the same directory as the input file.
6. View the Converted Image
Once the image is successfully converted, a message will be displayed indicating the new format and the file location:

Image successfully converted to PNG and saved as /path/to/your/image.png
You can now open or use the converted image.

**Error Handling**
If the provided file is not a valid image, the program will show an error message:
Invalid image type. Please upload another image.

If the file path is incorrect or the file doesn't exist, the program will notify you:
File not found. Please provide a valid image file path.

**Supported Formats**
Input Formats: JPEG, PNG, BMP, GIF, TIFF
Output Formats: JPEG, PNG, BMP, GIF, TIFF (excluding the current format of the input image)

Here's an example of the program flow:

Enter the path of the image file: /path/to/your/image.jpg
The input image format is: JPEG
Select the format to convert the image into:
1. PNG
2. BMP
3. GIF
4. TIFF
Enter the number corresponding to the desired format: 1
Image successfully converted to PNG and saved as /path/to/your/image.png.
