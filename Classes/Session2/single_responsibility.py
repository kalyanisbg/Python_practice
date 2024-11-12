class Album:
    def __init__(self, name, artist, songs) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs
    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, song):
        self.songs.remove(song)
