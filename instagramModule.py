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
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")


def show_download_complete_window(message):
    window = Toplevel()
    window.title("Download Complete")
    label = Label(window, text=message)
    label.pack()
