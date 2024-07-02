from ArabicOcr import arabicocr  # Importing the arabicocr module

image_path = 'pic.jpg'  # Path to the input image
out_image = 'out.jpg'  # Path to the output image

# Calling the arabic_ocr function from the arabicocr module
results = arabicocr.arabic_ocr(image_path, out_image)

print(results)  # Printing the results

words = []  # Empty list to store the extracted words

# Looping through the results and extracting the words
for i in range(len(results)):
    word = results[i][1]  # Extracting the word from the result tuple
    words.append(word)  # Adding the word to the words list

# Writing the words list to a text file named 'file.txt' with UTF-8 encoding
with open('file.txt', 'w', encoding='utf-8') as myfile:
    myfile.write(str(words))
