"""
PDF Merger
"""
import tkinter as tk
from tkinter import filedialog
import PyPDF2


def merge_pdfs(output_filename, pdf_files):
    merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        if pdf_file:
            merger.append(pdf_file)

    with open(output_filename, "wb") as output_file:
        merger.write(output_file)


def select_files():
    file_paths = filedialog.askopenfilenames(
        filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        output_filename = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_filename:
            merge_pdfs(output_filename, file_paths)
            print("PDFs merged successfully.")


app = tk.Tk()
app.withdraw()

select_files()
