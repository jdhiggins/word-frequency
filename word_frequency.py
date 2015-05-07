import re

def get_text(text_file):
    """Gets all text from input document."""
    with open(text_file) as text:
        full_text = text.read()
    return full_text


def make_text(text):
    """Takes text and removes punctuation and spaces"""
    return (re.sub(r'[^A-Za-z ]'," ", text)).lower()


def word_frequency(a_string):
    """Takes a string and gives a dictionary with word count"""
    clean_text = make_text(a_string)
    word_list = clean_text.split()
    word_counter = {}

    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    return word_counter


def sort_words(a_dict):
    """Takes a dictionary and prints the top 20 words by count"""
    sorted_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    top_20 = sorted_list[0:20]
    for word in top_20:
        print((word[0]+ " " +str(word[1])))

if __name__ == "__main__":
    all_text = get_text("sample.txt")
    all_words_by_freq = word_frequency(all_text)
    sort_words(all_words_by_freq)
