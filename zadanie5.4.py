import random
from datetime import datetime


class Media:
    def __init__(self, title, year, genre, plays=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays

    def play(self, count=1):
        self.plays += count

    def __str__(self):
        return f"{self.title} ({self.year})"


class Movie(Media):
    pass


class Series(Media):
    def __init__(self, title, year, genre, season, episode, plays=0):
        super().__init__(title, year, genre, plays)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"


library = []


def get_movies():
    return sorted([item for item in library if isinstance(item, Movie)], key=lambda m: m.title)


def get_series():
    return sorted([item for item in library if isinstance(item, Series)], key=lambda s: s.title)


def search(title):
    return [item for item in library if title.lower() in item.title.lower()]


def generate_views():
    item = random.choice(library)
    views = random.randint(1, 100)
    item.play(views)


def generate_views_multiple(times=10):
    for _ in range(times):
        generate_views()


def top_titles(n=3, content_type=None):
    if content_type == "movie":
        items = get_movies()
    elif content_type == "series":
        items = get_series()
    else:
        items = library
    return sorted(items, key=lambda x: x.plays, reverse=True)[:n]


if __name__ == "__main__":
    print("Biblioteka filmów.\n")

    library.extend([
        Movie("Pulp Fiction", 1994, "Crime"),
        Movie("Inception", 2010, "Sci-Fi"),
        Movie("The Godfather", 1972, "Crime"),
        Series("The Simpsons", 1989, "Animation", 1, 5),
        Series("Breaking Bad", 2008, "Drama", 2, 3),
        Series("Stranger Things", 2016, "Horror", 3, 1),
    ])

    generate_views_multiple()

    print(f"Najpopularniejsze filmy i seriale dnia {datetime.now().strftime('%d.%m.%Y')}:\n")
    for item in top_titles(3):
        print(f"{item} - {item.plays} odtworzeń")
