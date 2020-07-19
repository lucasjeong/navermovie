from bs4 import BeautifulSoup
import urllib.request as req

url = "https://movie.naver.com/movie/running/current.nhn"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

movie_table = soup.select("#content > div.article > div:nth-child(1) > div.lst_wrap > ul")[0]
movie_list = movie_table.select("dl.lst_dsc")

for movie in movie_list:
    movie_namelink = movie.select("dt.tit a")[0]

    movie_name = movie_namelink.string
    movie_link = "https://movie.naver.com" + movie_namelink["href"]

    movie_star = movie.select("span.num")[0].string

    if float(movie_star) >= 9.0:
        if movie.select("span.link_txt a")[0].string == "드라마":
            print(f"제목 - {movie_name}")
            print(f"영화 정보 : {movie_link}")
        else:
            if movie.select("span.link_txt a")[1].string == "드라마":
                print(f"제목 - {movie_name}")
                print(f"영화 정보 : {movie_link}")
            else:
                if movie.select("span.link_txt a")[2].string == "드라마":
                    print(f"제목 - {movie_name}")
                    print(f"영화 정보 : {movie_link}")