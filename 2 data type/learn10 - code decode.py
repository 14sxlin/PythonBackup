if __name__ == '__main__':
    artist = "Tag Åsén"
    code = artist.encode("Latin1")
    print("{} -> encode(getbytes) = {}".format(artist, code))
    print(code.decode("latin1"))