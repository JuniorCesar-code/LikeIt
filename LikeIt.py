import tkinter as tk
from tkinter import messagebox
import pyperclip

class LikeShareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Like & Share Application")
        self.root.geometry("340x220")
        self.root.resizable(False, False)

        self.like_count = 0
        self.liked = False

        content_frame = tk.Frame(root, bg="white", bd=1, relief="solid", padx=12, pady=10)
        content_frame.pack(fill="x", padx=20, pady=(20, 12))

        tk.Label(content_frame, text="Check out this Post!", font=("Arial", 13, "bold"),
                 bg="white").pack()
        tk.Label(content_frame, text="Python is awesome", font=("Arial", 11),
                 fg="#555", bg="white").pack()

        btn_frame = tk.Frame(root, bg=root.cget("bg"))
        btn_frame.pack(pady=4)

        self.like_btn = tk.Button(btn_frame, text="🤍 Like (0)", width=14,
                                  font=("Arial", 11), command=self.toggle_like,
                                  bg="#f0f0f0", relief="flat", cursor="hand2")
        self.like_btn.grid(row=0, column=0, padx=6)

        share_btn = tk.Button(btn_frame, text="🔗 Share", width=14,
                              font=("Arial", 11), command=self.share_post,
                              bg="#f0f0f0", relief="flat", cursor="hand2")
        share_btn.grid(row=0, column=1, padx=6)

        self.status_var = tk.StringVar()
        tk.Label(root, textvariable=self.status_var, font=("Arial", 10),
                 fg="#555").pack(pady=8)

    def toggle_like(self):
        self.liked = not self.liked
        if self.liked:
            self.like_count += 1
            self.like_btn.config(text=f"❤️ Like ({self.like_count})", bg="#ffe0e0")
            self.status_var.set("You liked this post!")
        else:
            self.like_count -= 1
            self.like_btn.config(text=f"🤍 Like ({self.like_count})", bg="#f0f0f0")
            self.status_var.set("Like removed.")

    def share_post(self):
        link = "https://www.instagram.com/yourprofile"
        try:
            pyperclip.copy(link)
            self.status_var.set("Link copied to clipboard!")
        except Exception:
            messagebox.showinfo("Share", f"Share this link:\n{link}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LikeShareApp(root)
    root.mainloop()








