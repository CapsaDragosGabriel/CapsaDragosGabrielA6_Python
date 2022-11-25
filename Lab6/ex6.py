import re


def censor_words(match):
    temp = match.group(0)
    #de facut cu regex
    for idx in range(1, len(match.group(0)), 2):
        temp = temp[:idx] + '*' + temp[idx + 1:]
    return temp


def get_words(text):
    # \b ptr "whole words only"
    # cu lambda-ul inlocuiesc cuvintele potrivite cu varianta lor cenzurata
    return re.sub(r'\b[aeiouAEIOU][a-zA-Z0-9]*[aeiouAEIOU]\b', lambda match: censor_words(match), text)


if __name__ == '__main__':
    text = "cuvinte asa cenzurate uaaaaaau,"
    print(get_words(text))
