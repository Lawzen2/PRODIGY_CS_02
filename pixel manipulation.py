from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image
import numpy as np

# Function to encrypt an image
def encrypt_image(input_path, key):
    image = Image.open(input_path)
    image_array = np.array(image)
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save("encrypted_image.png")
    return "encrypted_image.png"

# Function to decrypt an image
def decrypt_image(input_path, key):
    image = Image.open(input_path)
    image_array = np.array(image)
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save("decrypted_image.png")
    return "decrypted_image.png"

# Function to select a file
def select_file(operation, key):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        if operation == "encrypt":
            output_path = encrypt_image(file_path, key)
            messagebox.showinfo("Success", f"Image encrypted and saved as: {output_path}")
        elif operation == "decrypt":
            output_path = decrypt_image(file_path, key)
            messagebox.showinfo("Success", f"Image decrypted and saved as: {output_path}")
    else:
        messagebox.showerror("Error", "No file selected!")

# Function to create the GUI
def create_gui():
    root = Tk()
    root.title("Image Encryption Tool - Developed by Khalid")
    root.geometry("500x400")
    root.configure(bg="#2C3E50")  # Background color

    # Heading
    Label(root, text="Image Encryption Tool", font=("Helvetica", 18, "bold"), fg="#ECF0F1", bg="#2C3E50").pack(pady=20)

    # Buttons for encryption and decryption
    Button(
        root, text="Encrypt Image", font=("Helvetica", 12), bg="#1ABC9C", fg="#2C3E50", relief="raised",
        command=lambda: select_file("encrypt", key=50)
    ).pack(pady=10)

    Button(
        root, text="Decrypt Image", font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1", relief="raised",
        command=lambda: select_file("decrypt", key=50)
    ).pack(pady=10)

    # Footer Note
    Label(root, text="Developed by Khalid", font=("Helvetica", 10), fg="#95A5A6", bg="#2C3E50").pack(side="bottom", pady=10)

    root.mainloop()

# Run the GUI application
if __name__ == "__main__":
    create_gui()
