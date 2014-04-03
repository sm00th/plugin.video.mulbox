import os, sys
import urllib2
import xbmcaddon, xbmcgui, xbmcplugin, xbmc

pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]
addon = xbmcaddon.Addon(id='plugin.video.mulbox')
__language__ = addon.getLocalizedString

try:
  uhash = addon.getSetting('uhash')
  proto = int(addon.getSetting('proto')) + 1
except(ValueError):
  proto = 1

if proto == 2:
  proto = 3

BASE_URL = 'http://www.mulbox.tk'
PLAYLIST_URL = BASE_URL + '/' + uhash + '/playlist' + str(proto) + '.m3u'
XBMC_PLAYLIST = xbmc.translatePath("special://temp/mulbox.m3u")

print "playlist url: %s" % PLAYLIST_URL
print "ondisk path: %s" % XBMC_PLAYLIST

try:
  pldata = urllib2.urlopen(PLAYLIST_URL)
  pfile = open(XBMC_PLAYLIST, 'w')
  pfile.write(pldata.read())
  pldata.close()
  pfile.close()
except:
  dialog = xbmcgui.Dialog()
  dialog.ok(addon.getLocalizedString(30200), addon.getLocalizedString(30201))
  sys.exit(1)

pl = xbmc.PlayList(1)
ret = pl.load(XBMC_PLAYLIST)

if ret == 0:
  dialog = xbmcgui.Dialog()
  dialog.ok(addon.getLocalizedString(30200), addon.getLocalizedString(30202))
  sys.exit(1)

for i in range(pl.size()):
  print "[%d]: %s: %s" % (i, pl[i].getdescription(), pl[i].getfilename())
  xbmcplugin.addDirectoryItem(pluginHandle, pl[i].getfilename(), pl[i], isFolder=False)

xbmcplugin.endOfDirectory(pluginHandle)
