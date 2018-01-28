"""This module uses The Movie Database API to download movie data
   and generate media.Movie() class instances.

   Functions:
       load_movie() - downloads the movie data from The Movie Database,
           makes instance of media.Movie() class and appends it to the input list.
       make_trailer_url() - generates the movie trailer url.
"""

import urllib
import json
import media

API_KEY = "YOUR_API_KEY_HERE"
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500/"
TRAILER_BASE_URL = "https://www.youtube.com/watch?v="
API_BASE_URL = "https://api.themoviedb.org/3/"

def load_movie(title):
    """Download movie data from The Movie Database,
       make instance of media.Movie() class and append it to input list"""
    try:
        query = urllib.urlencode([
            ("api_key", "fc151f187839bb33c12a7985f58a8194"),
            ("language", "en-US"), ("query", title), ("page", 1),
            ("include_adult", "false")
        ])
        response = urllib.urlopen(API_BASE_URL+"search/movie?"+query)
        data = json.load(response)
        temp_title = data["results"][0]["title"]
        temp_poster = POSTER_BASE_URL+data["results"][0]["poster_path"]
        temp_trailer = make_trailer_url(data["results"][0]["id"])
        return media.Movie(temp_title, temp_poster, temp_trailer)
    except IndexError:
        print("Movie {} not found !".format(title))
        return 0

def make_trailer_url(movie_id):
    """Generate the movie trailer url"""
    query = urllib.urlencode([
        ("api_key", "fc151f187839bb33c12a7985f58a8194"),
        ("language", "en-US")
    ])
    response = urllib.urlopen(API_BASE_URL+"movie/"+str(movie_id)+"/videos?"+query)
    data = json.load(response)
    key = data["results"][0]["key"]
    return TRAILER_BASE_URL + key
