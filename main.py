import tkinter as tk
import qrcode
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk

class QRCodeGenerator:
    def __init__(self, root, geometry):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry = geometry
        self.root.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):
        title_label = ttk.Label(self.root, text="QR Code Generator", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        input_label = ttk.Label(self.root, text="Enter text, link, or file path:")
        input_label.pack(pady=5)

        self.data_entry = ttk.Entry(self.root, width=50)
        self.data_entry.pack(pady=10)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=5)

        generate_btn = ttk.Button(button_frame, text="Generate QR Code", command=self.generate_qrcode)
        generate_btn.pack(side="left", padx=5)

        save_btn = ttk.Button(button_frame, text="Save QR Code", command=self.save_qrcode)
        save_btn.pack(side="left", pady=5)

        self.qr_label = ttk.Label(self.root)
        self.qr_label.pack(pady=10)

    def generate_qrcode(self):
        data = self.data_entry.get().strip()
        if not data:
            messagebox.showerror("Error", "Please enter some text or a link!")
            return

        qr_img = qrcode.make(data)
        qr_img = qr_img.resize((250, 250))
        self.qr_image = ImageTk.PhotoImage(qr_img)
        self.qr_label.configure(image=self.qr_image)

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
if __name__ == "__main__":
    root = tk.Tk()
    width = 500
    height = 500
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws // 2) - (width // 2)
    y = (hs // 2) - (height // 2)
    geo = root.geometry(f"{width}x{height}+{x}+{y}")
    tapp = QRCodeGenerator(root, geo)
    root.mainloop()
