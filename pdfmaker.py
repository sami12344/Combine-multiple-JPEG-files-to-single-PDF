from fpdf import FPDF
from PIL import Image
import os
from tqdm import tqdm
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

# Function to get page number position based on user choice
def get_page_number_position(position, page_width, page_height):
    if position == "bottom left":
        return (10, 10)  # x=10, y=10
    elif position == "bottom right":
        return (page_width - 30, 10)  # x=page_width-30, y=10
    elif position == "top left":
        return (10, page_height - 20)  # x=10, y=page_height-20
    elif position == "top right":
        return (page_width - 30, page_height - 20)  # x=page_width-30, y=page_height-20
    elif position == "top middle":
        return (page_width / 2 - 10, page_height - 20)  # x=center, y=page_height-20
    elif position == "bottom middle":
        return (page_width / 2 - 10, 10)  # x=center, y=10
    else:
        raise ValueError("Invalid position selected.")

# Function to create a temporary PDF with a page number
def create_page_number_pdf(page_num, position, page_width, page_height):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))
    x, y = get_page_number_position(position, page_width, page_height)
    can.setFont("Helvetica", 12)
    can.drawString(x, y, str(page_num))
    can.save()
    packet.seek(0)
    return packet

# Ask the user if they want to combine multiple PDF files
combine_pdfs = input("Do you want to combine multiple PDF files? (yes/no): ").strip().lower()

# If combining PDFs, prompt for the folder containing PDF files
if combine_pdfs == 'yes':
    pdf_folder = input("Enter the path to the folder containing PDF files to combine: ")
    output_folder = input("Enter the path to the output folder: ")
    output_pdf_name = input("Enter the name of the output PDF file (without extension): ")
    combined_pdf_path = os.path.join(output_folder, f'{output_pdf_name}_combined.pdf')

    # Ask the user if they want to add page numbers
    add_page_numbers = input("Do you want to add page numbers? (yes/no): ").strip().lower()

    if add_page_numbers == 'yes':
        # Ask the user where to insert the page numbers
        page_number_position = input(
            "Where do you want to insert page numbers? "
            "(bottom left, bottom right, top left, top right, top middle, bottom middle): "
        ).strip().lower()

        # Ask the user for the starting page number
        start_page_number = int(input("Enter the starting page number (e.g., 1, 10, etc.): ").strip())

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    merger = PdfMerger()
    pdf_files = sorted([f for f in os.listdir(pdf_folder) if f.endswith('.pdf')])

    for pdf_file in tqdm(pdf_files, desc="Combining PDFs", unit="file"):
        merger.append(os.path.join(pdf_folder, pdf_file))

    merger.write(combined_pdf_path)
    merger.close()

    # Add page numbers if the user chose "yes"
    if add_page_numbers == 'yes':
        reader = PdfReader(combined_pdf_path)
        writer = PdfWriter()

        for i in range(len(reader.pages)):
            page = reader.pages[i]

            # Get the page dimensions
            page_width = float(page.mediabox[2])
            page_height = float(page.mediabox[3])

            # Create a temporary PDF with the page number
            temp_pdf = create_page_number_pdf(start_page_number + i, page_number_position, page_width, page_height)

            # Merge the page number with the original page
            page_number_reader = PdfReader(temp_pdf)
            page.merge_page(page_number_reader.pages[0])

            writer.add_page(page)

        # Write the modified PDF to the output file
        with open(combined_pdf_path, "wb") as f:
            writer.write(f)

    print(f"Combined PDF saved to {combined_pdf_path}")

else:
    # Prompt the user for the input folder containing image files
    image_folder = input("Enter the path to the folder containing image files (JPEG, JPG, PNG): ")

    # Prompt the user for the output folder and PDF filename
    output_folder = input("Enter the path to the output folder: ")
    output_pdf_name = input("Enter the name of the output PDF file (without extension): ")
    output_pdf = os.path.join(output_folder, f'{output_pdf_name}.pdf')

    # Ask the user if they want to add page numbers
    add_page_numbers = input("Do you want to add page numbers? (yes/no): ").strip().lower()

    if add_page_numbers == 'yes':
        # Ask the user where to insert the page numbers
        page_number_position = input(
            "Where do you want to insert page numbers? "
            "(bottom left, bottom right, top left, top right, top middle, bottom middle): "
        ).strip().lower()

        # Ask the user for the starting page number
        start_page_number = int(input("Enter the starting page number (e.g., 1, 10, etc.): ").strip())

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize PDF object
    pdf = FPDF()

    # Function to add page numbers based on the selected position
    def add_page_number(pdf, page_num, position, page_width, page_height):
        x, y = get_page_number_position(position, page_width, page_height)
        pdf.set_font('Arial', 'I', 12)  # Set font style
        pdf.set_xy(x, y)
        pdf.cell(10, 10, str(page_num), 0, 0, 'C')  # Center-align the page number

    # Get the list of image files in the input folder
    image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

    # Check if there are any images to process
    if not image_files:
        print("No image files found in the specified folder.")
        exit()

    # Loop through all image files in the input folder with a progress bar
    page_num = start_page_number if add_page_numbers == 'yes' else 1  # Initialize page number
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
                add_page_number(pdf, page_num, page_number_position, 210, 297)
                page_num += 1  # Increment page number
        except Exception as e:
            print(f"Error processing image {image_name}: {e}")

    # Save the PDF to the specified output path
    pdf.output(output_pdf, "F")

    print(f"PDF saved to {output_pdf}")