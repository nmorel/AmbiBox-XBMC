import Media
import os

media = Media.Media()

ratios = dict()

#paths = ['E:\\', 'F:\\', 'G:\\', 'H:\\']
#paths = ['F:\\']
paths = ['C:\\dev']
for path in paths:
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".mkv", ".avi", ".mp4", ".m2ts", ".ts")):
                fullPath = os.path.join(root, name)
                ratio = media.getAspectRatio(fullPath)
                videosByRatio = ratios.get(ratio, set())
                videosByRatio.add(fullPath)
                ratios[ratio] = videosByRatio


print "%i ratios trouves" % (len(ratios))

f = open('ratios.html', 'w')

for ratio in ratios.iterkeys():
    f.write("<p><b>%s : </b></p>\n<ol>\n" % ratio)
    videosByRatio = ratios.get(ratio)
    print "%s : %i occurences trouvees" % (ratio, len(videosByRatio))
    for video in videosByRatio:
        f.write("\t<li>%s</li>" % video)
    f.write("\n</ol><br>\n\n")
