import random
from datetime import datetime


class Movie:
    def __init__(self, title, year, genre, director, plays=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director
        self.plays = plays

    def play(self, count=1):
        self.plays += count

    def __str__(self):
        return f"{self.title} ({self.year})"


class Series(Movie):
    def __init__(self, title, year, genre, season, episode, director, plays=0):
        super().__init__(title, year, genre, director, plays)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"

def get_items_by_kind(library, kind_value):
    return sorted(
        [item for item in library if getattr(item, "kind", None) == kind_value],
        key=lambda x: x.title
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
        items = get_items_by_kind(library, content_type)
    elif content_type == "series":
        items = get_items_by_kind(library, content_type)
    else:
        items = library
    return sorted(items, key=lambda x: x.plays, reverse=True)[:n]




def add_season(library, title, year, genre, season, episodes_count, director):
    for ep in range(1, episodes_count + 1):
        library.append(Series(title, year, genre, season, ep, director))

def count_episodes(library, series_title):
    return len([item for item in library if isinstance(item, Series) and item.title == series_title])

if __name__ == "__main__":
    print("Biblioteka filmów.\n")

    library = [
        Movie("Pulp Fiction", 1994, "Crime", "Quentin Tarantino"),
        Movie("Inception", 2010, "Sci-Fi", "Christopher Nolan"),
        Movie("The Godfather", 1972, "Crime", "Francis Ford Coppola"),
        Series("The Simpsons", 1989, "Animation", 1, 5, "James L. Brooks"),
        Series("Breaking Bad", 2008, "Drama", 2, 3, "Michelle MacLaren"),
        Series("Stranger Things", 2016, "Horror", 3, 1, "Matt Duffer & Ross Duffer"),
    ]

    add_season(library, "The Office", 2005, "Comedy", season=1, episodes_count=6, director="Greg Daniels")

    generate_views_multiple(library)

    today = datetime.now().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {today}:\n")

    for item in top_titles(library, 3):
        print(f"{item} – {item.plays} odtworzeń")
