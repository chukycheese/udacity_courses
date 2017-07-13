import webbrowser

# 9. Updating the Design for Class Movie
class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    """This class provieds a way to store movie related information"""

    # Lesson 7: 2. Class Variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # 5. Defining __init__
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration)

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Add a method: show_trailer()
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TVShow(Video):
    def __init__(self, season, episode, tv_station):
        Video.__init__(self, title, duration)

        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self)
