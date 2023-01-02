# import PdfFileWriter and PdfFileReader
# class from PyPDF2 library
from PyPDF2 import PdfWriter, PdfReader

# Create a PdfFileWriter object
out = PdfWriter()

# Open encrypted PDF file with the PdfFileReader
file = PdfReader("encrypted.pdf")

# Store correct password in a variable password.
password = "GBEPK0250B"

# Check if the opened file is actually Encrypted
if file.is_encrypted:

    # If encrypted, decrypt it with the password
    file.decrypt(password)

    # Now, the file has been unlocked.
    # Iterate through every page of the file
    # and add it to our new file.
    for idx in range(len(file.pages)):
        # Get the page at index idx
        page = file.pages[idx]

        # Add it to the output file
        out.add_page(page)

    # Open a new file "myfile_decrypted.pdf"
    with open("myfile_decrypted.pdf", "wb") as f:

        # Write our decrypted PDF to this file
        out.write(f)

    # Print success message when Done
    print("File decrypted Successfully.")
else:

    # If file is not encrypted, print the
    # message
    print("File already decrypted.")
