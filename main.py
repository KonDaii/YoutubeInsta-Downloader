# Author: Danny Lao
# Date: Nov 17, 2023
# YouTubeInstagram Downloader uses the pytube library to install YouTube videos and audio for personal use.
# It was made as a personal tool to avoid having to use websites for each individual site you want to download from.
import instagramModule
import youtubeModule


def main():
    link = input("Enter the Instagram/YouTube video URL: ")
    if "youtube.com" in link:
        print("Do you want video or audio only? ")
        videoOrAudio = input().lower()  # Convert the input to lowercase for case-insensitive comparison
        if videoOrAudio == "video":
            youtubeModule.DownloadYoutubeVideo(link)
        elif videoOrAudio == "audio":
            youtubeModule.DownloadYoutubeAudio(link)
        else:
            print("Please select either video or audio.")
    elif "instagram.com" in link:
        instagramModule.downloadReel(link)
    else:
        print("The link is not a YouTube/Instagram link")


main()
