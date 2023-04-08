from PyPDF2 import PdfMerger

merger = PdfMerger()
pdf_files = ["1.pdf","2.pdf"]
for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write("merged_2_pages.pdf")
merger.close()