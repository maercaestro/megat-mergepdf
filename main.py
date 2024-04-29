import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import os
import tempfile

def merge_pdfs(input_paths, output_path):
    # Create a PDF merger object
    merger = PdfWriter()

    # Loop through each PDF file and append it to the merger in the specified order
    for path in input_paths:
        with open(path, 'rb') as file:
            reader = PdfReader(file)
            for page in range(len(reader.pages)):
                merger.add_page(reader.pages[page])

    # Write the merged PDF to the output file
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)


# Function to split PDF based on specified page range
def split_pdf(input_path, output_path, start_page, end_page):
    # Create a PDF reader object
    reader = PdfReader(input_path)

    # Create a PDF writer object
    writer = PdfWriter()

    # Loop through the specified page range and add pages to the writer object
    for page_num in range(start_page - 1, min(end_page, reader.getNumPages())):
        writer.addPage(reader.getPage(page_num))

    # Write the extracted pages to the output file
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

# Streamlit app
st.sidebar.title("MEGAT PDF Toolkit")

# Sidebar selection for choosing between splitting and merging
app_mode = st.sidebar.selectbox("Choose an application", ["Merge PDFs", "Split PDFs"])

if app_mode == "Merge PDFs":
    st.title("MEGAT Merge PDFs")

    # Allow user to upload multiple PDF files
    uploaded_files = st.file_uploader("Upload PDF files", accept_multiple_files=True, type='pdf')

    if uploaded_files:
        st.write("Uploaded PDF files:")
        file_names = [file.name for file in uploaded_files]

        output_filename = st.text_input("Enter the filename for the merged PDF", "merged.pdf")

        # Merge PDF files when the user clicks the button
        if st.button("Merge PDFs"):
            # Create a temporary directory
            temp_dir = tempfile.mkdtemp()
            input_files = []

            # Save uploaded files to the temporary directory
            for file_index, uploaded_file in enumerate(uploaded_files):
                file_path = os.path.join(temp_dir, f"{file_index}.pdf")
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())
                input_files.append(file_path)

            output_file = output_filename  # Output file name

            merge_pdfs(input_files, output_file)
            st.success("PDFs merged successfully!")

            # Provide download link for the merged PDF file
            with open(output_file, 'rb') as f:
                st.download_button(label="Download Merged PDF", data=f, file_name=output_file, mime='application/pdf')

elif app_mode == "Split PDFs":
    st.title("MEGAT Split PDFs")

    # Allow user to select a PDF file to split
    pdf_to_split = st.file_uploader("Select PDF file to split", type='pdf')

    if pdf_to_split:
        st.write("Selected PDF file:")
        st.write(pdf_to_split.name)

        # Input fields for start and end page
        start_page = st.number_input("Start Page", value=1, min_value=1)
        end_page = st.number_input("End Page", value=1, min_value=1)

        # Radio button to choose output location
        output_location = st.radio("Output Location", options=["Download", "Save Locally"], index=0)

        # Split PDF when the user clicks the button
        if st.button("Split PDF"):
            # Create a temporary directory
            temp_dir = tempfile.mkdtemp()
            input_file_path = os.path.join(temp_dir, pdf_to_split.name)
            output_file = f"split_{pdf_to_split.name}"

            # Save uploaded file to the temporary directory
            with open(input_file_path, "wb") as f:
                f.write(pdf_to_split.read())

            split_pdf(input_file_path, output_file, start_page, end_page)
            st.success("PDF split successfully!")

            # Provide download link for the split PDF file or save it locally
            if output_location == "Download":
                with open(output_file, 'rb') as f:
                    st.download_button(label="Download Split PDF", data=f, file_name=output_file, mime='application/pdf')
            else:
                st.markdown(f"Download your split PDF file from [this link](/{output_file})")
