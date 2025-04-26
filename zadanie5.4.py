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
    def __init__(self, title, year, genre, director, plays=0):
        super().__init__(title, year, genre, plays)
        self.director = director

    def __str__(self):
        return f"{self.title} ({self.year}), Directed by {self.director}"


class Series(Media):
    def __init__(self, title, year, genre, season, episode, plays=0):
        super().__init__(title, year, genre, plays)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"


def get_movies(library):
    return sorted(
        [item for item in library if isinstance(item, Movie)],
        key=lambda m: m.title
    )


def get_series(library):
    return sorted(
        [item for item in library if isinstance(item, Series)],
        key=lambda s: s.title
    )


def search(library, title):
    return [item for item in library if title.lower() in item.title.lower()]


def generate_views(library):
    item = random.choice(library)
    views = random.randint(1, 100)
    item.play(views)


def generate_views_multiple(library, times=10):
    for _ in range(times):
        generate_views(library)


def top_titles(library, n=3, content_type=None):
    if content_type == "movie":
        items = get_movies(library)
    elif content_type == "series":
        items = get_series(library)
    else:
        items = library
    return sorted(items, key=lambda x: x.plays, reverse=True)[:n]


if __name__ == "__main__":
    print("Biblioteka filmów.\n")

    library = [
        Movie("Pulp Fiction", 1994, "Crime", "Quentin Tarantino"),
        Movie("Inception", 2010, "Sci-Fi", "Christopher Nolan"),
        Movie("The Godfather", 1972, "Crime", "Francis Ford Coppola"),
        Series("The Simpsons", 1989, "Animation", 1, 5),
        Series("Breaking Bad", 2008, "Drama", 2, 3),
        Series("Stranger Things", 2016, "Horror", 3, 1),
    ]

    generate_views_multiple(library)

    print(f"Najpopularniejsze filmy i seriale dnia {datetime.now().strftime('%d.%m.%Y')}:\n")
    for item in top_titles(library, 3):
        print(f"{item} - {item.plays} odtworzeń")
