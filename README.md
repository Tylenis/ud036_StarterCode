# Movie Trailer Website
generates a html file  which contains links to movies trailers on youtube and opens it in the browser.

## Note
This product uses the TMDb API but is not endorsed or certified by TMDb.

## Requirements:
Python 2.7

## Download instruction:
download from https://github.com/Tylenis/ud036_StarterCode/archive/master.zip
or clone from https://github.com/Tylenis/ud036_StarterCode.git

## Usage
Create (delete) media.Movie() class instances in entertainment_center.py file.
```
WALL_E = media.Movie("WALL-E", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg", "https://www.youtube.com/watch?v=alIq_wG9FNk")
```

Add (remove) instance to the MOVIES_LIST list.
```
MOVIES_LIST = [WALL_E]
```

Run file.
```
python entertainment_center.py
```

