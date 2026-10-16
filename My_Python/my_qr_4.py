import qrcode
import os


def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    img.save(filename)

    print(f"\nQR Code successfully saved as '{filename}'")


def main():
    print("===== QR CODE GENERATOR =====")

    data = input("Enter text or URL: ").strip()

    filename = input(
        "Enter filename to save (e.g., qr.png): "
    ).strip()

    generate_qr(data, filename)


if __name__ == "__main__":
    main()
    
    