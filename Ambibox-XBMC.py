import xbmc
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
            if ratio in ratioDictionary:
                ratio = ratioDictionary[ratio]
            else:
                message = "Ratio inconnu : %s" % ratio
                xbmc.executebuiltin('XBMC.Notification(AmbiBox, %s, 3000)' % message)
                print message
                # Using 16:9 as default profile
                ratio = '16:9'

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
ratioDictionary = {
    '16:9': '16:9',
    '2.35:1': '2.35:1',
    '2.40:1': '2.40:1',
    '2.25:1': '2.25:1',
    '4:3': '4:3',
    '3:2': '3:2',
    '1.391': '4:3',
    '1.85:1': '1.85:1',
    '1.727': '1.7',
    '1.739': '1.7',
    '1.731': '1.7',
    '1.733': '1.7',
    '1.659': '1.7',
    '1.895': '2.0',
    '2.000': '2.0'
}

VIDEO = 0
while 1:
    if xbmc.Player().isPlaying():
        if xbmc.Player().isPlayingVideo():
            VIDEO = 1
        else:
            VIDEO = 0
    xbmc.sleep(1000)
