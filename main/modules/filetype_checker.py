import mimetypes

def fileMime(value):
    return mimetypes.guess_type(value)[0]