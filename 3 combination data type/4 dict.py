import string
import sys
import os
import collections

if __name__ == '__main__':
    info = {"id": 203, "name": "xiaoming"}
    print(info["id"])

    d = {}.fromkeys("ABCD", 3)
    s = set("ACX")
    matches = d.keys() & s
    print(d, matches)

    words = {}
    strip = string.whitespace + string.punctuation
    for filename in sys.argv[1:]:
        for line in open(filename):
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] = words.get(word, 0) + 1

    file_sizes = {name: os.path.getsize(name) for name in os.listdir(".")}
    print(file_sizes)

    inverse_file_sizes = {v: k for k, v in file_sizes.items()}
    print(inverse_file_sizes)

    my = collections.defaultdict(int)  # int is a factory
    print(my)
    try:
        my["gender"] += 1
        print("my.gender = {0}".format(my['gender']))
        # info["gender"] += 1
        # print("info.gender = {0}".format(info['gender']))
    except KeyError as e:
        print("error : ", e)

    my = collections.OrderedDict()
    my[5] = "b"
    my[4] = "a"
    my[6] = "c"
    for i in my.keys():
        print(i)
    for v in my.values():
        print(v)

    my[1] = None

