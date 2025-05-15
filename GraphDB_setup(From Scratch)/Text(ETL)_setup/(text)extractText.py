import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def extract_text_from_folder(folder_path, output_folder):
    """Extracts text from all PDFs in a folder and saves each as a text file."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create output folder if not exists

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)

            output_file = os.path.join(output_folder, filename.replace(".pdf", ".txt"))
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"Extracted text from: {filename}")

# Change these paths
pdf_folder = "SmartTrend"  # Folder containing PDFs(i manually extracted one by one.)

output_folder = "extracted_text"  # Folder to save extracted text files

extract_text_from_folder(pdf_folder, output_folder)
print("Text extraction complete.")
