## MEGAT PDF Toolkit

This toolkit provides functionalities to merge and split PDF files.

### Merge PDFs

To merge multiple PDF files, follow these steps:

1. Upload PDF files: Click on the "Upload PDF files" button and select the PDF files you want to merge.
2. Enter filename: Specify the filename for the merged PDF file.
3. Click "Merge PDFs": This will merge the uploaded PDF files into a single PDF.
4. Download merged PDF: After successful merging, click on the "Download Merged PDF" button to download the merged PDF file.

### Split PDFs

To split a PDF file into multiple parts, follow these steps:

1. Select PDF file: Click on the "Select PDF file to split" button and choose the PDF file you want to split.
2. Specify start and end page: Enter the start and end page numbers for splitting the PDF.
3. Choose output location: Select whether you want to download the split PDF file or save it locally.
4. Click "Split PDF": This will split the selected PDF file according to the specified page range.
5. Download or save split PDF: After successful splitting, you can either download the split PDF file or save it locally, depending on your choice.

### Requirements

- Python 3.x
- streamlit
- PyPDF2

### Installation

To install the required dependencies, run:
```python
pip install -r requirements.txt
```
### Usage

To run the MEGAT PDF Toolkit, execute the following command:
```
streamlit run <filename>.py
```
