# -*- coding: utf-8 -*-
# NVDA Add-on: Emulate Numpad Mode
# Copyright (C) 2021 ibrahim hamadeh
# This add-on is free software, licensed under the terms of the GNU General Public License (version 2).
# See the file COPYING for more details.

import core, ui
import globalPluginHandler
from globalCommands import commands
import inputCore
from keyboardHandler import KeyboardInputGesture
import scriptHandler
from logHandler import log
import addonHandler
addonHandler.initTranslation()

# mapping keys to script
mappedKeys= {
	'7': ['script_review_previousLine', '7'],
	'8': ['script_review_currentLine', '8'],
	'9': ['script_review_nextLine', '9'],
	'u': ['script_review_previousWord', '4'],
	'i': ['script_review_currentWord', '5'],
	'o': ['script_review_nextWord', '6'],
	'j': ['script_review_previousCharacter', '1'],
	'k': ['script_review_currentCharacter', '2'],
	'l': ['script_review_nextCharacter', '3'],
	'm': ['None', '0'],
}

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.modes= [
		# Translators: The normal mode you can toggle to.
		_('Normal Mode'),
		# Translators: The numpad mode you can toggle to.
		_('Numpad Mode'),
		# Translators: The numbers mode you can toggle to.
		_('Numbers Mode')
		]
		self.index= 0

	def terminate(self, *args, **kwargs):
		super().terminate(*args, **kwargs)

	def activateNumpadMode(self):
		'''Activating numpad Mode.'''
		#log.info('activating numpad mode ...')
		#log.info('binding gestures for numpad mode...')
		for key in mappedKeys:
			self.bindGesture(f'kb:{key}', 'numpadMode')

	def activateNumbersMode(self):
		#log.info('binding gestures for numbersMode')
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)
		for key in mappedKeys:
			self.bindGesture(f'kb:{key}', 'numbersMode')

	def clearAllBindings(self):
		''' Helper function to clear numpad mode bindings.'''
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_numpadMode(self, gesture):
		#log.info('under script numpadMode')
		key= gesture.mainKeyName
		try:
			script= getattr(commands, mappedKeys[key][0])
		except:
			gesture.send()
		else:
			script(gesture)

	def script_numbersMode(self, gesture):
		key= gesture.mainKeyName
		if key not in mappedKeys or key in '789':
			gesture.send()
			return
		_gesture= KeyboardInputGesture.fromName(mappedKeys[key][1])
		inputCore.manager.emulateGesture(_gesture)

	
	def script_toggleEmulatedModes(self, gesture):
		self.index= (self.index+1)%len(self.modes)
		#log.info(f'self.index: {self.index}')
		message= self.modes[self.index]
		if self.index== 1:
			self.activateNumpadMode()
		elif self.index==2:
			self.activateNumbersMode()
		else:
			self.clearAllBindings()
		ui.message(message)

	# Translators: Category of addon in input gestures.
	script_toggleEmulatedModes.category= _("Emulate Numpad Mode")
	# Translators: Message displayed in input help more.
	script_toggleEmulatedModes.__doc__= _("Toggle between normal, emulated numpad mode and numbers mode state")

	__gestures= {
	'kb:nvda+h': 'toggleEmulatedModes',
	}

