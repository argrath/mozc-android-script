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

kbds = ('514', '513', '512', '511', '510', '411', '410', '416', '415', '414', '413', '314', '313')

root0 = './src/'
root1 = './backup/'
root2 = './custom/'
root3 = './src/'
root4 = './search/'
root5 = './replace/'

def load(path):
	f = open(path, 'r')
	text = f.read()
	f.close()
	return text;

def save(path, text):
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
		text = load(root5 + path + '.' + custom) % myapp
		path = 'android/src/' + myapp['appid'].replace('.', '/') + '/' + path
		print path + ' ' + custom + ' generate'
		save(root2 + path, text)
		save(root3 + path, text)
for path, customs in sorted(paths.iteritems()):
	print path,
	if not os.path.isfile(root1 + path): save(root1 + path, load(root0 + path.replace('AlphabetLayoutPreference.java', 'KeyboardLayoutPreference.java')))
	text = load(root1 + path)
	for custom, indexes in sorted(customs.iteritems()):
		print custom,
		for index in sorted(indexes, key = int):
			print index,
			pathn = path + '.' + custom + '.' + index
			pathe = root5 + pathn + '.each'
			t = load(root5 + pathn)
			text2 = text.replace(load(root4 + pathn), t + eachkbd(load(pathe)) if os.path.isfile(pathe) else (t % myapp) if custom == 'fix_myapp' else t)
			if text == text2: print '(unmatch)',
			text = text2
	print
	save(root2 + path, text)
	save(root3 + path, text)

