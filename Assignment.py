import os
import random
import pygame
from tkinter import Tk, Button, Label, messagebox, filedialog


# Function to play a random song from the directory
def play_random_song():
    if len(songs) == 0:
        messagebox.showinfo("Random Song Player", "All songs have been played.")
        return

    # Randomly select a song from the list
    song = random.choice(songs)
    songs.remove(song)

    try:
        # Play the selected song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        song_label.config(text="Now playing: " + os.path.basename(song))
    except pygame.error:
        messagebox.showerror("Random Song Player", "Failed to load the song.")


# Function to pause the currently playing song
def pause_song():
    pygame.mixer.music.pause()


# Function to resume the paused song
def resume_song():
    pygame.mixer.music.unpause()


# Function to skip to the next song
def skip_song():
    pygame.mixer.music.stop()
    play_random_song()


# Function to browse and select a new songs directory
def select_songs_directory():
    global songs_dir, songs

    new_songs_dir = filedialog.askdirectory()
    if new_songs_dir:
        songs_dir = new_songs_dir
        songs = [os.path.join(songs_dir, file) for file in os.listdir(songs_dir) if file.endswith(".mp3")]
        messagebox.showinfo("Random Song Player", "New songs directory selected.")


# Initialize Pygame mixer
pygame.mixer.init()

# Create the main window
window = Tk()
window.title("Random Song Player")

# Create buttons
play_button = Button(window, text="Play", command=play_random_song)
pause_button = Button(window, text="Pause", command=pause_song)
resume_button = Button(window, text="Resume", command=resume_song)
skip_button = Button(window, text="Skip", command=skip_song)
browse_button = Button(window, text="Select Songs Directory", command=select_songs_directory)

# Create a label to display the currently playing song
song_label = Label(window, text="")

# Add buttons and label to the window
play_button.pack(pady=10)
pause_button.pack(pady=5)
resume_button.pack(pady=5)
skip_button.pack(pady=5)
browse_button.pack(pady=10)
song_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
