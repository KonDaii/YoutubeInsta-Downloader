from pytube import YouTube
import os
def DownloadYoutubeVideo(link):
    youtubeVideo = YouTube(link)
    video = youtubeVideo.streams.get_highest_resolution()
    try:
        # Create a folder if it doesn't exist
        folder_path = 'YoutubeVideo'
        os.makedirs(folder_path, exist_ok=True)

        # Download video to the folder
        video.download(output_path=folder_path)
    except Exception as e:
        print(f"An error has occurred: {e}")
    else:
        print("Youtube video download has completed successfully")


def DownloadYoutubeAudio(link):
    youtubeAudio = YouTube(link)
    audio = youtubeAudio.streams.get_audio_only()
    try:
        # Create a folder if it doesn't exist
        folder_path = 'YoutubeAudio'
        os.makedirs(folder_path, exist_ok=True)

        # Download audio to the folder
        audio.download(output_path=folder_path)
    except Exception as e:
        print(f"An error has occurred: {e}")
    else:
        print("Youtube audio download has completed successfully")