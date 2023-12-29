from pytube import YouTube
import os
from tkinter import Toplevel, Label


def DownloadYoutubeVideo(link):
    try:
        youtubeVideo = YouTube(link)
        video = youtubeVideo.streams.get_highest_resolution()

        # Create a folder if it doesn't exist
        folder_path = 'YoutubeVideo'
        os.makedirs(folder_path, exist_ok=True)

        # Download video to the folder
        video.download(output_path=folder_path)

    except Exception as e:
        show_error_window(f"Video is unavailable. Double check your link and try again.")
    else:
        print("Youtube video download has completed successfully")
        show_download_complete_window("Youtube Video Download Complete")


def DownloadYoutubeAudio(link):
    try:
        youtubeAudio = YouTube(link)
        audio = youtubeAudio.streams.get_audio_only()

        # Create a folder if it doesn't exist
        folder_path = 'YoutubeAudio'
        os.makedirs(folder_path, exist_ok=True)

        # Download audio to the folder
        audio.download(output_path=folder_path)

    except Exception as e:
        show_error_window(f"Audio is unavailable. Double check your link and try again.")
    else:
        print("Youtube audio download has completed successfully")
        show_download_complete_window("Youtube Audio Download Complete")


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
