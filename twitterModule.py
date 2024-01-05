# Placeholder file for future twitter functionality.
# Twitter functionality not currently added.
import os
from tkinter import Toplevel, Label


def downloadTwitterVid(link):
    try:
        # insert code

        # Create a folder if it doesn't exist
        folder_path = 'TwitterVideos'
        os.makedirs(folder_path, exist_ok=True)

        # Download video to the folder
    except Exception as e:
        show_error_window(f"Twitter video is unavailable. Double check your link and try again.")
    else:
        show_download_complete_window("Twitter function not available yet")


def show_download_complete_window(message):
    window = Toplevel()
    window.title("Download Complete")
    label = Label(window, text=message)
    label.pack()


def show_error_window(error_message):
    window = Toplevel()
    window.title("Error")
    label = Label(window, text=error_message)
    label.pack()
