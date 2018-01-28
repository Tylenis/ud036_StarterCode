"""Module contains a single class for a movie data storage."""


class Movie(object):
    """Store the movie data.

       Attributes:
           title: movie title.
           poster_image_url: movie poster url.
           trailer_youtube_url: url of movie trailer on youtube.
    """
    def __init__(self, title, poster_url, trailer_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
