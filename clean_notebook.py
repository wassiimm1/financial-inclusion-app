import nbformat
import os

# Replace with your notebook filename
notebook_filename = "Financial_Inclusion_in_Africa.ipynb"

# Load the notebook
with open(notebook_filename, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove widgets metadata if it exists
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Save the cleaned notebook (overwrite the original)
with open(notebook_filename, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Notebook '{notebook_filename}' has been cleaned successfully!")
