# Author: Danny Lao
# Date: Nov 17, 2023
# YouTubeInstagram Downloader uses the pytube library to install YouTube videos and audio for personal use.
# It was made as a personal tool to avoid having to use websites for each individual site you want to download from.

from tkinter import *
from tkinter import simpledialog, filedialog, messagebox

import instagramModule
import twitterModule
import youtubeModule


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
    # adding a label to the root window
    lbl = Label(root, text="Enter the Instagram/YouTube video URL:")
    lbl.grid(row=0, column=0, columnspan=2, pady=10)  # Center the label
    link_label = Label(root,
                       text="Video Link:",
                       bg="turquoise",
                       pady=5,
                       padx=9)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)
    # adding Entry Field
    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    Download_B = Button(root,
                        text="Download Video",
                        command=Download,
                        width=20,
                        bg="bisque",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)

    destination_label = Label(root,
                              text="Destination:",
                              bg="turquoise",
                              pady=5,
                              padx=9)
    destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 14")
    root.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)


def Download():
    link = video_Link.get()
    downloadFolder = download_Path.get()
    if "youtube.com" in link:
        video_or_audio = simpledialog.askstring("Input",
                                                "Do you want video or audio only? (Enter 'video' or 'audio')").lower()
        if video_or_audio == "video":
            youtubeModule.downloadYoutubeVideo(link, downloadFolder)
        elif video_or_audio == "audio":
            youtubeModule.downloadYoutubeAudio(link, downloadFolder)
        else:
            messagebox.showinfo("Please select either video or audio.")
    elif "instagram.com" in link:
        instagramModule.downloadReel(link, downloadFolder)
    elif "x.com" in link or "twitter.com" in link:
        twitterModule.downloadTwitterVid(link, downloadFolder)
    else:
        messagebox.showinfo("The link is not a YouTube/Instagram/X link. Try again.")


# Defining Browse() to select a
# destination folder to save the video
# does not work with InstagramModule for now
def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)


# Defining Download() to download the video
# create root window
root = Tk()

# root window title and dimension
root.title("YoutubeInsta Downloader")
# Set geometry(widthxheight)
root.geometry("520x280")
root.resizable(False, False)
# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Execute Tkinter
root.mainloop()
