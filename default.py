import os
import urllib2
import xbmcaddon, xbmcgui, xbmcplugin, xbmc

pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]
__settings__ = xbmcaddon.Addon(id='plugin.video.mulbox')
__language__ = __settings__.getLocalizedString

try:
  uhash = __settings__.getSetting('uhash')
  proto = int(__settings__.getSetting('proto')) + 1
except(ValueError):
  proto = 1

if proto == 2:
  proto = 3

BASE_URL = 'http://www.mulbox.tk'
PLAYLIST_URL = BASE_URL + '/' + uhash + '/playlist' + str(proto) + '.m3u'
XBMC_PLAYLIST = xbmc.translatePath("special://temp/mulbox.m3u")

print "playlist url: %s" % PLAYLIST_URL
print "ondisk path: %s" % XBMC_PLAYLIST

pldata = urllib2.urlopen(PLAYLIST_URL)
pfile = open(XBMC_PLAYLIST, 'w')
pfile.write(pldata.read())
pldata.close()
pfile.close()

pl = xbmc.PlayList(1)
ret = pl.load(XBMC_PLAYLIST)

for i in range(pl.size()):
  print "[%d]: %s: %s" % (i, pl[i].getdescription(), pl[i].getfilename())
  xbmcplugin.addDirectoryItem(pluginHandle, pl[i].getfilename(), pl[i], isFolder=False)

xbmcplugin.endOfDirectory(pluginHandle)
