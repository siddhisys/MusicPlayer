import os
import shutil
from player import play_song

class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.current = None  

    def add_song(self, song_path, copy_into_library=True, library_folder="songs"):
        final_path = song_path

        if copy_into_library:
            os.makedirs(library_folder, exist_ok=True)
            if os.path.isabs(song_path):
                base = os.path.basename(song_path)
                final_path = os.path.join(library_folder, base)
                if not os.path.exists(final_path):
                    shutil.copy2(song_path, final_path)
            else:
                
                if os.path.dirname(song_path):
                    base = os.path.basename(song_path)
                    final_path = os.path.join(library_folder, base)
                    if not os.path.exists(final_path):
                        shutil.copy2(song_path, final_path)

        # append to linked list
        new_node = Node(final_path)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if not self.head:
            print("⚠ Playlist is empty")
            return

        print("\n🎶 Playlist:")
        temp = self.head
        idx = 1
        while temp:
            filename = os.path.basename(temp.data)
            name_without_ext = filename.replace(".mp3", "")
            if " - " in name_without_ext:
                artist, title = name_without_ext.split(" - ", 1)
            else:
                artist, title = "Unknown", name_without_ext
            marker = " (current)" if self.current is temp else ""
            print(f"{idx}. {artist} : {title}{marker}")
            temp = temp.next
            idx += 1

    def next_song(self):
        """
        Move to the next song in the playlist (or start at head) and return its path.
        Returns None if there is no next song.
        """
        if self.head is None:
            print("⚠ Playlist empty, nothing to play")
            return None

        if self.current is None:
            self.current = self.head
        else:
            self.current = self.current.next

        if self.current is None:
            print("ℹ️ Reached end of playlist.")
            return None
        return self.current.data

    def play_current(self):
        """Play the current song (does not advance). Starts at head if current is None."""
        if self.head is None:
            print("⚠ Playlist empty, nothing to play")
            return None
        if self.current is None:
            self.current = self.head
        play_song(self.current.data)
        return self.current.data

    def remove_song(self, song_path):
        temp = self.head
        prev = None
        while temp:
            if temp.data == song_path or os.path.basename(temp.data) == os.path.basename(song_path):
                
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                
                if self.current is temp:
                    self.current = temp.next
                print(f"🗑 Removed {os.path.basename(temp.data)} from playlist")
                return
            prev = temp
            temp = temp.next
        print(f"❌ {os.path.basename(song_path)} not found in playlist")

    def load_songs(self, folder="songs"):
        if not os.path.exists(folder):
            print(f"⚠ Folder '{folder}' does not exist")
            return
        for file in os.listdir(folder):
            if file.lower().endswith(".mp3"):
                self.add_song(os.path.join(folder, file))
