from collections import defaultdict
from collections import Counter
import re


def analyze_text(file_name):
    '''
    Analyze text file data according to different measures

    :param
    file_name(str): The name of input file in the current directory

    :return
    text(dict): Dictionary containing information of text analysis of the input file,

    if file not found it will return message indicating input file error
    '''
    text = {}
    words = {}
    s_words = {}
    chars = {}
    u_words = []
    less_chars = []
    longest_word = ""
    n_letter = 0
    n_word = 0
    n_line = 0
    avg_word_line = 0
    avg_char_line = 0
    avg_char_word = 0
    mw_size = 0
    n_char = 0
    s_words = defaultdict(lambda: 0, s_words)
    words = defaultdict(lambda: 0, words)
    chars = defaultdict(lambda: 0, chars)
    try:
        file = open(file_name, encoding='utf-8')
        # perform file operations
        for line in file:
            n_char += len(line)
            line = re.sub(r'[^a-zA-Z]', ' ', line)
            line = line.split()
            for word in line:
                if len(word) > 3:
                    words[word] += 1
                elif 1 < len(word) <= 3:
                    s_words[word] += 1
                n_letter += len(word)
                for char in word:
                    chars[char] += 1
            n_word += len(line)
            n_line += 1
        if n_word > 0:
            avg_word_line = round(n_word / n_line, 2)
            avg_char_line = round(n_char / n_line, 2)
            avg_char_word = round(n_char / n_word, 2)
            for key, value in words.items():
                if value == 1:
                    u_words.append(key)
                if len(key) > mw_size:
                    mw_size = len(key)
                    longest_word = key
            for key, value in chars.items():
                if value == 1:
                    less_chars.append(key)
        file.close()
    except FileNotFoundError:
        msg = "Sorry, the file " + file_name + " does not exist."
        return msg

    top_words = Counter(words).most_common(3)
    top_chars = Counter(chars).most_common(3)
    top_s_words = Counter(s_words).most_common(3)
    f_size = round(n_char / 1024, 2)

    summary = f"""____________Summary______________
   File Name: {file_name}
   Total words: {n_word}
   Total letters: {n_letter}
   Total lines: {n_line}
   Average words per line: {avg_word_line}
   Average characters per line: {avg_char_line}
   Average characters per word: {avg_char_word}
   Most common words: {top_words[0][0]}, {top_words[1][0]}, {top_words[2][0]}
   Most common letters: {top_chars[0][0]}, {top_chars[1][0]}, {top_chars[2][0]}
   Longest word: {longest_word}
   Estimate file size: {f_size} KB
   """
    text['s'] = summary
    text['letters'] = n_letter
    text['chars'] = n_char
    text['words'] = n_word
    text['lines'] = n_line
    text['avg_wl'] = avg_word_line
    text['avg_cl'] = avg_char_line
    text['avg_cw'] = avg_char_word
    text['top_words'] = top_words
    text['top_swords'] = top_s_words
    text['top_chars'] = top_chars
    text['u_words'] = u_words
    text['lc_chars'] = less_chars
    text['l_word'] = longest_word
    text['f_size'] = f_size
    return text


if __name__ == "__main__":
    analyze_result = analyze_text('test.txt')
    if type(analyze_result) is dict:
        summary = analyze_result['s']
        print(summary)
    else:
        print(analyze_result)
