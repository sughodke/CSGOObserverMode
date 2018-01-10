from pytube import YouTube 

def get_stream_link(yt_link):
    y = YouTube(yt_link)
    q = y.streams.filter(res="1080p", mime_type="video/mp4")

    return q.first().url

if __name__ == "__main__":
    import sys

    print(get_stream_link(sys.argv[1]))

