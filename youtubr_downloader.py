import pafy
import youtube_dl
link = "https://youtu.be/b80a8XKX6ws"
my_video = pafy.new(link)
print(my_video.title)
print(my_video.duration)
print(my_video.rating)
print(my_video.author)
print(my_video.length)
best = my_video.getbest()
print(best.resolution, best.extension)
best.download()

