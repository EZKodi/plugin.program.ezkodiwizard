import xbmcaddon

import os

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE = 'EZKodiWizard'
BUILDERNAME    = 'EZKodi'
EXCLUDES = [ADDON_ID, 'repository.ezkodi']
# Text File with build info in it.
BUILDFILE = 'http://'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE = 'http://'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE = ''
YOUTUBEFILE = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE = 'http://'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'https://www.yourhost.com/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONMAINT      = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONSPEED      = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONAPK        = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONADDONS     = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONYOUTUBE    = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONSAVE       = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONTRAKT      = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONREAL       = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONLOGIN      = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONCONTACT    = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
ICONSETTINGS   = 'https://raw.githubusercontent.com/EZKodi/EZKodiFiles/master/Art/Other%20Art/wizardicon.png'
# Hide the section separators 'Yes' or 'No'
HIDESPACERS = 'No'
# Character used in separator
SPACER = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1 = 'limegreen'
COLOR2 = 'white'
# Primary menu items   / {0} is the menu item and is required
THEME1 = u'[COLOR {color1}][I]([COLOR {color1}][B]EZK[/B][/COLOR][COLOR {color2}]odi Wizard[COLOR {color1}])[/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Build Names          / {0} is the menu item and is required
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Alternate items      / {0} is the menu item and is required
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Current Build Header / {0} is the menu item and is required
THEME4 = u'[COLOR {color1}]Current Build:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Current Theme Header / {0} is the menu item and is required
THEME5 = u'[COLOR {color1}]Current Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT = 'Yes'
# You can add \n to do line breaks
CONTACT = ''
# Images used for the contact window.  http:// for default icon and fanart
CONTACTICON = os.path.join(ART, 'qricon.png')
CONTACTFANART = 'http://'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE = 'Yes'
#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL = 'No'
# Addon ID for the repository
REPOID = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML = ''
# Url to folder zip is located in
REPOZIPURL = ''
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
# Enable Notification screen Yes or No
ENABLE = 'Yes'
# Url to notification file
NOTIFICATION = 'http://'
# Use either 'Text' or 'Image'
HEADERTYPE = 'Text'
# Font size of header
FONTHEADER = 'Font14'
HEADERMESSAGE = '[COLOR limegreen][B]EZK[/B][/COLOR]odi Wizard'
# url to image if using Image 424x180
HEADERIMAGE = 'http://'
# Font for Notification Window
FONTSETTINGS = 'Font13'
# Background for Notification Window
BACKGROUND = 'http://'
#########################################################
