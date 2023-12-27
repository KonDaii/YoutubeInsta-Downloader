import instaloader
from tkinter import Toplevel, Label


def downloadReel(instagram_url):
    try:
        # Create an Instaloader instance
        loader = instaloader.Instaloader()

        # Get the Instagram post details
        post = instaloader.Post.from_shortcode(loader.context, instagram_url.split("/")[-2])

        # Download the reel
<<<<<<< Updated upstream
        loader.download_post(post, target='reels')

        print("Reel downloaded successfully.")
=======
        loader.download_post(post, target='InstagramReels')
        print("Instagram reel has downloaded successfully.")
        show_download_complete_window("Instagram Reel Download Complete")
>>>>>>> Stashed changes
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")


<<<<<<< Updated upstream
if __name__ == "__main__":
    # You can test the module by running it as a script
    link = input("Enter the Instagram reel URL: ")
    if "instagram.com" in link:
        downloadReel(link)
    else:
        print("The link is not an Instagram reel link.")

=======
def show_download_complete_window(message):
    window = Toplevel()
    window.title("Download Complete")
    label = Label(window, text=message)
    label.pack()
>>>>>>> Stashed changes
