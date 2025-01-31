# Youtube Music player
This program streams a youtube playlist from url specified in the target file.

# How to use
you would need to create a cookies.txt file using yt-dlp. [Here is how to extract your cookies.](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp)

You can play your song by typing in:
```
python main.py <song name>
```

and your song of choice will be played.

If you did not provide any song name, your specified playlists will be played.

to predefine your playlists, create a file plists.txt and input this into it:

```
PLAYLIST <Your playlist URL>
...
```

place both files into the program source directory. Multiple playlists can be played.