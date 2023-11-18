from pytube import YouTube
def DownloadYoutubeVideo(link):
    youtubeVideo = YouTube(link)
    video = youtubeVideo.streams.get_highest_resolution()
    try:
        video.download()
    except:
        print("An error has occurred")
    print("Video download is completed successfully")


def DownloadYoutubeAudio(link):
    youtubeAudio = YouTube(link)
    audio = youtubeAudio.streams.get_audio_only()
    try:
        audio.download()
    except:
        print("An error has occurred")
    print("Audio download is completed successfully")