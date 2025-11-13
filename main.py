import customtkinter as ctk
import tkinter as tk
import qrcode
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image


class QRCodeGenerator:
    def __init__(self, root, geometry):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry(geometry)
        self.root.resizable(False, False)

        self.theme_dropdown = None

        self.setup_ui()

    def setup_ui(self):
        self.set_background_image()


        title_label = tk.Label(self.root, text="QR Code Generator", font=("Arial", 20, "bold"), bg="#d1eaff", fg="black")
        title_label.pack(pady=20)

        input_label = tk.Label(self.root, text="Enter text or link", bg="#d1eaff", fg="black", font=("Arial", 10))
        input_label.pack(pady=(5, 0))

        self.data_entry = ctk.CTkEntry(
            self.root,
            width=350,
            placeholder_text="Enter text or link",
            text_color="black",
            bg_color="#d1eaff",
            border_width=0
        )
        self.data_entry.pack(pady=(0, 10))

        button_frame = tk.Frame(self.root, bg="#d1eaff")
        button_frame.pack(pady=5)

        generate_btn = ctk.CTkButton(button_frame, text="Generate QR Code", command=self.generate_qrcode)
        generate_btn.pack(side="left", padx=5)

        save_btn = ctk.CTkButton(button_frame, text="Save QR Code", command=self.save_qrcode)
        save_btn.pack(side="left", padx=5, pady=5)

        self.theme_menu = ctk.CTkOptionMenu(
            self.root,
            values=["Light", "Dark", "System"],
            command=self.set_theme,
            width=140,
            bg_color="#d1eaff"
        )
        self.theme_menu.place(relx=0.99, rely=0.01, anchor="ne")
        self.theme_menu.set("Theme")

        self.qr_label = ctk.CTkLabel(self.root, text="", bg_color="#d1eaff")
        self.qr_label.pack(pady=10)
        self.qr_label.pack_forget()

    def set_background_image(self):
        bg_image = Image.open("background.jpg")
        bg_image = bg_image.resize((700, 700))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def generate_qrcode(self):
        data = self.data_entry.get().strip()
        if not data:
            messagebox.showerror("Error", "Please enter some text or a link!")
            return

        qr_img = qrcode.make(data)
        qr_img = qr_img.resize((250, 250))
        self.qr_image = ctk.CTkImage(light_image=qr_img, dark_image=qr_img, size=(250, 250))
        self.qr_label.pack(pady=20)
        self.qr_label.configure(image=self.qr_image, text="")

    def save_qrcode(self):
        if not hasattr(self, "qr_image"):
            messagebox.showerror("Error", "Please generate a QR code first!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")],
        )

        if file_path:
            data = self.data_entry.get().strip()
            qr_code = qrcode.make(data)
            qr_code.save(file_path)
            messagebox.showinfo("Saved", "QR Code has been saved to " + file_path)

    def set_theme(self, choice):
        ctk.set_appearance_mode(choice.lower())


if __name__ == "__main__":
    root = ctk.CTk()
    width = 700
    height = 700
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws // 2) - (width // 2)
    y = (hs // 2) - (height // 2)
    geo = f"{width}x{height}+{x}+{y}"
    tapp = QRCodeGenerator(root, geo)
    root.mainloop()
