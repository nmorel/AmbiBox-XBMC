from MediaInfoDLL import MediaInfo, Stream


class Media:

    def __init__(self):
        self.mi = MediaInfo()

    def getAspectRatio(self, file):
        self.mi.Open(file)
        format = self.mi.Get(Stream.Video, 0, "DisplayAspectRatio/String")
        self.mi.Close()
        return format
