# navigate The numpad Way #

*	Author: Ibrahim Hamadeh
*	Download [version 1.3][1]
*	NVDA compatibility: 2019.3 and later

## Introduction

This addon was made in response to a request from a user, that does not have a numeric keypad or numpad keys on his keyboard.
 Thus allowing him to benefit from the navigation feature of numpad keys.  

So I think this addon will mostly be of interest for users that do not have a numeric keypad in their computer.
 You can choose one of the available forms or set of keys on the main keyboard, to have them emulate the numpad keys and their related commands, regarding review or object navigation.

## Usage

After installing the addon, you will have three modes

Normal, Numpad and numbers mode, numbers mode is skipped by default, so mainly we have two modes normal and numpad .

you can toggle between these modes by Shift+NVDA+f4 shortcut. And as always you can modify this shortcut going to NVDA menu/preferences/input gestures/navigate The numpad Way.

The available forms that you can emulate them to numpad mode are

*	form1:  
q w e  
a s d  
z x c  

*	form2:  
e r t  
d f g  
c v b  
*	form3:  
y u i  
h j k  
n m ,  

*	form4:  
7 8 9  
u i o  
j k l

Every one of these forms will emulate

numpad7 numpad8 numpad9  
numpad4 numpad5 numpad6  
numpad1 numpad2 numpad3  

Emulating their review or object navigation, used alone or with conjuction with the shift or NVDA keys.

## Addon Settings ##

To access addon settings, go to: NVDA menu/preferences,  
hit enter then e to go to navigate the numpad way panel.

*	Choose form to emulate to numpad mode combo box: From here you can choose the form you like to emulate to numpad mode, and Form1 is chosen by default.
*	Next you will stand on a multi edit text control: it will help you to view the form you have selected, and you can use up and down arrows to navigate.
*	Skip Options combo box, this allows you to choose either Skip numbers mode, Skip Numpad mode, or keep both modes active.  
*	Dismiss numpadMode by escape key check box: it is checked by default, so that you can return to normal mode either by the toggle gesture of the addon(Shift+NVDA+F4 by default), or the escape key.

Final note:  
Sometimes some addons may grab one or more of the gestures of the form. Hope you can manage that by either using another form, or removing the gesture from the theif addon, for until now I do not have other solutions.

### Changes for 1.3 ###

*	Update last tested version, thus making the addon compatible with NVDA 2025.1.

### Changes for 1.2 ###

*	Update Turkish translation, by Umut KORKMAZ.

### Changes for 1.1 ###

*	Use from gui.settingsDialogs import SettingsPanel, to get rid of warning messages in the log.

### Changes for 1.0 ###

*	Rename the addon to navigate the numpad way, for there are addons, that their names very close to the previous names of the addon, thus renaming the addon make things clearer. 
*	Update last tested version, thus making the addon compatible with NVDA 2024.1.

### Changes for 0.9 ###

*	Fix a bug in numbers mode, related to position of number 0, in third and fourth forms.
*	Update last tested version, thus making the addon compatible with NVDA 2023.1.

### Changes for 0.8 ###

*	Make a combo box instead of check box, to skipp either Numbers mode, Numpad mode, or keep both.  
*	Add a new form(q w e, a s d, z x c), and put it as form1.

### Changes for 0.7 ###

*	Add Portuguese translation for the addon.
*	Change the default gesture or shortcut for the addon, it is now Shift+NVDA+F4.

### Changes for 0.6 ###
The addon was updated introducing lot of new ffeatures

*	Make a setting panel for the addon.
*	Now three forms are available to be emulated to numpad mode, and you can choose one of them.
*	Numbers mode is now skipped by default, and you may change that from addon settings.
*	Now you can dismiss numpad mode by escape key, and this also can be accessed and changed from addon settings.

### Changes for 0.5 ###

*	Update last tested version, to comply with NVDA 2022.1 API.

### Changes for 0.4 ###

*	Add Turkish translation.

### Contributions ###

*	umut korkmaz, thanks for supporting the Turkish translation of the addon.
*	Ângelo Abrantes, thanks for supporting the Portuguese translation of the addon.

[1]: https://github.com/ibrahim-s/navigateTheNumpadWay/releases/download/1.3/navigateTheNumpadWay-1.3.nvda-addon
