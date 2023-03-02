# -*- coding: utf-8 -*-
# Emulate Numpad Mode/forms.py
# Copyright (C) 2021 ibrahim hamadeh
# This add-on is free software, licensed under the terms of the GNU General Public License (version 2).
# See the file COPYING for more details.

import config
from typing import List, Dict

# the general dictionary, that maps numpad commands or keys to their related scripts.
generalDict= {
	"{numpad7}": "script_review_previousLine",
	"{numpad8}": "script_review_currentLine",
	"{numpad9}": "script_review_nextLine",
	"{numpad4}": "script_review_previousWord",
	"{numpad5}": "script_review_currentWord",
	"{numpad6}": "script_review_nextWord",
	"{numpad1}": "script_review_previousCharacter",
	"{numpad2}": "script_review_currentCharacter",
	"{numpad3}": "script_review_nextCharacter",
	"NVDA+{numpad7}": "script_reviewMode_next",
	"NVDA+{numpad1}": "script_reviewMode_previous",
	"NVDA+{numpad5}": "script_navigatorObject_current",
	"NVDA+{numpad8}": "script_navigatorObject_parent",
	"NVDA+{numpad6}": "script_navigatorObject_next",
	"NVDA+{numpad4}": "script_navigatorObject_previous",
	"NVDA+{numpad2}": "script_navigatorObject_firstChild",
	"shift+{numpad7}": "script_review_top",
	"shift+{numpad9}": "script_review_bottom",
	"shift+{numpad1}": "script_review_startOfLine",
	"shift+{numpad3}": "script_review_endOfLine",
	"shift+{numpad2}": "script_reportFocusObjectAccelerator"
}

class Forms:
	''' Helper class that deals with various or available forms and their alternative numpad scripts or gestures.'''

# form1 dictionary, that maps numpad keys to their alternative set of keys on main keyboard that should be emulated.
	form1= {
	'numpad7': 'q',
	'numpad8': 'w',
	'numpad9': 'e',
	'numpad4': 'a',
	'numpad5': 's',
	'numpad6': 'd',
	'numpad1': 'z',
	'numpad2': 'x',
	'numpad3': 'c'
	}

	# form2 dictionary, that maps numpad keys to their alternative set of keys on main keyboard that should be emulated.
	form2= {
	'numpad7': 'e',
	'numpad8': 'r',
	'numpad9': 't',
	'numpad4': 'd',
	'numpad5': 'f',
	'numpad6': 'g',
	'numpad1': 'c',
	'numpad2': 'v',
	'numpad3': 'b'
	}

	# form3 dictionary, that maps numpad keys to their alternative set of keys on main keyboard that should be emulated.
	form3= {
	'numpad7': 'y',
	'numpad8': 'u',
	'numpad9': 'i',
	'numpad4': 'h',
	'numpad5': 'j',
	'numpad6': 'k',
	'numpad1': 'n',
	'numpad2': 'm',
	'numpad3': ','
	}

	# form4 dictionary, that maps numpad keys to their alternative set of keys on main keyboard that should be emulated.
	form4= {
	'numpad7': '7',
	'numpad8': '8',
	'numpad9': '9',
	'numpad4': 'u',
	'numpad5': 'i',
	'numpad6': 'o',
	'numpad1': 'j',
	'numpad2': 'k',
	'numpad3': 'l'
	}

	forms= (form1, form2, form3, form4)
	def __init__(self) -> None:
		self._index= config.conf["emulateNumpadMode"]["formChosen"]
		self._form= self.forms[self._index]

	@property
	def _numpadDict(self) -> Dict[str, str]:
		''' Returns a dictionary for the selected form, that maps keys or commands on main keyboard to their alternative numpad scripts.'''
		selectedForm= self._form
		d= {key.format(**selectedForm): value for key, value in generalDict.items()}
		return d

	@property
	def _numbersDict(self) -> Dict[str, str]:
		''' Return a dictionary, that maps the selecte form or set of keys on main keyboard to numbers 0 to 9.'''
		selectedForm= self._form
		# mapping keys to numbers dictionary
		d= {key: value for key, value in zip(selectedForm.values(), '789456123')}
		# map a key for each form to 0, and update the dictionary.
		if self._index== 3: # fourth form selected
			d.update(m= '0')
		# if form1 or form2or form3 is selected
		else:
			d.update(space= '0')
		return d

	def getKeyNames(self, form= None) -> str:
		''' Getting the names of the keys in the selected portion or form in main keyboard.'''
		selectedForm= self._form if not form else form
		keyValues= [value for key, value in selectedForm.items()]
		line1=' ; '.join(keyValues[:3])
		line2= ' ; '.join(keyValues[3: 6])
		line3= ' ; '.join(keyValues[6:])
		return line1+'\n'+ line2 + '\n' +line3

	@property
	def allKeyNames(self) -> List[str]:
		''' Getting a list of key names in all available forms.'''
		_list= [self.getKeyNames(form) for form in self.forms]
		return _list
