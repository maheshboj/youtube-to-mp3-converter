import os
import sys
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def convert_url(url, output_dir, status_label, progress_bar, btn_convert):
    if not url.strip():
        messagebox.showwarning("Input Error", "Please enter a valid YouTube URL.")
        return

    status_label.config(text="Downloading and converting to MP3...", foreground="#1e88e5")
    progress_bar.start(10)
    btn_convert.config(state="disabled")
    
    # Process asynchronously via Tkinter after or run subprocess
    def run():
        try:
            cmd = [
                "yt-dlp",
                "-x",
                "--audio-format", "mp3",
                "--audio-quality", "0",
                "--output", os.path.join(output_dir, "%(title)s.%(ext)s"),
                url.strip()
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            status_label.config(text="Download & Conversion Complete! 🎉", foreground="#2e7d32")
            messagebox.showinfo("Success", f"MP3 saved to:\n{output_dir}")
        except subprocess.CalledProcessError as e:
            err_msg = e.stderr if e.stderr else str(e)
            status_label.config(text="Error occurred during conversion.", foreground="#c62828")
            messagebox.showerror("Error", f"Failed to download/convert:\n{err_msg[:400]}")
        except Exception as e:
            status_label.config(text="Error occurred.", foreground="#c62828")
            messagebox.showerror("Error", str(e))
        finally:
            progress_bar.stop()
            btn_convert.config(state="normal")

    import threading
    threading.Thread(target=run, daemon=True).start()

def main():
    root = tk.Tk()
    root.title("YouTube to MP3 Converter")
    root.geometry("620x360")
    root.resizable(False, False)

    # Style
    style = ttk.Style()
    style.theme_use("clam")

    # Target default link
    default_url = "https://youtu.be/eShagnIgvZA?si=bJKHR-u97jbgojrd"
    default_output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    if not os.path.exists(default_output_dir):
        default_output_dir = os.path.dirname(os.path.abspath(__file__))

    output_dir_var = tk.StringVar(value=default_output_dir)

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    title_label = ttk.Label(frame, text="YouTube to MP3 Converter", font=("Segoe UI", 16, "bold"))
    title_label.pack(anchor="w", pady=(0, 15))

    # URL input
    url_label = ttk.Label(frame, text="YouTube Video / Song URL:", font=("Segoe UI", 10))
    url_label.pack(anchor="w", pady=(0, 5))

    url_entry = ttk.Entry(frame, font=("Segoe UI", 10), width=65)
    url_entry.insert(0, default_url)
    url_entry.pack(fill=tk.X, pady=(0, 15))

    # Output folder
    folder_label = ttk.Label(frame, text="Save To Folder:", font=("Segoe UI", 10))
    folder_label.pack(anchor="w", pady=(0, 5))

    folder_frame = ttk.Frame(frame)
    folder_frame.pack(fill=tk.X, pady=(0, 15))

    folder_entry = ttk.Entry(folder_frame, textvariable=output_dir_var, font=("Segoe UI", 9))
    folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))

    def choose_folder():
        folder = filedialog.askdirectory(initialdir=output_dir_var.get())
        if folder:
            output_dir_var.set(folder)

    browse_btn = ttk.Button(folder_frame, text="Browse...", command=choose_folder)
    browse_btn.pack(side=tk.RIGHT)

    # Progress bar
    progress_bar = ttk.Progressbar(frame, mode="indeterminate")
    progress_bar.pack(fill=tk.X, pady=(5, 10))

    # Status
    status_label = ttk.Label(frame, text="Ready", font=("Segoe UI", 9))
    status_label.pack(anchor="w", pady=(0, 15))

    # Action Button
    convert_btn = ttk.Button(
        frame,
        text="Convert & Download MP3",
        command=lambda: convert_url(url_entry.get(), output_dir_var.get(), status_label, progress_bar, convert_btn)
    )
    convert_btn.pack(ipady=5, fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    # If run with command line arguments: python app.py <url> [output_dir]
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        save_dir = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()
        print(f"Downloading & converting {target_url} to MP3 in {save_dir}...")
        cmd = [
            "yt-dlp",
            "-x",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "--output", os.path.join(save_dir, "%(title)s.%(ext)s"),
            target_url
        ]
        res = subprocess.run(cmd)
        sys.exit(res.returncode)
    else:
        main()
