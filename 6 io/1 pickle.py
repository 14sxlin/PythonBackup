import pickle
import gzip

GZIP_MAGIC = b"\x1F\x88"


def export_pickle(filename,data,compress=False):
    fh = None
    try:
        if compress:
            fh = gzip.open(filename,"wb")
        else:
            fh = open(filename,"wb")
        pickle.dump(data,fh,pickle.HIGHEST_PROTOCOL)
        return True
    except (EnvironmentError,pickle.PickleError) as e:
        print(e)
        return False
    finally:
        if fh is not None:
            fh.close()


def import_pickle(filename):
    fh = None
    try:
        fh = open(filename,"rb")
        magic =fh.read(len(GZIP_MAGIC))
        if magic == GZIP_MAGIC:
            fh.close()
            fh = gzip.open(filename,"rb")
        else:
            fh.seek(0)
        return True
    except (EnvironmentError,pickle.PickleError) as e:
        print(e)


if __name__ == '__main__':
    print("pickle")

    import abc

