from PyPDF2 import PdfWriter, PdfReader

# Create a PdfFileWriter object
out = PdfWriter()

# Open encrypted PDF file with the PdfFileReader
file_name = "encrypted.pdf"
file = PdfReader(file_name)

# Store correct password in a variable password.
password = "Update password here"

# Check if the opened file is actually Encrypted
if file.is_encrypted:

    # If encrypted, decrypt it with the password
    file.decrypt(password)

    for page_no in range(len(file.pages)):
        # Get the page at index idx
        page = file.pages[page_no]

        # Add it to the output file
        out.add_page(page)

    decrypted_file_name = "decrypted_"+file_name
    with open(decrypted_file_name, "wb") as f:
        out.write(f)

    print("File decrypted Successfully, please check file "+decrypted_file_name)
else:
    print("File already decrypted, no need to decrypt it")
