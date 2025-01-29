import audio
import sys
import os

def get_plist_urls():
    plist_l = []
    with open(f"{os.path.dirname(__file__)}/plists.txt", "r") as f:
        data = f.readlines()
        for line in data:
            parse = line.split(' ')
            if f"{parse[0]}" == "PLAYLIST":
                plist_l.append(f"{parse[1]}")
        
    return plist_l

def main():
    try:
        plist = get_plist_urls()
        for i in range(len(plist)):
            p = audio.playlist(plist[i])
            p.play_items()
    except KeyboardInterrupt:
        print("Interrupted")
    except Exception as e:
        print(f"Exception Occurred: {e}")

main()