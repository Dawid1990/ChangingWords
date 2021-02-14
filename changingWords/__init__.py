from .pageParser import pageParser
from .replaceWords import replaceWords

def main():
    song_name = input("Enter song name: \n")
    __checkInput(song_name)
    print(f"You entered {song_name}")
    last_letter = input("Enter last letter of words that will be replaced: \n")
    __checkInput(last_letter)
    print(f"You entered {last_letter}")
    replace_word = input("Enter word which will replace words ending with letter inputed before: \n")
    __checkInput(replace_word)
    print(f"You entered {replace_word}")
    slack_token = input("Enter slack token if you want to send it to slack channel: \n")
    
    if slack_token:
        slack_channel = input("Enter slack channel")
        __checkInput(slack_channel)

    parser = pageParser()
    replacing = replaceWords()
    song_lyrics = parser.get_song_lyrics(song_name)
    replaced_text = replacing.change_words(song_lyrics, last_letter, replace_word)
    print(f"Changed text: \n {replaced_text}")

def __checkInput(input):
    if not input:
        print(f"Error: empty input is not valid")
        exit()