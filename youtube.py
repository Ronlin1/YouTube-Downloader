# import youtube
from pytube import YouTube

# ask user input
link = input("\nPaste Video Link: ")
video = YouTube(link)

print("\n")
# video details
print("Title of the video, ", video.title)
print("Total Views: ", video.views)
print("Length: ", video.length , "seconds")

# stream details
stream = str(video.streams.filter(progressive=True))
# print(stream)
streamlist = stream.split(", ")
print("\nAll available Options: \n")\

# get tag details
for i in range(0, len(streamlist)):
    st = streamlist[i].split(" ")
    print(i+1,")", st[1], " and ", st[3], sep="")

tag = int(input("\nEnter the itag of the video: "))
load = video.streams.get_by_itag(tag)

# download
print("\nDownloading ......")
load.download()
print("\n Yay... download complete")
