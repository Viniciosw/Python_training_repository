# Importing the libraries
from pytube import YouTube

# Create a YouTube object with the desired video URL
video = YouTube('https://www.youtube.com/watch?v=qrO4YZeyl0I')

# Capturing the code (video language)
code = [code.code for code in video.captions]
code = code[-1]

# Capturing the information of the code and caption of the video
obj_subtitles = video.captions[code]

# Obtaining the JSON with the video caption information
obj_subtitles = obj_subtitles.json_captions

# Capturing the caption, start, and duration of the caption
subtitles = [[f'Lyrics: {sub_info['utf8']}, Start: {event['tStartMs']}, Duration: {event['dDurationMs']}'] for event in obj_subtitles['events'] for sub_info in event['segs']]

file_name = '01_subtitles.txt'

# Opening the file in write mode
with open(f'.\\results\\{file_name}', 'w', encoding = 'utf-8') as arq:

    # Write the items to the file, joining them with line breaks
    arq.write('\n'.join(map(lambda item: item[0], subtitles)))