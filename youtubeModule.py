from pytube import YouTube
<<<<<<< Updated upstream
=======
import os
from tkinter import Toplevel, Label


>>>>>>> Stashed changes
def DownloadYoutubeVideo(link):
    youtubeVideo = YouTube(link)
    video = youtubeVideo.streams.get_highest_resolution()
    try:
<<<<<<< Updated upstream
        video.download()
    except:
        print("An error has occurred")
    print("Video download is completed successfully")
=======
        # Create a folder if it doesn't exist
        folder_path = 'YoutubeVideo'
        os.makedirs(folder_path, exist_ok=True)

        # Download video to the folder
        video.download(output_path=folder_path)
    except Exception as e:
        print(f"An error has occurred: {e}")
    else:
        print("Youtube video download has completed successfully")
        show_download_complete_window("Youtube Video Download Complete")
>>>>>>> Stashed changes


def DownloadYoutubeAudio(link):
    youtubeAudio = YouTube(link)
    audio = youtubeAudio.streams.get_audio_only()
    try:
<<<<<<< Updated upstream
        audio.download()
    except:
        print("An error has occurred")
    print("Audio download is completed successfully")
=======
        # Create a folder if it doesn't exist
        folder_path = 'YoutubeAudio'
        os.makedirs(folder_path, exist_ok=True)

        # Download audio to the folder
        audio.download(output_path=folder_path)
    except Exception as e:
        print(f"An error has occurred: {e}")
    else:
        print("Youtube audio download has completed successfully")
        show_download_complete_window("Youtube Audio Download Complete")


def show_download_complete_window(message):
    window = Toplevel()
    window.title("Download Complete")
    label = Label(window, text=message)
    label.pack()
>>>>>>> Stashed changes
