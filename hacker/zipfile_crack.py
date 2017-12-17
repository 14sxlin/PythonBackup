import zipfile


def extract_zipfile(filename, pwd=None):
    try:
        zfile = zipfile.ZipFile(filename)
        zfile.extractall(pwd=pwd)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    extract_zipfile("test.zip")
