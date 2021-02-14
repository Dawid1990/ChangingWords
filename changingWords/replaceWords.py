import re

class replaceWords:
    def change_words(self, text, last_letter_in_word, replacement_word):
        same_words_list = []
        splitted_lyrics = re.split(' |\n', text)
        
        for item in splitted_lyrics:
            if item in same_words_list:
                continue
            if item.endswith(last_letter_in_word):
                same_words_list.append(item)
                text = re.sub(r"\b%s\b" % item, replacement_word, text, flags=re.UNICODE) 
            elif item.endswith(last_letter_in_word + ','):
                same_words_list.append(item)
                text = re.sub(r"\b%s\b" % item[:-1], replacement_word, text, flags=re.UNICODE)

        return text