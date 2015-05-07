import re
import sys

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
    frequent_words = ['a', 'able', 'about', 'across', 'after',
                        'all', 'almost', 'also', 'am', 'among',
                        'an', 'and', 'any', 'are', 'as', 'at',
                          'be', 'because', 'been', 'but', 'by',
                          'can', 'cannot', 'could', 'dear', 'did',
                           'do', 'does', 'either', 'else', 'ever',
                        'every', 'for', 'from', 'get', 'got',
                        'had', 'has', 'have', 'he', 'her', 'hers',
                        'him', 'his', 'how', 'however', 'i', 'if',
                        'in', 'into', 'is', 'it', 'its', 'just', 'least',
                        'let', 'like', 'likely', 'may', 'me', 'might', 'most',
                         'must', 'my', 'neither', 'no', 'nor', 'not', 'of',
                         'off', 'often', 'on', 'only', 'or', 'other', 'our',
                          'own', 'rather', 'said', 'say', 'says', 'she',
                          'should', 'since', 'so', 'some', 'than', 'that',
                          'the', 'their', 'them', 'then', 'there', 'these',
                          'they', 'this', 'tis', 'to', 'too', 'twas', 'us',
                          'wants', 'was', 'we', 'were', 'what', 'when', 'where',
                           'which', 'while', 'who', 'whom', 'why', 'will',
                           'with', 'would', 'yet', 'you', 'your']
    for word in word_list:
        if word in frequent_words:
            word_counter[word] = 0
        elif word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    return word_counter


def sort_words(a_dict):
    """Takes a dictionary and prints the top 20 words by count. Prints with
    histogram that shows relative frequency"""
    sorted_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    top_20 = sorted_list[0:20]
    highest_count = (top_20)[0][1]
    if highest_count >= 50:
        divisor = int(highest_count / 50)
    else:
        divisor = 1
    for word in top_20:
        print(word[0]+ " " +(int(word[1]/divisor) * "#"))

if __name__ == "__main__":
    all_text = get_text(sys.argv[1])
    all_words_by_freq = word_frequency(all_text)
    sort_words(all_words_by_freq)
