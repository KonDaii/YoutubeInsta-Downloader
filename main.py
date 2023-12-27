# Author: Danny Lao
# Date: Nov 17, 2023
# YouTubeInstagram Downloader uses the pytube library to install YouTube videos and audio for personal use.
# It was made as a personal tool to avoid having to use websites for each individual site you want to download from.

from tkinter import *
from tkinter import simpledialog

import instagramModule
import youtubeModule


def download_video_or_audio():
    link = txt.get()
    if "youtube.com" in link:
        video_or_audio = simpledialog.askstring("Input",
                                                "Do you want video or audio only? (Enter 'video' or 'audio')").lower()
        if video_or_audio == "video":
            youtubeModule.DownloadYoutubeVideo(link)
        elif video_or_audio == "audio":
            youtubeModule.DownloadYoutubeAudio(link)
        else:
            lbl.configure(text="Please select either video or audio.")
    elif "instagram.com" in link:
        instagramModule.downloadReel(link)
    else:
        lbl.configure(text="The link is not a YouTube/Instagram link")


# create root window
root = Tk()

# root window title and dimension
root.title("YoutubeInsta Downloader")
# Set geometry(widthxheight)
root.geometry('300x200')

# adding a label to the root window
lbl = Label(root, text="Enter the Instagram/YouTube video URL:")
lbl.grid(row=0, column=0, columnspan=2, pady=10)  # Center the label

# adding Entry Field
txt = Entry(root, width=50)
txt.grid(row=1, column=0, columnspan=2, pady=5)  # Center the entry field

# button widget with red color text inside
btn = Button(root, text="Download", fg="red", command=download_video_or_audio)
# Set Button Grid
btn.grid(row=2, column=0, columnspan=2, pady=10)  # Center the button

# Execute Tkinter
root.mainloop()
