import webbrowser

class Movie():
    # Lesson 7: 2. Class Variables
    valid_ratings = ["G", "PG", "PG-13" "R"]
    
    # 5. Defining __init__
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Add a method: show_trailer()
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
