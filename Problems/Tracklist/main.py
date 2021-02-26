def tracklist(**kwargs):
    for k, v in kwargs.items():
        print(k)
        for album, track in v.items():
            print(f"ALBUM: {album} TRACK: {track}")
