# Arabic OCR

This project uses the `ArabicOcr` package to convert Arabic text in images to editable text using OCR techniques.

> [!NOTE]
> The script may take a long time to run the first time as it installs the prediction model.

## Installation

Install the required package using pip:

```bash
pip install ArabicOcr
```

## Usage

```python
from ArabicOcr import arabicocr

# Define the input and output image paths
image_path = 'pic.jpg'
out_image = 'out.jpg'

# Perform OCR on the image
results = arabicocr.arabic_ocr(image_path, out_image)
print(results)

# Extract words from the results
words = [result[1] for result in results]

# Save the words to a text file
with open('file.txt', 'w', encoding='utf-8') as myfile:
    myfile.write(str(words))
```

## Description

The `ArabicOcr` package is used to convert Arabic text in images to text using OCR techniques.

