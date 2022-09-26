# NVDA Add-on: Emulate Numpad Mode
# Copyright (C) 2021 ibrahim hamadeh
# This add-on is free software, licensed under the terms of the GNU General Public License (version 2).
# See the file COPYING for more details.

import ui
import globalPluginHandler
import gui, wx
from gui import guiHelper
from globalCommands import commands
from scriptHandler import script
import inputCore
import config
from keyboardHandler import KeyboardInputGesture
from logHandler import log
from .forms import Forms

import addonHandler
addonHandler.initTranslation()

class GestureHelper():
	''' Helper class to deal with gesture in the form, that are present at the same time in user gesture map.
		user gesture map contains only gestures added or assigned by the user, and they sometimes grab the form gesture.
	'''
	# temptDict holds gestures that will be suspended, and activated later.
	temptDict= {}
	# numpadDict maps gestures in the form to scripts. it will be assigned a value from activateNumpadMode method.
	numpadDict= None

	def suspendGestures(self):
		''' Suspending gestures that are in the user gesture map, and are used in the form. '''
		userGestureMap= inputCore.manager.userGestureMap._map
		for k in self.numpadDict:
			normalizedGesture= inputCore.normalizeGestureIdentifier(f'kb:{k}')
			if normalizedGesture in userGestureMap:
				scripts= userGestureMap[normalizedGesture]
				#log.info(f'scripts: {scripts}')
				if scripts:
					GestureHelper.temptDict[normalizedGesture]= scripts[:]
					for script in scripts[:]:
						#log.info(f'script: {script}')
						try:
							inputCore.manager.userGestureMap.remove(normalizedGesture, *script)
							#log.info(f'removing script: {script}')
						except Exception as e:
							log.info('Error in removing gesture', exc_info= True)
							continue
		#log.info(f'temptDict: {self.temptDict}')

	def activateSuspendedGestures(self):
		''' Activating or returning suspended gestures to funcional or previous state.'''
		#log.info('under activateSuspendedGestures...')
		_dict= self.temptDict
		#log.info(f'_dict: {_dict}')
		if not _dict:
			return
		for gesture in _dict:
			scripts= _dict[gesture][:]
			if scripts:
				[inputCore.manager.userGestureMap.add(gesture, *script) for script in scripts]
		GestureHelper.temptDict= {}

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

		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(EmulateNumpadModePanel)

	def terminate(self, *args, **kwargs):
		super().terminate(*args, **kwargs)
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(EmulateNumpadModePanel)

	def activateNumpadMode(self):
		'''Activating numpad Mode for selected form.'''
		#log.info('activating numpad mode ...')
		form= Forms()
		self.numpadDict= form._numpadDict
		GestureHelper.numpadDict= form._numpadDict
		self.numbersDict= form._numbersDict
		# Suspending gestures if present in user gesture map.
		GestureHelper().suspendGestures()

		# If use escape key to dismiss numpad mode, bind escape key to toggleEmulatedModes script.
		if config.conf["emulateNumpadMode"]["dismissNumpadModeByEscape"]:
			self.bindGesture(f'kb:escape', 'toggleEmulatedModes')
		# Binding gestures in selected form to numpadMode script.
		for key in self.numpadDict:
			self.bindGesture(f'kb:{key}', 'numpadMode')

	def activateNumbersMode(self):
		''' Activating numbers mode for selected form.'''
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)
		# If use escape key to dismiss numpad mode, bind escape key to toggleEmulatedModes script.
		if config.conf["emulateNumpadMode"]["dismissNumpadModeByEscape"]:
			self.bindGesture(f'kb:escape', 'toggleEmulatedModes')
		# Binding keys in selected form to numbersMode script.
		for key in self.numbersDict:
			self.bindGesture(f'kb:{key}', 'numbersMode')

	def clearAllBindings(self):
		''' Helper function to clear numpad or numbers mode bindings.'''
		self.clearGestureBindings()
		GestureHelper().activateSuspendedGestures()
		self.bindGestures(self.__gestures)

	@script(
		# Translators: Message displayed in input help mode.
		description= _("Emulate numpad key press.")
	)
	def script_numpadMode(self, gesture):
		#log.info('under script numpadMode...')
		keys= gesture.displayName
		#log.info(f'displayName: {keys}')
		try:
			script= getattr(commands, self.numpadDict[keys])
		except:
			gesture.send()
			log.info("", exc_info=True)
		else:
			script(gesture)

	@script(
		# Translators: Message displayed in input help mode.
		description= _("Emulate a number key press.")
	)
	def script_numbersMode(self, gesture):
		#log.info('under script_numbersMode...')
		key= gesture.mainKeyName
		if key not in self.numbersDict or key in '789':
			gesture.send()
			return
		_gesture= KeyboardInputGesture.fromName(self.numbersDict[key])
		inputCore.manager.emulateGesture(_gesture)

	def script_toggleEmulatedModes(self, gesture):
		self.index= (self.index+1)%len(self.modes)
		if gesture.mainKeyName== 'escape' and config.conf["emulateNumpadMode"]["dismissNumpadModeByEscape"]:
			self.index= 0
		elif config.conf["emulateNumpadMode"]["skiptNumbersMode"] and self.index== 2:
			self.index= 0
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
	# Translators: Message displayed in input help mode.
	script_toggleEmulatedModes.__doc__= _("Toggle between normal, emulated numpad mode and numbers mode states.")

	__gestures={
		'kb:shift+nvda+f4': 'toggleEmulatedModes'
	}

#default configuration 
configspec={
	"formChosen": "integer(default=0)",
	"skiptNumbersMode": "boolean(default=True)",
	"dismissNumpadModeByEscape": "boolean(default=True)",
}
config.conf.spec["emulateNumpadMode"]= configspec

# The setting panel for the addon.
class EmulateNumpadModePanel(gui.SettingsPanel):
	# Translators: title of the panel
	title= _("Emulate Numpad Mode")

	def makeSettings(self, sizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=sizer)

		# The combo box to choose the form
		formChoices= [
			# Translators: Option in combo box for form1
			_("Form1"),
			# Translators: Option in combo box for form2
			_("Form2"),
			# Translators: Option in combo box for form3
			_("Form3")
		]
		self.chooseFormCumbo= sHelper.addLabeledControl(
			# Translators: Label of combo box
			_("Choose form to emulate to numpad mode:"), wx.Choice, choices= formChoices)
		self.chooseFormCumbo.SetSelection(config.conf["emulateNumpadMode"]["formChosen"])
		self.chooseFormCumbo.Bind(wx.EVT_CHOICE, self.onChooseForm)

		# Text control to show the selected form
		self.selectedForm= sHelper.addLabeledControl(
			# Translators: Label of text control that exposes the selected form.
			_("Selected Form"), wx.TextCtrl, style=wx.TE_MULTILINE|wx.TE_READONLY
		)
		self.selectedForm.SetValue(Forms().getKeyNames())
		self.selectedForm.Bind(wx.EVT_SET_FOCUS, self.onFormFocus)

		# checkbox to skipt numbers mode.
		self.skipNumbersModeCheckbox = sHelper.addItem(wx.CheckBox(self,
			# Translators: Label of checkbox
			label= _("Skipt numbers mode")
		))
		self.skipNumbersModeCheckbox.SetValue(config.conf["emulateNumpadMode"]["skiptNumbersMode"])

		# checkbox to make escape key dismiss numpad mode.
		self.dismissNumpadModeByEscapeCheckbox = sHelper.addItem(wx.CheckBox(self,
			# Translators: Label of checkbox
			label= _("Dismiss numpadMode by escape key")
		))
		self.dismissNumpadModeByEscapeCheckbox.SetValue(config.conf["emulateNumpadMode"]["dismissNumpadModeByEscape"])

	def onChooseForm(self, event):
		index= self.chooseFormCumbo.GetSelection()
		keyNames= Forms().allKeyNames[index]
		self.selectedForm.SetValue(keyNames)

	def onFormFocus(self, event):
		import core
		# Translators: Message helps the user to view the form.
		core.callLater(1000,ui.message, _("You can use up and down arrows to view the form"))

	def onSave(self):
		config.conf["emulateNumpadMode"]["formChosen"]= self.chooseFormCumbo.GetSelection()
		config.conf["emulateNumpadMode"]["skiptNumbersMode"]= self.skipNumbersModeCheckbox.GetValue()
		config.conf["emulateNumpadMode"]["dismissNumpadModeByEscape"]= self.dismissNumpadModeByEscapeCheckbox.GetValue()
