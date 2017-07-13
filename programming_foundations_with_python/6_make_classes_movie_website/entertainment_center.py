import fresh_tomatoes
import media
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)

avatar = media.Movie("Avater",
                     "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=aVdO-cx-McA")
# print(avatar.storyline)

# Add another instance: okja
okja = media.Movie("Okja",
                   "Meet Mija, a young girl who risks everything to prevent a powerful, multi-national company from kidnapping her best friend - a fascinating animal named Okja.",
                   "http://t1.gstatic.com/images?q=tbn:ANd9GcSkeKv-OKoYw_T-ObRdOKEMfdTrQoJa6O4dLiOhca2PyD1ZkC5c",
                   "https://www.youtube.com/watch?v=AjCebKn4iic")

# print(okja.storyline)
# okja.show_trailer()

# 15. Coding the Movie Website
movies = [toy_story, avatar, okja]
fresh_tomatoes.open_movies_page(movies)
