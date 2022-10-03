from asyncio import streams
from pytube import Youtube
link = input('Enter the Youtube link: ')
dn = pytube.Youtube(link)
dn.streams.first().download()
print('Your video has been downloaded', link)