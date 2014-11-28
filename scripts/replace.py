#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, re

myapp = {
	'appid': 'mozc.android.yourname.yourappname',
	'apkfile': 'YourAppName',
	'appname_en': 'YourAppName',
	'appname_ja': 'YourAppName',
	'fullname_en': 'YourAppName for Android',
	'fullname_ja': 'YourAppName for Android',
	'developer_en': 'Mozc Project Team / Customized by YourName',
	'developer_ja': 'Mozc Project Team / Customized by YourName',
	't_url': 'http://code.google.com/p/mozc/',
	'p_url': 'http://code.google.com/p/mozc/',
}

'''
myapp = {
	'appid': 'org.mozc.android.inputmethod.japanese',
	'apkfile': 'MozcForAndroid',
	'appname_en': 'Mozc',
	'appname_ja': 'Mozc',
	'fullname_en': 'Mozc for Android',
	'fullname_ja': 'Mozc for Android',
	'developer_en': 'Mozc Project Team',
	'developer_ja': 'Mozc Project Team',
	't_url': 'http://code.google.com/p/mozc/',
	'p_url': 'http://code.google.com/p/mozc/',
}
'''

kbds = ('514', '513', '512', '511', '510', '411', '410', '808', '608', '408', '416', '415', '414', '413', '314', '313')

root0 = './src/'
root1 = './backup/'
root2 = './custom/'
root3 = './src/'
root4 = './search/'
root5 = './replace/'

def load(path):
	if not os.path.isfile(path): return None
	f = open(path, 'r')
	text = f.read()
	f.close()
	return text;

def save(path, text):
	if text is None or load(path) == text: return
	if not os.path.isdir(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
	f = open(path, 'w')
	f.write(text)
	f.close()

def eachkbd(part):
	text = ''
	for kbd in kbds: text += part % {'kbd': kbd}
	return text;

paths = {}
for root, dirs, files in os.walk(root5):
	for file in files:
		if '.each' in file: continue
		m = re.search(r'^(.+?)\.(\w+)(?:\.(\d+))?$', file)
		path = re.sub('^' + root5, '', root)
		path = path + ('/' if path else '') + m.group(1)
		custom = m.group(2)
		if custom not in sys.argv[1:]: continue
		if m.group(3):
			if path not in paths: paths[path] = {}
			if custom not in paths[path]: paths[path][custom] = {}
			paths[path][custom][m.group(3)] = True
			continue
		text = load(root5 + path + '.' + custom)
		text = (text % myapp) if custom == 'fix_myapp' else text
		if path == 'MozcService.java': path = 'android/src/' + myapp['appid'].replace('.', '/') + '/' + path
		print path + ' ' + custom + ' generate'
		save(root2 + path, text)
		save(root3 + path, text)
for root, dirs, files in os.walk(root0 + 'android/resources_oss/res/xml/'):
	for file in files:
		if not re.search(r'^kbd_\w+\.xml$', file): continue
		path = re.sub('^' + root0, '', root) + file
		custom = 'add_flick'
		if path not in paths: paths[path] = {}
		if custom not in paths[path]: paths[path][custom] = {}
		paths[path][custom]['0'] = True
for path, customs in sorted(paths.iteritems()):
	print path,
	if not os.path.isfile(root1 + path): save(root1 + path, load(root0 + path.replace('AlphabetLayoutPreference.java', 'KeyboardLayoutPreference.java')))
	text = load(root1 + path)
	if text is None: continue
	for custom, indexes in sorted(customs.iteritems()):
		print custom,
		for index in sorted(indexes, key = int):
			print index,
			pathn = path + '.' + custom + '.' + index
			pathe = root5 + pathn + '.each'
			t = load(root5 + pathn)
			if t is None: continue
			text2 = text.replace(load(root4 + pathn), t + eachkbd(load(pathe)) if os.path.isfile(pathe) else (t % myapp) if custom == 'fix_myapp' else t)
			if text == text2: print '(unmatch)',
			text = text2
	print
	if re.search(r'^android/resources_oss/res/xml/kbd_\w+\.xml$', path):
		text = text.replace('"/>', '" />')
		text = text.replace('\t', '  ')
		text = text.replace('''
  </Row>
</Keyboard>
''', '''
  </Row>
  <!-- Next sourceId: 0 -->
</Keyboard>
''')
	if re.search(r'^android/resources_oss/res/xml/kbd_\w+\.xml$', path) and 'add_flick' in sys.argv[1:]:
		text = re.sub(r'''
        <Flick>
          <KeyEntity mozc:sourceId="\d+"
                     mozc:keyCode="@integer/key_(left|right|up|down)"
                     mozc:keyIcon="@raw/(twelvekeys|godan)__function__\1_arrow__icon">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__\1_arrow__popup" />
          </KeyEntity>
        </Flick>
''', r'''
        <Flick>
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_\1"
                     mozc:keyIcon="@raw/\2__function__\1_arrow__icon">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__\1_arrow__popup" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="left">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_left"
                     mozc:keyIcon="@raw/\2__function__left_arrow__icon">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__left_arrow__popup" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="up">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_up"
                     mozc:keyIcon="@raw/\2__function__up_arrow__icon">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__up_arrow__popup" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="right">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_right"
                     mozc:keyIcon="@raw/\2__function__right_arrow__icon">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__right_arrow__popup" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="down">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_down"
                     mozc:keyIcon="@raw/\2__function__down_arrow__icon">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__down_arrow__popup" />
          </KeyEntity>
        </Flick>
''', text)
		text = re.sub(r'''
        <Flick>
          <KeyEntity mozc:sourceId="\d+"
                     mozc:keyCode="@integer/uchar_space"
                     mozc:keyIcon="@raw/(twelvekeys|godan|qwerty)__(function|keyicon)__space__icon">
            <PopUp mozc:popUpIcon="@raw/qwerty__\2__space__popup" />
          </KeyEntity>
        </Flick>
''', r'''
        <Flick>
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/uchar_space"
                     mozc:keyIcon="@raw/\1__\2__space__icon5">
            <PopUp mozc:popUpIcon="@raw/qwerty__\2__space__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="left">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/uchar_escape"
                     mozc:keyIcon="@raw/\1__\2__escape__icon">
            <PopUp mozc:popUpIcon="@raw/qwerty__\2__escape__popup" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="up">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_han_space"
                     mozc:keyIcon="@raw/\1__\2__space__icon5">
            <PopUp mozc:popUpIcon="@raw/qwerty__\2__space__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="right">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/uchar_tab"
                     mozc:keyIcon="@raw/\1__\2__tab__icon">
            <PopUp mozc:popUpIcon="@raw/qwerty__\2__tab__popup" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="down">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_zen_space"
                     mozc:keyIcon="@raw/\1__\2__space__icon5">
            <PopUp mozc:popUpIcon="@raw/qwerty__\2__space__popup5" />
          </KeyEntity>
        </Flick>
''', text)
		text = re.sub(r'''
        <Flick>
          <KeyEntity mozc:sourceId="\d+"
                     mozc:keyCode="@integer/key_(symbol|chartype_to_kana_123|chartype_to_abc_123)"
                     mozc:keyIcon="@raw/(twelvekeys|godan|qwerty)__function__(symbol|number_kana|number_alphabet)__icon">
            <PopUp mozc:popUpIcon="@raw/qwerty__function__\3__popup" />
          </KeyEntity>
        </Flick>
''', r'''
        <Flick>
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_\1"
                     mozc:keyIcon="@raw/\2__function__\3__icon5">
            <PopUp mozc:popUpIcon="@raw/qwerty__function__\3__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="left">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_layout_l"
                     mozc:keyIcon="@raw/\2__function__\3__icon5">
            <PopUp mozc:popUpIcon="@raw/qwerty__function__\3__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="up">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_input_method"
                     mozc:keyIcon="@raw/\2__function__input_method__icon">
            <PopUp mozc:popUpIcon="@raw/qwerty__function__input_method__popup" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="right">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_layout_r"
                     mozc:keyIcon="@raw/\2__function__\3__icon5">
            <PopUp mozc:popUpIcon="@raw/qwerty__function__\3__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="down">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_mushroom"
                     mozc:keyIcon="@raw/\2__function__mushroom__icon">
            <PopUp mozc:popUpIcon="@raw/qwerty__function__mushroom__popup" />
          </KeyEntity>
        </Flick>
''', text)
		text = re.sub(r'''
        <Flick>
          <KeyEntity mozc:sourceId="\d+"
                     mozc:keyCode="@integer/key_chartype_to_(kana|abc|123)"
                     mozc:longPressKeyCode="@integer/key_menu_dialog"
                     mozc:keyIcon="@raw/(twelvekeys|godan|qwerty)__function__(kana|alphabet|number|text_kana|text_alphabet)__icon">
            <PopUp mozc:popUpIcon="@raw/(twelvekeys|godan|qwerty)__function__(kana|alphabet|number|text_kana|text_alphabet)__popup" />
          </KeyEntity>
        </Flick>
''', r'''
        <Flick>
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:longPressKeyCode="@integer/key_menu_dialog"
                     mozc:keyCode="@integer/key_chartype_to_\1"
                     mozc:keyIcon="@raw/\2__function__\3__icon5">
            <PopUp mozc:popUpIcon="@raw/%s__function__\5__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="left">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_chartype_to_kana"
                     mozc:keyIcon="@raw/\2__function__kana__icon5">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__kana__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="up">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_preferences"
                     mozc:keyIcon="@raw/\2__function__preferences__icon">
            <PopUp mozc:popUpIcon="@raw/qwerty__function__preferences__popup" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="right">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_chartype_to_abc"
                     mozc:keyIcon="@raw/\2__function__alphabet__icon5">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__alphabet__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="down">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_chartype_to_%s123"
                     mozc:keyIcon="@raw/\2__function__number__icon5">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__number__popup5" />
          </KeyEntity>
        </Flick>
''' % ('qwerty' if re.search(r'kbd_qwerty_(kana_123|abc_123)\.xml$', path) else 'twelvekeys', 'kana_' if re.search(r'kbd_qwerty_(kana|abc_123)\.xml$', path) else 'abc_' if re.search(r'kbd_qwerty_(abc|kana_123)\.xml$', path) else ''), text)
		text = re.sub(r'''
        <Flick>
          <KeyEntity mozc:sourceId="\d+"
                     mozc:longPressKeyCode="@integer/key_menu_dialog"
                     mozc:keyCode="@integer/key_chartype_to_(kana|abc|123)"
                     mozc:keyIcon="@raw/(twelvekeys|godan|qwerty)__function__(kana|alphabet|number|text_kana|text_alphabet)__icon">
            <PopUp mozc:popUpIcon="@raw/(twelvekeys|godan|qwerty)__function__(kana|alphabet|number|text_kana|text_alphabet)__popup" />
          </KeyEntity>
        </Flick>
''', r'''
        <Flick>
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:longPressKeyCode="@integer/key_menu_dialog"
                     mozc:keyCode="@integer/key_chartype_to_\1"
                     mozc:keyIcon="@raw/\2__function__\3__icon5">
            <PopUp mozc:popUpIcon="@raw/%s__function__\5__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="left">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_chartype_to_kana"
                     mozc:keyIcon="@raw/\2__function__kana__icon5">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__kana__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="up">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_preferences"
                     mozc:keyIcon="@raw/\2__function__preferences__icon">
            <PopUp mozc:popUpIcon="@raw/qwerty__function__preferences__popup" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="right">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_chartype_to_abc"
                     mozc:keyIcon="@raw/\2__function__alphabet__icon5">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__alphabet__popup5" />
          </KeyEntity>
        </Flick>
        <Flick mozc:direction="down">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_chartype_to_%s123"
                     mozc:keyIcon="@raw/\2__function__number__icon5">
            <PopUp mozc:popUpIcon="@raw/twelvekeys__function__number__popup5" />
          </KeyEntity>
        </Flick>
''' % ('qwerty' if re.search(r'kbd_qwerty_(kana_123|abc_123)\.xml$', path) else 'twelvekeys', 'kana_' if re.search(r'kbd_qwerty_(kana|abc_123)\.xml$', path) else 'abc_' if re.search(r'kbd_qwerty_(abc|kana_123)\.xml$', path) else ''), text)
		text = re.sub(r'''
        <Flick>
          <KeyEntity mozc:sourceId="\d+"
                     mozc:keyCode="@integer/key_capslock"
                     mozc:keyIcon="@raw/qwerty__(shift_off|shift_on|caps_on)" />
        </Flick>
''', r'''
        <Flick>
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_capslock"
                     mozc:keyIcon="@raw/qwerty__\1" />
        </Flick>
        <Flick mozc:direction="up">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_caps_on"
                     mozc:keyIcon="@raw/qwerty__caps_on" />
        </Flick>
        <Flick mozc:direction="down">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_caps_off"
                     mozc:keyIcon="@raw/qwerty__shift_off" />
        </Flick>
''', text)
		text = re.sub(r'''
        <Flick>
          <KeyEntity mozc:sourceId="\d+"
                     mozc:keyCode="@integer/key_alt"
                     mozc:keyIcon="@raw/qwerty__function__alt__icon" />
        </Flick>
''', r'''
        <Flick>
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_alt"
                     mozc:keyIcon="@raw/qwerty__function__alt__icon" />
        </Flick>
        <Flick mozc:direction="up">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_alt_on"
                     mozc:keyIcon="@raw/qwerty__function__alt__icon" />
        </Flick>
        <Flick mozc:direction="down">
          <KeyEntity mozc:sourceId="0" mozc:flickHighlight="true"
                     mozc:keyCode="@integer/key_alt_off"
                     mozc:keyIcon="@raw/qwerty__function__alt__icon" />
        </Flick>
''', text)
	if re.search(r'^android/resources_oss/res/xml/kbd(_12keys)?_qwerty[68]08_(kana|abc)\.xml$', path): text = text.replace(' mozc:flickHighlight="true"', '')
	if re.search(r'^android/resources_oss/res/xml/kbd_\w+\.xml$', path):
		count = 0
		def countup(m2):
			global count
			count += 1
			return 'mozc:sourceId="' + str(count) + '"'
		text = re.sub(r'mozc:sourceId="\d+"', countup, text)
		count += 1
		text = re.sub(r'<!-- Next sourceId: \d+ -->', '<!-- Next sourceId: ' + str(count) + ' -->', text)
	save(root2 + path, text)
	save(root3 + path, text)

