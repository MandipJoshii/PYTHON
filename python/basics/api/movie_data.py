import pandas as py
import requests as r


response = r.get('https://api.themoviedb.org/3/discover/movie?api_key=f0c78d92ea64912ea058acd747d9f01d&include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc')

print(response.status_code) # -> 200 status code -> successfully fetch data from http request from get()
# print(response.text)
df = py.DataFrame(response.json()["results"])[['id','original_title','title','vote_average','vote_count']] 
"""this means -> [['id','original_title','title','vote_average','vote_count']]
only select and display given columns"""
print(df)


df.to_csv("movie_report.csv",index=False)