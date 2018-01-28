"""Module creates a list of movies and serves it
   to fresh_tomatoes.open_movies_page()"""

import sys
import media
import fresh_tomatoes
import load_from_themoviedb

#Predestination movie: movie title, poster image and movie trailer
PREDESTINATION = media.Movie(
    "Predestination",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAzODc3NjU1NzNeQTJeQWpwZ15BbWU4MDk5NTQ4NTMx._V1_SY1000_CR0,0,677,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=F_CCjXQ9aYw"
)
#WALL_E movie: movie title, poster image and movie trailer
WALL_E = media.Movie(
    "WALL-E",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=alIq_wG9FNk"
)
#Interstellar movie: movie title, poster image and movie trailer
INTERSTELLAR = media.Movie(
    "Interstellar",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=0vxOhd4qlnA"
)
#The Martian movie: movie title, poster image and movie trailer
MARTIAN = media.Movie(
    "The Martian",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ej3ioOneTy8"
)
#Gran Torino movie: movie title, poster image and movie trailer
GRAN_TORINO = media.Movie(
    "Gran Torino",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5NTk2OTU1Nl5BMl5BanBnXkFtZTcwMDc3NjAwMg@@._V1_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=3WkGaPMInMc"
)
#Apocalypse Now movie: movie title, poster image and movie trailer
APOCALYPSE_NOW = media.Movie(
    "Apocalypse Now",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDg1MDgzMmQtNDhlYS00MzZiLTllZGItNzliZTE1ODBiZDQwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,658,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=snDR7XsSkB4"
)

movies_list = [PREDESTINATION, WALL_E, INTERSTELLAR,
               MARTIAN, GRAN_TORINO, APOCALYPSE_NOW]

if sys.argv > 1:
    for i in range(1, len(sys.argv)):
        new_movie = load_from_themoviedb.load_movie(sys.argv[i])
        if new_movie != 0:
            movies_list.append(new_movie)

fresh_tomatoes.open_movies_page(movies_list)
