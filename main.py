from playlist import Playlist
from stackqueue import Stack, Queue, PriorityQueue
from player import stop_song, pause_song, resume_song, play_song
import os

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def resolve_song_path(song_input, library_folder="songs"):

    # If it's already a full path that exists, return it
    if os.path.exists(song_input):
        return song_input
    
    # Try adding .mp3 extension
    if not song_input.lower().endswith('.mp3'):
        song_with_ext = song_input + '.mp3'
    else:
        song_with_ext = song_input
    
    # Check if it exists as is (with .mp3)
    if os.path.exists(song_with_ext):
        return song_with_ext
    
    # Try in the library folder
    library_path = os.path.join(library_folder, song_with_ext)
    if os.path.exists(library_path):
        return library_path
    
    # Try without extension in library folder (in case user added .mp3 twice)
    if song_input.lower().endswith('.mp3'):
        base_name = song_input[:-4]  # remove .mp3
        library_path_base = os.path.join(library_folder, base_name + '.mp3')
        if os.path.exists(library_path_base):
            return library_path_base
    
    return None

def main():
    playlist = Playlist()
    listening_history = Stack()
    play_next_queue = Queue()
    party_mode_queue = PriorityQueue()

    # Load library
    playlist.load_songs("songs")

    while True:
        print("\n=== 🎵 Music Playlist Manager 🎵 ===")
        print("1. Show all songs")
        print("2. Add a song to playlist")
        print("3. Remove a song from playlist")
        print("4. Play next song")
        print("5. View listening history")
        print("6. Queue a song (Play Next)")
        print("7. Party Mode (Priority Queue)")
        print("8. Shuffle playlist (Recursion demo)")
        print("9. Stop music")
        print("10. Pause music")
        print("11. Resume music")
        print("12. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            playlist.display()

        elif choice == '2':
            song = input("Enter song filename (with path if outside 'songs/'): ").strip().strip('"')

            playlist.add_song(song)
            print("✅ Song added to playlist.")

        elif choice == '3':
            song = input("Enter exact song path/name to remove: ").strip().strip('"')
            playlist.remove_song(song)

        elif choice == '4':
            # Priority: Party Mode > Play-Next Queue > normal playlist order
            to_play = None

            if not party_mode_queue.is_empty():
                to_play = party_mode_queue.dequeue()
            elif not play_next_queue.is_empty():
                to_play = play_next_queue.dequeue()
            else:
                # Advance through the playlist
                to_play = playlist.next_song()

            if to_play:
                # Try to resolve the path
                resolved_path = resolve_song_path(to_play)
                if resolved_path:
                    play_song(resolved_path)
                    listening_history.push(os.path.basename(resolved_path))
                else:
                    print(f"❌ Could not find song: {to_play}")
                    print("💡 Make sure the song exists in the 'songs' folder or provide the full path")
            else:
                print("⚠ Nothing to play (queues empty and/or end of playlist).")
        elif choice == '5':
            print("🕑 Listening History:")
            listening_history.display()

        elif choice == '6':
            song = input("Enter song name (e.g., '1000 Tears') or full path: ").strip().strip('"')
            # Validate that the song exists before adding to queue
            resolved_path = resolve_song_path(song)
            if resolved_path:
                play_next_queue.enqueue(resolved_path)  # Store the resolved path
                print("🎵 Song queued for next play!")
                play_next_queue.display()
            else:
                print(f"❌ Could not find song: {song}")
                print("💡 Make sure the song exists in the 'songs' folder or provide the full path")

        elif choice == '7':
            song = input("Enter song name or path for Party Mode: ").strip().strip('"')
            resolved_path = resolve_song_path(song)
            if resolved_path:
                priority = int(input("Enter priority (higher = plays first): ").strip())
                party_mode_queue.enqueue(resolved_path, priority)  # Store the resolved path
                print("🎉 Added to Party Mode!")
                party_mode_queue.display()
            else:
                print(f"❌ Could not find song: {song}")
                print("💡 Make sure the song exists in the 'songs' folder or provide the full path")

        elif choice == '8':
            n = int(input("Enter number for factorial shuffle demo: "))
            print(f"Factorial of {n} = {factorial(n)}")

        elif choice == '9':
            stop_song()

        elif choice == '10':
            pause_song()

        elif choice == '11':
            resume_song()

        elif choice == '12':
            print("👋 Exiting...")
            break

        else:
            print("⚠ Invalid choice, try again")

if __name__ == "__main__":
    main()