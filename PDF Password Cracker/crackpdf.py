import PyPDF2
import itertools
import time

def brute_force_pdf_password(file_path, max_length, charset):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        if not reader.is_encrypted:
            print("The PDF is not encrypted!")
            return None

        start_time = time.time()
        for length in range(1, max_length + 1):
            for attempt in itertools.product(charset, repeat=length):
                password = ''.join(attempt)
                try:
                    print(f"Trying password: {password}")
                    if reader.decrypt(password):
                        print(f"Success! The Password is: {password}")
                        print(f"Time taken: {time.time() - start_time} seconds")
                        return password
                except Exception as e:
                    continue

        print("Password not found.")
        return None

file_path = 'Test.pdf'
max_length = 6
charset = '0123456789'

brute_force_pdf_password(file_path, max_length, charset)
