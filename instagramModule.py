# instagramModule.py
import instaloader


def downloadReel(instagram_url):
    try:
        # Create an Instaloader instance
        loader = instaloader.Instaloader()

        # Get the Instagram post details
        post = instaloader.Post.from_shortcode(loader.context, instagram_url.split("/")[-2])

        # Download the reel
        loader.download_post(post, target='reels')

        print("Reel downloaded successfully.")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # You can test the module by running it as a script
    link = input("Enter the Instagram reel URL: ")
    if "instagram.com" in link:
        downloadReel(link)
    else:
        print("The link is not an Instagram reel link.")

