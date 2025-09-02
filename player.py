import os
import pygame

pygame.mixer.init()

def play_song(filename):
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        song_name = os.path.basename(filename).replace(".mp3", "")
        if " - " in song_name:
            artist, title = song_name.split(" - ", 1)
        else:
            artist, title = "Unknown", song_name
        print(f"▶ Now playing: {artist} : {title}")
    except Exception as e:
        print(f"Error playing {filename}: {e}")

def stop_song():
    pygame.mixer.music.stop()
    print("⏹ Music stopped")

def pause_song():
    pygame.mixer.music.pause()
    print("⏸ Music paused")

def resume_song():
    pygame.mixer.music.unpause()
    print("▶ Music resumed")
