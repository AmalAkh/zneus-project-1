from nbconvert import PDFExporter
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat

def convert_to_pdf(notebook_filename):
   
    

    # Load the notebook
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)

    # 1️⃣ Execute the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': '.'}})

    # 2️⃣ Export executed notebook to PDF
    pdf_exporter = PDFExporter()
    body, resources = pdf_exporter.from_notebook_node(nb)

    # 3️⃣ Save as PDF
    output_filename = notebook_filename.replace(".ipynb", ".pdf")
    with open(output_filename, "wb") as f:
        f.write(body)

filenames = ["eda.ipynb","normalization.ipynb","model-binary.ipynb","model-multiclass.ipynb"]

for filename in filenames:
    convert_to_pdf(filename)

