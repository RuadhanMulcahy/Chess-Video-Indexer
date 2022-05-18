from pytube import YouTube

def download_youtube_video(url):
    video = YouTube(url)
    video.streams.filter(res='720p', file_extension='mp4', fps=30).first().download(filename='./files/videos/0.mp4')

# download_youtube_video('https://www.youtube.com/watch?v=0S2MGVp_tP0')
# download_youtube_video('https://www.youtube.com/watch?v=2QWiX0tkkW4')