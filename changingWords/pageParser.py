import requests
import sys
import re
from bs4 import BeautifulSoup

class pageParser:
    main_page_url = "http://teksty.org/czeslaw-spiewa,teksty-piosenek"

    def __open_url_and_get_text(self, page_url):
        try:
            r = requests.get(page_url)

            if r.status_code == 200:
                r.encoding = 'utf-8'
                return r.text
            else:
                print ('Error ! Returned HTTP code: ' + str(r.status_code))
                exit()
        except requests.exceptions.MissingSchema:
            print ('Invalid URL')
        except requests.exceptions.ConnectionError:
            print ('Connection Error')
        except requests.exceptions.RequestException as e:
            print (e)
        except:      
            print ('Unhandled exception ' + str(sys.exc_info()[0]))

        exit()

    def __get_song_pages_count(self):
        pages_count = 0
        soup = BeautifulSoup(self.__open_url_and_get_text(self.main_page_url), 'lxml')
        pages_number = soup.body.find('div', 'pages')
    
        for link in pages_number.children:
            if link.string != '\n':
                pages_count += 1
            else:
                continue

        return pages_count

    def __find_song_link(self, song_name):
        pages_count = self.__get_song_pages_count()

        for i in range(1, pages_count):
            page_url = self.main_page_url + '/' + str(i)
            soup = BeautifulSoup(self.__open_url_and_get_text(page_url), 'lxml')
            songs_tags = soup.find_all(id = re.compile("(song_[0-9])"))
            songs_tags_count = len(songs_tags) - 1

            for song in songs_tags:
                song_title = song.find('strong').get_text()
            
                if song_title.strip().upper() == song_name.strip().upper():
                    song_link = song.find('a').get('href')
                    break

            if song_link:
                break

        if not song_link:
            print("Cannot find song lyrics")
            exit()

        return song_link

    def get_song_lyrics(self, song_name):
        song_link = self.__find_song_link(song_name)
        soup = BeautifulSoup(self.__open_url_and_get_text(song_link), 'lxml')
        lyrics = soup.body.find('div', 'tabCont originalText songTextDisplay')
        return lyrics.get_text().replace('\r\n\t\t\t', '', 1)