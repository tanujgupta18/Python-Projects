import PyPDF2
import itertools

def brute_force_pdf_password(file_path, max_length):
    # charset = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*+-= '
    charset = '0123456789'
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for length in range(1, max_length + 1):
            for attempt in itertools.product(charset, repeat=length):
                password = ''.join(attempt)
                try:
                    if reader.decrypt(password):
                        print(f"Success! The Password is: {password}")
                        return password
                except Exception as e:
                    print(f"An error occurred: {e}")
                    continue

    print("Sorry! Password not found")
    return None

file_path = 'Bank.pdf'
max_length = 11
brute_force_pdf_password(file_path, max_length)
