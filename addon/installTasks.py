# -*- coding: UTF-8 -*-
# installTasks for navigateTheNumpadWay add-on
# After renaming emulateNumpadMode addon to navigateTheNumpadWay
# During installing navigateTheNumpadWay, we aim to remove emulateNumpadMode if it exist.

import addonHandler

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.name == 'emulateNumpadMode':
			if not addon.isPendingRemove:
				addon.requestRemove()
			return
