# PDF Maker

This script converts a folder of JPEG images into a single PDF file. It also provides an option to add page numbers to the PDF.

## Requirements

- Python 3.x
- `fpdf` library
- `Pillow` library
- `tqdm` library

You can install the required libraries using pip:

```bash
pip install fpdf Pillow tqdm
```

## Usage

1. Run the script:

```bash
python pdfmaker.py
```

2. Follow the prompts to provide the input folder, output folder, and output PDF filename.

3. Choose whether to add page numbers to the PDF.

## Features

- Converts all JPEG images in the specified folder to a single PDF.
- Optionally adds page numbers to the PDF.
- Displays a progress bar while processing images.

## Example

```bash
Enter the path to the folder containing JPEG images: /path/to/images
Enter the path to the output folder: /path/to/output
Enter the name of the output PDF file (without extension): my_pdf
Do you want to add page numbers? (yes/no): yes
```

## Error Handling

- The script checks if there are any JPEG images in the specified folder and exits if none are found.
- Errors encountered while processing individual images are printed to the console, and the script continues processing the remaining images.

## Output

The resulting PDF file is saved to the specified output folder with the provided filename.

## License

This project is licensed under the MIT License.
