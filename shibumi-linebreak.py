

# ------------------------
# asdfasdf
# asdf
# ------------------------
import math


def main():
    input_str = '''asdf aaaaasdf f f asdf'''

    '''
    asdf
    aaaaa
    sdf f
    f f
    asd
    '''

    input_strs = input_str.split()
    # px_per_char = 10
    px_per_char_dict = {'a': 20, 's': 20, 'd': 20, 'f': 20, ' ': 20}
    txt_len_px = 100



    n_lines = 0
    px_ct = 0
    # for _char in input_str:
    #     if px_ct + px_per_char_dict[_char] > txt_len_px:
    #         n_lines += 1
    #         px_ct = 0
    #     px_ct += px_per_char_dict[_char]

    def pix_ct_word(_word) -> int:
        char_count = 0
        for _char in _word:
            char_count += px_per_char_dict[_char]
        return char_count

    def line_count_word(_word) -> int:
        return math.ceil(pix_ct_word(_word) / txt_len_px)

    words = str()
    for _word in input_strs:
        if pix_ct_word(words) + pix_ct_word(' ' + _word) > txt_len_px:
            n_lines += line_count_word(_word)
            print(words)
            words = str()
        if pix_ct_word(_word) > txt_len_px:
            _words = [_word[i:i+5] for i in range(0,len(_word),5)]
            ' '.join(_words)
            n_lines += len(_words)
        else:
            words += ' ' + _word
            n_lines += 1

    # px_ct += px_per_char_dict[_char]
    # px_ct = len(input_str) * px_per_char
    # print(px_ct)
    print(n_lines)

    # n_wraps = math.ceil(px_ct / txt_len_px)
    # print(n_wraps)


if __name__ == '__main__':
    main()
