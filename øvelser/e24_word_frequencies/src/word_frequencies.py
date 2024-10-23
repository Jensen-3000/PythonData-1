#!/usr/bin/env python3


def word_frequencies(filename):
    dict = {}

    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1

    return dict


def get_to_5_p_word_frequencies(filename):
    wd = word_frequencies(filename)
    wd = dict(sorted(wd.items(), key=lambda x: x[1], reverse=True))

    for w, c in list(wd.items())[:5]:
        print(w, c, sep="\t")


def main():
    fname = r"øvelser\e24_word_frequencies\src\alice.txt"
    # print(word_frequencies(fname))

    get_to_5_p_word_frequencies(fname)


if __name__ == "__main__":
    main()
