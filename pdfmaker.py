from fpdf import FPDF
from PIL import Image
import os
from tqdm import tqdm

# Prompt the user for the input folder containing JPEG images
image_folder = input("Enter the path to the folder containing JPEG images: ")

# Prompt the user for the output folder and PDF filename
output_folder = input("Enter the path to the output folder: ")
output_pdf_name = input("Enter the name of the output PDF file (without extension): ")
output_pdf = os.path.join(output_folder, f'{output_pdf_name}.pdf')

# Ask the user if they want to add page numbers
add_page_numbers = input("Do you want to add page numbers? (yes/no): ").strip().lower()

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize PDF object
pdf = FPDF()

# Function to add page numbers (just the number) in the corner
def add_page_number(pdf, page_num):
    pdf.set_font('Arial', 'I', 10)  # Set font style
    pdf.set_xy(195, 5)  # Set position closer to the top-right corner (x=190, y=5)
    pdf.cell(10, 10, str(page_num), 0, 0, 'R')  # Add just the number

# Get the list of JPEG images in the input folder
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.jpeg')])

# Check if there are any images to process
if not image_files:
    print("No JPEG images found in the specified folder.")
    exit()

# Loop through all JPEG images in the input folder with a progress bar
page_num = 1  # Initialize page number
for image_name in tqdm(image_files, desc="Processing images", unit="image"):
    try:
        # Open the image
        img_path = os.path.join(image_folder, image_name)
        img = Image.open(img_path)

        # Add a new page to the PDF
        pdf.add_page()

        # Add the image to the PDF (A4 size: 210x297 mm)
        pdf.image(img_path, 0, 0, 210, 297)

        # Add page number if the user chose "yes"
        if add_page_numbers == 'yes':
            add_page_number(pdf, page_num)
            page_num += 1  # Increment page number
    except Exception as e:
        print(f"Error processing image {image_name}: {e}")

# Save the PDF to the specified output path
pdf.output(output_pdf, "F")

print(f"PDF saved to {output_pdf}")