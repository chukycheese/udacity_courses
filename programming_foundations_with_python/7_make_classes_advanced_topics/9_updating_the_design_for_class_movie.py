class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration



class Movie(Video):
    def __init__(self, title):
        print("Movie Constructor Called")
        Video.__init__(self, title, duration)


    def show_trailer():



class TvShow(Video):
    def __init__(self, title, duration, ):
