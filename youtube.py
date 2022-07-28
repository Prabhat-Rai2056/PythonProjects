from pytube import YouTube
url=input("Enter the url of video:")
path="E:\youtube_video"
YouTube(url).streams.get_highest_resolution().download(path)
print("Downloaded successfully")
