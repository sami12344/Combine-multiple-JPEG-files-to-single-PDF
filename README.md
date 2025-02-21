# PDF Maker

This script converts a folder of image files (JPEG, JPG, PNG) into a single PDF file. It also provides options to add page numbers and combine multiple PDF files.

## Requirements

- Python 3.x
- `fpdf` library
- `Pillow` library
- `tqdm` library
- `PyPDF2` library
- `reportlab` library

You can install the required libraries using pip:

```bash
pip install fpdf Pillow tqdm PyPDF2 reportlab
```

## Usage

1. Run the script:

```bash
python pdfmaker.py
```

2. Choose whether to combine multiple PDF files.

3. If combining PDFs, provide the folder containing the PDF files and the output folder and filename.

4. Choose whether to add page numbers to the combined PDF and specify the position and starting page number.

5. If not combining PDFs, follow the prompts to provide the input folder, output folder, and output PDF filename.

6. Choose whether to add page numbers to the PDF and specify the position and starting page number.

## Features

- Converts all image files (JPEG, JPG, PNG) in the specified folder to a single PDF.
- Optionally adds page numbers to the PDF.
- Optionally combines multiple PDF files into a single PDF.
- Displays a progress bar while processing images.
- Handles mixed image formats in the specified folder.

## Example

### Combining PDFs

```bash
Do you want to combine multiple PDF files? (yes/no): yes
Enter the path to the folder containing PDF files to combine: /path/to/pdfs
Enter the path to the output folder: /path/to/output
Enter the name of the output PDF file (without extension): combined_pdf
Do you want to add page numbers? (yes/no): yes
Where do you want to insert page numbers? (bottom left, bottom right, top left, top right, top middle, bottom middle): bottom right
Enter the starting page number (e.g., 1, 10, etc.): 1
```

### Converting Images to PDF

```bash
Do you want to combine multiple PDF files? (yes/no): no
Enter the path to the folder containing image files (JPEG, JPG, PNG): /path/to/images
Enter the path to the output folder: /path/to/output
Enter the name of the output PDF file (without extension): my_pdf
Do you want to add page numbers? (yes/no): yes
Where do you want to insert page numbers? (bottom left, bottom right, top left, top right, top middle, bottom middle): bottom right
Enter the starting page number (e.g., 1, 10, etc.): 1
```

## Error Handling

- The script checks if there are any image files in the specified folder and exits if none are found.
- Errors encountered while processing individual images are printed to the console, and the script continues processing the remaining images.

## Output

The resulting PDF file is saved to the specified output folder with the provided filename. If combining multiple PDFs, the combined PDF is saved with `_combined` appended to the filename.

## License

This project is licensed under the MIT License.
