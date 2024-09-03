List_of_all = []

class Movie:
    def __init__(self, title, year, genre, recreate):
        self.title = title
        self.year = year
        self.genre = genre
        self.recreate = recreate
        List_of_all.append(self)

        self.recreate = 0
    
    def __str__(self):
        return f'{self.title} ({self.year})'
    
    def play(self, step=1):
        self.recreate += step

    def __repr__(self):
        return f"Movie(title={self.title} year={self.year} genre={self.genre} recreate={self.recreate})"
    
    

class Series:
    def __init__(self, title, year, genre, episode, season, recreate):
        self.title = title
        self.year = year
        self.genre = genre
        self.episode = episode
        self.season = season
        self.recreate = recreate
        List_of_all.append(self)

    def play(self, step=1):
        self.recreate += step

    def __str__(self):
        return f'{self.title} S{self.season}E{self.episode}'
    
    def __repr__(self):
        return f"Series(title={self.title} year={self.year} genre={self.genre} episode={self.episode} season={self.season} recreate={self.recreate})"
    
Indiana_movie= Movie(title = 'Indiana', year = '2024', genre = 'documentary', recreate = 0)
print(Indiana_movie)

Bad_Kid = Series(title='Bad Kid', year='2024', genre='comedy', episode='01', season='01', recreate=0)
print(Bad_Kid)
print(Indiana_movie.recreate)
print(List_of_all)
Indiana_movie.play()
print(Indiana_movie.recreate)
Bad_Kid.play()
print(Bad_Kid.recreate)