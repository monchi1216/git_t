import string

def word_count(word_list):
    word_dict = {}
    for i in word_list:
        if i in word_dict.keys():
             word_dict[i] += 1
        else:
             word_dict[i] = 1
    # print(word_dict)
    return dict_count(word_dict)


def dict_count(word_dict):
    for key, value in word_dict.items():
        print(f'{key} {value}')


class STRING_MODIFY():

    def remove_punctuation(self, text):
        return ''.join([i.lower() for i in text if i not in
                        string.punctuation])

    def remove_newline(self, text):
        return (' '.join(text.split('\n'))).split(' ')
