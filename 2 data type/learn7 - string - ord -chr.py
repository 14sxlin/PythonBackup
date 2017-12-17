if __name__ == '__main__':
    text = """asdioasdn \
    sdifnsadonfsaidnniasdnfsd \
    asdfnsdknfsadfnsadjnfsdjknf"""
    print(text)
    text = "sadnhfiasdnfasdf" + \
           "sadfnsdnfsdjnfsjdnf"
    print(text)

    text = ("afsjdfjsdnfjdfnsjd"
            "asdnfsdjnfsjdnfksjdf")
    print(text)

    e = '\u20AC'
    print(e)
    utf8Index = ord(e)
    print("ord(", e, ")=", utf8Index)
    print("hex(ord(", e, "))=", hex(utf8Index))
    print("chr(", utf8Index, ")=", chr(utf8Index))
    a = 'a'
    print("ascii(", a, ")=", ascii(a))
    print("chr(ord(",a,")) = ", chr(ord(a) - 32))

    def uppercase(ch):
        return chr(ord(ch) - 32)

    print(a.upper() == uppercase(a))
    print(a.upper() is uppercase(a))

    sp0 = '\u00C5'    # Å
    spEn = 'Å'.encode("utf8")
    sp1 = '\xc3\x85'
    sp2 = '\xe2\x84\xAB'
    sp3 = '\x41\xCC\x8A'
    print("special0 = ", sp0, "utf8 encode: ", spEn)
    print("special1 = ", sp1)
    print("special2 = ", sp2)
    print("special3 = ", sp3)
    print("sp1 == sp2? ", sp0 == sp1)  # False
    import unicodedata
    # print(unicodedata.normalize("Å"))
