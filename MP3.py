from Item import Item

class MP3(Item):


    Duration = 0
    Artist = ''


    def playExtract(self):
        print(f"Playing a {self.Duration} second extract of {self.Title} by {self.Artist}.")

    def download(self):
        print(f"Downloading {self.Title} by {self.Artist}...")
        print("Download Complete.")