import instaloader
from tkinter import Toplevel, Label


def downloadReel(instagram_url):
    try:
        # Create an Instaloader instance
        loader = instaloader.Instaloader()

        # Get the Instagram post details
        post = instaloader.Post.from_shortcode(loader.context, instagram_url.split("/")[-2])

        # Download the reel
        loader.download_post(post, target='instagramReels')
        show_download_complete_window("Instagram Reel Download Complete. You can now close this window.")
    except Exception as e:
        show_error_window(f"Instagram reel is unavailable. Double check your link and try again.")


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
