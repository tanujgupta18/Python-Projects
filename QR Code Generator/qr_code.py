import qrcode as qr

def generate_qr_code(url, image_name):
    img = qr.make(url)
    img.save(f"{image_name}.png")

def main():
    url = input("Enter the URL: ")
    image_name = input("Enter the Image Name: ")

    if url and image_name:
        generate_qr_code(url, image_name)
        print("QR Code generated successfully!")
    else:
        print("Please enter both a valid URL and image name.")

if __name__ == "__main__":
    main()
