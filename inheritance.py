import time 

class MusicItem():
    def __init__(self, title, artist, release_year, duration, popularity):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.duration = duration
        self.popularity = popularity

    def changeReleases(self,release_year):
        self.release_year = release_year
    
    def changeDuration(self,duration):
        self.duration = duration

    def changePopularity(self,popularity):
        self.popularity = popularity

    def displayData(self):
        print("""----------------------------------------------------------------------------\nSong Name     Artist          Release Date        Duration        Popularity\n""")
        print(f"{self.title}    {self.artist}       {self.release_year}     {self.duration}     {self.popularity}\n")
        print("----------------------------------------------------------------------------")

class Song(MusicItem):
    def __init__(self, title, artist, release_year, duration, popularity, genre, explicit):
        super().__init__(title, artist, release_year, duration, popularity)
        self.genre = genre
        self.explicit = explicit

    def displaySongData(self):
        print("""----------------------------------------------------------------------------\nSong Name     Artist          Release Date        Duration        Popularity     Genre       Explicit\n""")
        print(f"{self.title}    {self.artist}       {self.release_year}     {self.duration}     {self.popularity}       {self.genre}        {self.explicit}\n")
        print("----------------------------------------------------------------------------")

    def changeSongGenre(self,genre):
        self.genre = genre
        
    def changeSongExplicit(self,explicit):
        if(explicit == 'y'):
            explicitValue=1
        else:
            explicitValue=0
        self.explicit = explicitValue

perfect=Song("Perfect","Ed Sheeran",2018,3.15,72.0,"Pop",1)
perfect1=MusicItem("Perfect","Ed Sheeran",2018,3.15,72.0)
perfect.displayData()

def displaySong():
    perfect.displaySongData()
    perfect1.displayData()

def changeDuration():
    duration=input("Enter new duration : ")
    perfect.changeDuration(duration)

def changeReleases():
    releases=input("Enter new release date : ")
    perfect.changeReleases(releases)
    perfect.displaySongData()

def changePopularity():
    popularity=input("Enter new popularity : ")
    perfect.changePopularity(popularity)
    perfect.displaySongData()

def changeexplicit():
    explicit=input("Enter new explicit mode (y/n): ").lower()[0]
    perfect.changeSongExplicit(explicit)
    perfect.displaySongData()    

def changeGenre():
    explicit=input("Enter new genre: ").lower()
    perfect.changeSongGenre(explicit)
    perfect.displaySongData()

def menu():
    while True:
        print("\nMenu:")
        print("1. Display Song ")
        print("2. Change Duration")
        print("3. Change Releases")
        print("4. Change Genre")
        print("5. Change Popularity")
        print("6. Change Explicit")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            displaySong()
            perfect.displaySongData()
        elif choice == "2":
            changeDuration()
            perfect.displaySongData()
        elif choice == "3":
            changeReleases()
            perfect.displaySongData()
        elif choice == "4":
            changeGenre()
            perfect1.displayData()
        elif choice == "5":
            changePopularity()
            perfect.displaySongData()
        elif choice == "6":
            changeexplicit()
            perfect1.displayData()    
        elif choice == "7":
            time.sleep(1)
            print("Thank You..")
            for i in range(0,2):
              time.sleep(1)
              print("Bye")
            break
        else:
            print("Invalid choice! Please select a valid option i.e. -> (1/2).")



if __name__ == '__main__':
    menu()