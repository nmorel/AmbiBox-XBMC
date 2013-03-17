import os
import codecs
import Media

media = Media.Media()

ratios = dict()

paths = [u'C:\\dev']
for path in paths:
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".mkv", ".avi", ".mp4", ".m2ts", ".ts")):
                fullPath = os.path.join(root, name)

                ratio = media.getAspectRatio(fullPath)

                print "%s : %s" % (fullPath, ratio)

                videosByRatio = ratios.get(ratio, list())
                videosByRatio.append(fullPath)
                ratios[ratio] = videosByRatio

f = codecs.open("ratios.html", "w", "utf-8")
f.write("<html><head><meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\"></head><body>\n")


f.write("<p><u><b>%i different ratios found : </b></u></p>\n" % (len(ratios)))
f.write("<ol>\n")
for ratio in ratios.iterkeys():
    videosByRatio = ratios.get(ratio)
    f.write("<p><b>%s :</b> %i videos" % (ratio, len(videosByRatio)))
f.write("</ol>")

f.write("<p><u><b>Videos files by ratio :</b></u></p>")
for ratio in ratios.iterkeys():
    f.write("<p><b>%s : </b></p>\n<ol>\n" % ratio)
    videosByRatio = ratios.get(ratio)
    for video in videosByRatio:
        f.write("\t<li>%s</li>" % video)
    f.write("\n</ol><br>\n\n")

f.write("</body></html>")
f.close()
