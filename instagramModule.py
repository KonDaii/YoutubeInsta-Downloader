# instagramModule
import os
import instaloader
from tkinter import Toplevel, Label


def downloadReel(link, downloadFolder):
    # Create a folder if user does not specify
    if downloadFolder == "":
        folder_path = 'InstagramReels'
        os.makedirs(folder_path, exist_ok=True)
    else:
        folder_path = downloadFolder
    try:
        # Create an Instaloader instance
        loader = instaloader.Instaloader()

        # Get the Instagram post details
        post = instaloader.Post.from_shortcode(loader.context, link.split("/")[-2])

        # Download the reel
        loader.download_post(post,folder_path)
        show_download_complete_window("Instagram Reel Download Complete. You can now close this window.")
    except Exception as e:
        show_error_window(f"Instagram reel is unavailable. Double-check your link and try again.")


def show_download_complete_window(message):
    window = Toplevel()
    window.title("Download Complete")
    label = Label(window, text=message, bg="forest green")
    label.pack()


def show_error_window(error_message):
    window = Toplevel()
    window.title("Error")
    label = Label(window, text=error_message, bg="red")
    label.pack()
