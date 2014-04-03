import os
import urllib2
import xbmcaddon, xbmcgui, xbmcplugin, xbmc

pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]
__settings__ = xbmcaddon.Addon(id='plugin.video.mulbox')
__language__ = __settings__.getLocalizedString

uhash = __settings__.getSetting('uhash')
proto = int(__settings__.getSetting('proto')) + 1
if proto == 2:
  proto = 3

BASE_URL = 'http://www.mulbox.tk'
PLAYLIST_URL = BASE_URL + '/' + uhash + '/playlist' + str(proto) + '.m3u'
XBMC_PLAYLIST_URL = "special://temp/mulbox.m3u"

print PLAYLIST_URL
pldata = urllib2.urlopen(PLAYLIST_URL)
pfile = open(xbmc.translatePath(XBMC_PLAYLIST_URL), 'w')
pfile.write(pldata.read())
pldata.close()
pfile.close()

pl = xbmc.PlayList(1)
pl.load(XBMC_PLAYLIST_URL)

os.unlink(xbmc.translatePath(XBMC_PLAYLIST_URL))

for i in range(pl.size()):
  xbmcplugin.addDirectoryItem(pluginHandle, pl[i].getfilename(), pl[i], isFolder=False)

xbmcplugin.endOfDirectory(pluginHandle)