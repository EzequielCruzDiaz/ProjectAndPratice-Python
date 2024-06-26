import pytube

link = input("https://www.youtube.com/watch?v=aAJNm0ApPjk&list=RDaAJNm0ApPjk&start_radio=1")
yt= pytube.YouTube(link)
yt.streams.first().download()
print("Downloaded", link)

