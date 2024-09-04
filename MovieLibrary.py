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

Oval_movie = Movie(title='Oval', year='2024', genre='action', recreate=0)

Bad_Kid = Series(title='Bad Kid', year='2024', genre='comedy', episode='01', season='01', recreate=0)
print(Bad_Kid)

#print(Indiana_movie.recreate)
#print(List_of_all)
Indiana_movie.play()
#print(Indiana_movie.recreate)
Bad_Kid.play()
#print(Bad_Kid.recreate)
#print(type(Indiana_movie))
 
list_get_movies = [] 
def get_movies():
    for item in List_of_all:
        if isinstance(item, Movie):
            list_get_movies.append(item)
get_movies()
print(list_get_movies)
list_of_movies = sorted(list_get_movies, key=lambda recorded: recorded.title)
print(list_of_movies) 

list_get_series = [] 
def get_series():
    for item in List_of_all:
        if isinstance(item, Series):
            list_get_series.append(item)
get_series()
print(list_get_series)
list_of_series = sorted(list_get_series, key=lambda recorded: recorded.title)
print(list_of_series)

list_of_search = []      
def search():
    searched_title = input("Wpisz tytuł filmu/serialu którego szukasz:")
    for item in List_of_all:
        if item.title == searched_title:
            print(item)
            return list_of_search.append(item)
    if len(list_of_search)==0:
        print("Brak takiego tytułu w bazie")   
search()

import random
def generate_views():
    random_item = random.choice(List_of_all)
    random_item.recreate = random.randrange(1,101)
    print(random_item)
    print(random_item.recreate)
generate_views()

def run_10_generate_views():
    for i in range(10):
        generate_views()
run_10_generate_views()

list_of_top = sorted(List_of_all, key=lambda recorded2: recorded2.recreate, reverse=1)
#print(list_of_top)

def top_titles():
    nof = int(input("Podaj ilość do wyświetlenia z listy top"))
    print(list_of_top[0:nof])

top_titles()
"""
def top_titles2():
    nof = int(input("Podaj ilość do wyświetlenia z listy top"))
    for item in list_of_top[0:nof]:
        print(item.title)
top_titles2()

"""