import xbmc
import xbmcgui
import Media
import AmbiBox


class AmbiBoxPlayer(xbmc.Player):

    def __init__(self):
        xbmc.Player.__init__(self)
        self.media = Media.Media()
        self.ambibox = AmbiBox.AmbiBox('127.0.0.1', 3636)

    def onPlayBackStarted(self):
        if xbmc.Player().isPlayingVideo():
            print 'Ambibox : starting playing video'

            # we retrieve the format of the playing video
            ratio = self.media.getAspectRatio(xbmc.Player().getPlayingFile())
            newProfile = profileFormat % ratio
            print "Setting AmbiBox profile to : " + newProfile

            self.ambibox.connect()

            # we store the previous parameters
            self.previousStatus = self.ambibox.getStatus()
            self.previousProfile = self.ambibox.getProfile()

            self.ambibox.lock()
            self.ambibox.setProfile(newProfile)
            self.ambibox.turnOn()
            self.ambibox.disconnect()

    def onPlayBackEnded(self):
        if VIDEO == 1:
            self.__onVideoStopped()

    def onPlayBackStopped(self):
        if VIDEO == 1:
            self.__onVideoStopped()

    def __onVideoStopped(self):
        self.ambibox.connect()
        self.ambibox.lock()
        # we set the previous parameters back
        self.ambibox.setProfile(self.previousProfile)
        self.ambibox.setStatus(self.previousStatus)
        self.ambibox.disconnect()

player = AmbiBoxPlayer()
profileFormat = "Adalight %s"

VIDEO = 0
while 1:
    if xbmc.Player().isPlaying():
        if xbmc.Player().isPlayingVideo():
            VIDEO = 1
        else:
            VIDEO = 0
    xbmc.sleep(1000)
