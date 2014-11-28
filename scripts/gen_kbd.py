#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

root0 = './src/'
root1 = './backup/'
root2 = './custom/'
root3 = './src/'
xmldir = 'android/resources_oss/res/xml/'

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

def tag(inner, tag, attrs, indent):
	return indent + '<' + tag + attrs + ('>\n%s</%s>\n' % (inner + indent, tag) if inner else ' />\n')

# {'w': width, 'h': height, 'f': flags, '': keys}
# 'Å`' => {'': 'Å`'}
#
# keys
# {'': [key, shift|caps|flick key]}
# {'': 'Å`']	=> ['': ['latin_small_letter_Å`', 'latin_capital_letter_Å`']}
#
# key
# {'': [[mozc:keyCode, mozc:keyIcon, mozc:popUpIcon, mozc:longPressKeyCode], Å`]}
# {'': ['Å`']]	=> {'': [['uchar_Å`', 'qwerty__keyicon__Å`', 'qwerty__keyicon__Å`']]}
#
# flags
# 'f': 'k'	key_ (default: uchar_)
# 'f': 't'	twelvekeys__ (default: qwerty__)
# 'f': 'f'	__function__ (default: __keyicon__)
# 			mozc:keyBackground="twelvekeysFunction"
# 'f': 'F'	__function__ (default: __keyicon__)
# 'f': 'p'	__popup (default: )
# 			__icon (default: )
# 'f': 'i'	__icon (default: )
# 'f': '1'	__icon1 (default: )
# 'f': '2'	__icon2 (default: )
# 'f': '4'	__icon4 (default: )
# 'f': '5'	__icon5 (default: )
# 'f': 'L'	mozc:keyEdgeFlags="left"
# 'f': 'R'	mozc:keyEdgeFlags="right"
# 'f': 's'	mozc:isSticky="true"
# 'f': 'm'	mozc:isModifier="true"
# 'f': 'r'	mozc:isRepeatable="true"
# 'w': 'Å`'	mozc:keyWidth="Å`"
# 'h': 'Å`'	mozc:keyHeight="Å`"
# 
# Spacer
# 'f': 'S'	Spacer
# 'f': 'L'	mozc:stick="left"
# 'f': 'R'	mozc:stick="right"
# 'w': 'Å`'	mozc:horizontalGap="Å`"

chartype = {'kana': 'chartype_to_kana', 'alphabet': 'chartype_to_abc', 'number': 'chartype_to_123'}

keydata = {

'514': [
	[
		{'f': 'Li', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'': ['digit_zero']},
		{'f': 'i', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'i', '': ['circumflex_accent', 'tilde']},
		{'f': 'i', '': [['reverse_solidus', 'yen_sign'], 'vertical_line']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'w': '3.14%p', 'f': 'S'},
		{'f': 'L', '': 'q'},
		'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'i', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'w': '4.00%p', 'f': 'SL'},
		{'h': '36.80%p', 'f': 'Rgfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'w': '4.00%p', 'f': 'S'},
		{'f': 'L', '': 'a'},
		's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'Ri', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
	],
	[
		{'w': '14.29%p', 'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		{'w': '14.29%p', 'f': 'fkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'w': '50.00%p', 'f': 'fbkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
],

'513': [
	[
		{'f': 'Li', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'': ['digit_zero']},
		{'f': 'i', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'i', '': ['circumflex_accent', 'tilde']},
		{'f': 'Ri', '': [['reverse_solidus', 'yen_sign'], 'vertical_line']},
	],
	[
		{'w': '3.33%p', 'f': 'S'},
		{'f': 'L', '': 'q'},
		'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'Ri', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
	],
	[
		{'w': '4.36%p', 'f': 'S'},
		{'f': 'L', '': 'a'},
		's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'Ri', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'w': '15.38%p', 'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		{'w': '15.38%p', 'f': 'fkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'w': '23.08%p', 'f': 'fbkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'w': '15.38%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'512': [
	[
		{'f': 'Li', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'f': '2', '': ['digit_zero', 'vertical_line']},
		{'f': 'i', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'Ri', '': ['circumflex_accent', 'tilde']},
	],
	[
		{'f': 'L', '': 'q'},
		'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'Ri', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
	],
	[
		{'f': 'L', '': 'a'},
		's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'Ri', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
	],
	[
		{'f': 'L', '': 'z'},
		'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		{'f': 'fkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'w': '25.00%p', 'f': 'fbkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'w': '16.67%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'511': [
	[
		{'f': 'Li', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'f': '2', '': ['digit_zero', 'vertical_line']},
		{'f': 'Ri', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
	],
	[
		{'f': 'L', '': 'q'},
		'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'Ri', '': ['commercial_at', 'grave_accent']},
	],
	[
		{'f': 'L', '': 'a'},
		's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'Ri', '': ['colon', 'asterisk']},
	],
	[
		{'f': 'L', '': 'z'},
		'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': '4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		{'f': 'fkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'w': '18.18%p', 'f': 'fbkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'w': '18.18%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'510': [
	[
		{'f': 'Li', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'f': 'R2', '': ['digit_zero', 'vertical_line']},
	],
	[
		{'f': 'L', '': 'q'},
		'w', 'e', 'r', 't', 'y', 'u', 'i', 'o',
		{'f': 'R', '': 'p'},
	],
	[
		{'f': 'L', '': 'a'},
		's', 'd', 'f', 'g', 'h', 'j',
		{'f': '4', '': ['latin_small_letter_k', 'latin_capital_letter_k', ['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': '4', '': ['latin_small_letter_l', 'latin_capital_letter_l', 'commercial_at', 'grave_accent']},
		{'f': 'R5', '': ['semicolon', 'plus_sign', 'colon', 'asterisk']},
	],
	[
		{'f': 'L', '': 'z'},
		'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'R5', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		{'f': 'fkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': 'fbkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'frp', '': [['backspace', 'delete']]},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'411': [
	[
		{'f': 'L5', '': ['latin_small_letter_q', 'latin_capital_letter_q', 'digit_one', 'exclamation_mark']},
		{'f': '4', '': ['latin_small_letter_w', 'latin_capital_letter_w', 'digit_two', 'quotation_mark']},
		{'f': '4', '': ['latin_small_letter_e', 'latin_capital_letter_e', 'digit_three', 'number_sign']},
		{'f': '4', '': ['latin_small_letter_r', 'latin_capital_letter_r', 'digit_four', 'dollar_sign']},
		{'f': '4', '': ['latin_small_letter_t', 'latin_capital_letter_t', 'digit_five', 'percent_sign']},
		{'f': '4', '': ['latin_small_letter_y', 'latin_capital_letter_y', 'digit_six', 'ampersand']},
		{'f': '4', '': ['latin_small_letter_u', 'latin_capital_letter_u', 'digit_seven', 'apostrophe']},
		{'f': '4', '': ['latin_small_letter_i', 'latin_capital_letter_i', 'digit_eight', 'left_parenthesis']},
		{'f': '4', '': ['latin_small_letter_o', 'latin_capital_letter_o', 'digit_nine', 'right_parenthesis']},
		{'f': '4', '': ['latin_small_letter_p', 'latin_capital_letter_p', 'digit_zero', 'vertical_line']},
		{'f': 'R5', '': ['commercial_at', 'grave_accent', ['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
	],
	[
		{'f': 'L', '': 'a'},
		's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'Ri', '': ['colon', 'asterisk']},
	],
	[
		{'f': 'L', '': 'z'},
		'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': '4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		{'f': 'fkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'w': '18.18%p', 'f': 'fbkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'w': '18.18%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'410': [
	[
		{'f': 'L5', '': ['latin_small_letter_q', 'latin_capital_letter_q', 'digit_one', 'exclamation_mark']},
		{'f': '4', '': ['latin_small_letter_w', 'latin_capital_letter_w', 'digit_two', 'quotation_mark']},
		{'f': '4', '': ['latin_small_letter_e', 'latin_capital_letter_e', 'digit_three', 'number_sign']},
		{'f': '4', '': ['latin_small_letter_r', 'latin_capital_letter_r', 'digit_four', 'dollar_sign']},
		{'f': '4', '': ['latin_small_letter_t', 'latin_capital_letter_t', 'digit_five', 'percent_sign']},
		{'f': '4', '': ['latin_small_letter_y', 'latin_capital_letter_y', 'digit_six', 'ampersand']},
		{'f': '4', '': ['latin_small_letter_u', 'latin_capital_letter_u', 'digit_seven', 'apostrophe']},
		{'f': '4', '': ['latin_small_letter_i', 'latin_capital_letter_i', 'digit_eight', 'left_parenthesis']},
		{'f': '4', '': ['latin_small_letter_o', 'latin_capital_letter_o', 'digit_nine', 'right_parenthesis']},
		{'f': 'R5', '': ['latin_small_letter_p', 'latin_capital_letter_p', 'digit_zero', 'vertical_line']},
	],
	[
		{'f': 'L', '': 'a'},
		's', 'd', 'f', 'g', 'h', 'j',
		{'f': '4', '': ['latin_small_letter_k', 'latin_capital_letter_k', ['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': '4', '': ['latin_small_letter_l', 'latin_capital_letter_l', 'commercial_at', 'grave_accent']},
		{'f': 'R5', '': ['semicolon', 'plus_sign', 'colon', 'asterisk']},
	],
	[
		{'f': 'L', '': 'z'},
		'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'R5', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		{'f': 'fkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': 'fbkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'frp', '': [['backspace', 'delete']]},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'808': [
	[
		{'w': '6.25%p', 'f': 'S'},
		{'f': 'Li', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'f': 'i', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': '2', '': ['digit_zero', 'vertical_line']},
		{'f': 'i', '': ['circumflex_accent', 'tilde']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'w': '6.25%p', 'f': 'S'},
		{'f': 'L', '': 'q'},
		'e', 't', 'u', 'o',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': 'Lfkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		'w', 'r', 'y', 'i', 'p',
		{'f': 'i', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'w': '6.25%p', 'f': 'S'},
		{'f': 'L', '': 'a'},
		'd', 'g', 'j', 'l',
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'Rtfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		's', 'f', 'h', 'k',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'Rfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
	],
	[
		{'w': '6.25%p', 'f': 'S'},
		'z', 'c', 'b', 'm',
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
#		{'w': '6.25%p', 'f': 'SL'},
		{'f': 'Rtfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		'x', 'v', 'n',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
],

'608': [
	[
		{'w': '6.25%p', 'f': 'S'},
		{'f': 'L5', '': ['latin_small_letter_q', 'latin_capital_letter_q', 'digit_one', 'exclamation_mark']},
		{'f': '4', '': ['latin_small_letter_e', 'latin_capital_letter_e', 'digit_three', 'number_sign']},
		{'f': '4', '': ['latin_small_letter_t', 'latin_capital_letter_t', 'digit_five', 'percent_sign']},
		{'f': '4', '': ['latin_small_letter_u', 'latin_capital_letter_u', 'digit_seven', 'apostrophe']},
		{'f': '4', '': ['latin_small_letter_o', 'latin_capital_letter_o', 'digit_nine', 'right_parenthesis']},
		{'f': '4', '': ['commercial_at', 'grave_accent', ['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': '4', '': ['latin_small_letter_w', 'latin_capital_letter_w', 'digit_two', 'quotation_mark']},
		{'f': '4', '': ['latin_small_letter_r', 'latin_capital_letter_r', 'digit_four', 'dollar_sign']},
		{'f': '4', '': ['latin_small_letter_y', 'latin_capital_letter_y', 'digit_six', 'ampersand']},
		{'f': '4', '': ['latin_small_letter_i', 'latin_capital_letter_i', 'digit_eight', 'left_parenthesis']},
		{'f': '4', '': ['latin_small_letter_p', 'latin_capital_letter_p', 'digit_zero', 'vertical_line']},
		{'f': '4', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket', 'circumflex_accent', 'tilde']},
		{'f': 'Rfkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
	],
	[
		{'w': '6.25%p', 'f': 'S'},
		{'f': 'L', '': 'a'},
		'd', 'g', 'j', 'l',
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		's', 'f', 'h', 'k',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'Rtfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
	[
		{'w': '6.25%p', 'f': 'S'},
		'z', 'c', 'b', 'm',
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
#		{'w': '6.25%p', 'f': 'SL'},
		{'f': 'Rtfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		'x', 'v', 'n',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
],

'408': [
	[
		{'f': 'Lfkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': '1', '': ['digit_one', 'exclamation_mark', 'digit_two', 'quotation_mark']},
		{'f': '1', '': ['digit_three', 'number_sign', 'digit_four', 'dollar_sign']},
		{'f': '1', '': ['digit_five', 'percent_sign', 'digit_six', 'ampersand']},
		{'f': '1', '': ['digit_seven', 'apostrophe', 'digit_eight', 'left_parenthesis']},
		{'f': '1', '': ['digit_nine', 'right_parenthesis', 'digit_zero', 'vertical_line']},
		{'f': '1', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign', 'circumflex_accent', 'tilde']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Ltfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
#		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
#		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': '1', '': ['latin_small_letter_q', 'latin_capital_letter_q', 'latin_small_letter_w', 'latin_capital_letter_w']},
		{'f': '1', '': ['latin_small_letter_e', 'latin_capital_letter_e', 'latin_small_letter_r', 'latin_capital_letter_r']},
		{'f': '1', '': ['latin_small_letter_t', 'latin_capital_letter_t', 'latin_small_letter_y', 'latin_capital_letter_y']},
		{'f': '1', '': ['latin_small_letter_u', 'latin_capital_letter_u', 'latin_small_letter_i', 'latin_capital_letter_i']},
		{'f': '1', '': ['latin_small_letter_o', 'latin_capital_letter_o', 'latin_small_letter_p', 'latin_capital_letter_p']},
		{'f': '1', '': ['commercial_at', 'grave_accent', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
	[
		{'f': 'Lfaksm', '': [['alt'], ['alt']]}, # , 0, ['alt_on', 'alt'], 0, ['alt_off', 'alt']
		{'f': '1', '': ['latin_small_letter_a', 'latin_capital_letter_a', 'latin_small_letter_s', 'latin_capital_letter_s']},
		{'f': '1', '': ['latin_small_letter_d', 'latin_capital_letter_d', 'latin_small_letter_f', 'latin_capital_letter_f']},
		{'f': '1', '': ['latin_small_letter_g', 'latin_capital_letter_g', 'latin_small_letter_h', 'latin_capital_letter_h']},
		{'f': '1', '': ['latin_small_letter_j', 'latin_capital_letter_j', 'latin_small_letter_k', 'latin_capital_letter_k']},
		{'f': '1', '': ['latin_small_letter_l', 'latin_capital_letter_l', 'semicolon', 'plus_sign']},
		{'f': '1', '': ['colon', 'asterisk', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'Rfkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		{'f': '1', '': ['latin_small_letter_z', 'latin_capital_letter_z', 'latin_small_letter_x', 'latin_capital_letter_x']},
		{'f': '1', '': ['latin_small_letter_c', 'latin_capital_letter_c', 'latin_small_letter_v', 'latin_capital_letter_v']},
		{'f': '1', '': ['latin_small_letter_b', 'latin_capital_letter_b', 'latin_small_letter_n', 'latin_capital_letter_n']},
		{'f': '1', '': ['latin_small_letter_m', 'latin_capital_letter_m', ['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': '1', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'416': [
	[
		{'f': 'Lfkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': 'i', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'': ['digit_zero']},
		{'f': 'i', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'i', '': ['circumflex_accent', 'tilde']},
		{'f': 'i', '': [['reverse_solidus', 'yen_sign'], 'vertical_line']},
		{'w': '12.50%p', 'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'w': '8.75%p', 'f': 'fkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'i', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'w': '16.25%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'w': '10.00%p', 'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'i', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'w': '2.50%p', 'f': 'SL'},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
	],
	[
		{'w': '12.50%p', 'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
],

'415': [
	[
		{'f': 'Lfkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': 'Li', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'': ['digit_zero']},
		{'f': 'i', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'i', '': ['circumflex_accent', 'tilde']},
		{'f': 'i', '': [['reverse_solidus', 'yen_sign'], 'vertical_line']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'i', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'w': '13.33%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'i', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
],

'414': [
	[
		{'f': 'Lfkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': 'i', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'': ['digit_zero']},
		{'f': 'i', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'i', '': ['circumflex_accent', 'tilde']},
		{'f': 'Ri', '': [['reverse_solidus', 'yen_sign'], 'vertical_line']},
	],
	[
		{'f': 'Lfkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'i', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'i', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
#		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
#		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
],

'413': [
	[
		{'f': 'Lfkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': 'Li', '': ['digit_one', 'exclamation_mark']},
		{'f': 'i', '': ['digit_two', 'quotation_mark']},
		{'f': 'i', '': ['digit_three', 'number_sign']},
		{'f': 'i', '': ['digit_four', 'dollar_sign']},
		{'f': 'i', '': ['digit_five', 'percent_sign']},
		{'f': 'i', '': ['digit_six', 'ampersand']},
		{'f': 'i', '': ['digit_seven', 'apostrophe']},
		{'f': 'i', '': ['digit_eight', 'left_parenthesis']},
		{'f': 'i', '': ['digit_nine', 'right_parenthesis']},
		{'f': '2', '': ['digit_zero', 'vertical_line']},
		{'f': 'i', '': [['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'h': '46.00%p', 'f': 'Rgfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		'z', 'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': '4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
#		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
#		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
],

'314': [
	[
		{'f': 'Lfkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': '4', '': ['latin_small_letter_q', 'latin_capital_letter_q', 'digit_one', 'exclamation_mark']},
		{'f': '4', '': ['latin_small_letter_w', 'latin_capital_letter_w', 'digit_two', 'quotation_mark']},
		{'f': '4', '': ['latin_small_letter_e', 'latin_capital_letter_e', 'digit_three', 'number_sign']},
		{'f': '4', '': ['latin_small_letter_r', 'latin_capital_letter_r', 'digit_four', 'dollar_sign']},
		{'f': '4', '': ['latin_small_letter_t', 'latin_capital_letter_t', 'digit_five', 'percent_sign']},
		{'f': '4', '': ['latin_small_letter_y', 'latin_capital_letter_y', 'digit_six', 'ampersand']},
		{'f': '4', '': ['latin_small_letter_u', 'latin_capital_letter_u', 'digit_seven', 'apostrophe']},
		{'f': '4', '': ['latin_small_letter_i', 'latin_capital_letter_i', 'digit_eight', 'left_parenthesis']},
		{'f': '4', '': ['latin_small_letter_o', 'latin_capital_letter_o', 'digit_nine', 'right_parenthesis']},
		{'f': '4', '': ['latin_small_letter_p', 'latin_capital_letter_p', 'digit_zero', 'vertical_line']},
		{'f': '4', '': ['commercial_at', 'grave_accent', ['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': 'fkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		'z', 'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': '4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
],

'313': [
	[
		{'f': 'Lfkp', '': ['symbol']}, # , ['layout_l', 'symbol'], ['input_method', 'symbol'], ['layout_r', 'symbol'], ['mushroom', 'symbol']]},
		{'f': '4', '': ['latin_small_letter_q', 'latin_capital_letter_q', 'digit_one', 'exclamation_mark']},
		{'f': '4', '': ['latin_small_letter_w', 'latin_capital_letter_w', 'digit_two', 'quotation_mark']},
		{'f': '4', '': ['latin_small_letter_e', 'latin_capital_letter_e', 'digit_three', 'number_sign']},
		{'f': '4', '': ['latin_small_letter_r', 'latin_capital_letter_r', 'digit_four', 'dollar_sign']},
		{'f': '4', '': ['latin_small_letter_t', 'latin_capital_letter_t', 'digit_five', 'percent_sign']},
		{'f': '4', '': ['latin_small_letter_y', 'latin_capital_letter_y', 'digit_six', 'ampersand']},
		{'f': '4', '': ['latin_small_letter_u', 'latin_capital_letter_u', 'digit_seven', 'apostrophe']},
		{'f': '4', '': ['latin_small_letter_i', 'latin_capital_letter_i', 'digit_eight', 'left_parenthesis']},
		{'f': '4', '': ['latin_small_letter_o', 'latin_capital_letter_o', 'digit_nine', 'right_parenthesis']},
		{'f': '4', '': ['latin_small_letter_p', 'latin_capital_letter_p', 'digit_zero', 'vertical_line']},
		{'f': 'fkp', '': ['space']}, # , ['escape', 'space'], ['han_space', 'space'], ['tab', 'space'], ['zen_space', 'space']]},
		{'f': 'Rfrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]}, # , 0, 'caps_on', 0, ['caps_off', 'shift_off']
		'a', 's', 'd', 'f', 'g', 'h', 'j',
		{'f': '4', '': ['latin_small_letter_k', 'latin_capital_letter_k', ['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': '4', '': ['latin_small_letter_l', 'latin_capital_letter_l', 'commercial_at', 'grave_accent']},
		{'f': '4', '': ['semicolon', 'plus_sign', 'colon', 'asterisk']},
		{'w': '15.38%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['alphabet', 'kana', 'number'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]}, # , 'kana', 'preferences', 'alphabet', 'number']},
		'z', 'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': '4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
#		{'f': 'tfkrp', '': [['up', 'up_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
#		{'f': 'tfkrp', '': [['down', 'down_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]}, # , ['left', 'left_arrow'], ['up', 'up_arrow'], ['right', 'right_arrow'], ['down', 'down_arrow']]},
	],
],

}

for row, col in ((5, 14), (5, 13), (5, 12), (5, 11), (5, 10), (4, 11), (4, 10), (8, 8), (6, 8), (4, 8), (4, 16), (4, 15), (4, 14), (4, 13), (3, 14), (3, 13)):
	h = '%.2f%%p' % (92.0 / row)
	w = '%.2f%%p' % (100.0 / col)
	for mode, name in enumerate(('kbd_qwerty%d%02d_kana.xml' % (row, col), 'kbd_qwerty%d%02d_abc.xml' % (row, col), 'kbd_12keys_qwerty%d%02d_abc.xml' % (row, col))):
		keyall = keydata['%d%02d' % (row, col)]
		sourceId = 1
		xmlall = ''
		for r, keyrow in enumerate(keyall):
			xmlrow = ''
			for key in keyrow:
				xmlkey = ''
				if not isinstance(key, dict): key = {'': key}
				f = '' if 'f' not in key else key['f'][mode] if isinstance(key['f'], list) else key['f']
				if 'S' in f:
					xmlrow += tag(xmlkey, 'Spacer',
					 ' mozc:horizontalGap="%s"' % key['w']
					  + (' mozc:stick="left"'  if 'L' in f else '')
					  + (' mozc:stick="right"' if 'R' in f else ''),
					 '    ')
					continue
				k = key['']
				if not isinstance(k, list): k = ['latin_small_letter_' + k, 'latin_capital_letter_' + k]
				if 'm' not in f: k = [k] if 'f' in f or len(k) < 2 else [k, k[2:4] + k[0:2]] if '1' in f else [k, k[1:2] + k[0:1] + k[2:]]
				for index, keystate in enumerate(k):
					xmlstate = ''
					for index2, ids in enumerate(keystate):
						if ids is 0: continue
						code = ids[0] if isinstance(ids, list) else ids
						if not isinstance(code, list): code = [code, code]
						if len(code) == 2: code = [code[0], code[1], code[1]]
						icon = ids[1 if len(ids) >= 2 else 0] if isinstance(ids, list) else ids
						if not isinstance(icon, list): icon = [icon if 'f' in f or 'p' in f else ('fullwidth_' + icon), icon]
						if len(icon) == 1: icon = [icon[0], code[0]]
						if len(icon) == 2: icon = [icon[0], icon[1], icon[1]]
						popup = ids[2] if isinstance(ids, list) and len(ids) >= 3 else icon
						if not isinstance(popup, list): popup = [popup, popup, popup]
						long = ids[3] if isinstance(ids, list) and len(ids) >= 4 else ''
						if not isinstance(long, list): long = [long, long, long]
						c_prefix = 'key_' if 'k' in f and code[mode] not in ['space', 'tab'] else 'uchar_'
						i_prefix1 = 'godan__' if 'g' in f else 'twelvekeys__' if ('t' in f and icon[mode] != 'symbol') or code[mode] == 'number' else 'qwerty__'
						i_prefix2 = '' if 'm' in f and 'a' not in f else 'function__' if 'f' in f and 'b' not in f else 'keyicon__'
						i_suffix = '' if 'f' not in f and code[mode] not in ['han_space', 'zen_space', 'tab'] and index2 else '__icon5' if '5' in f else '__icon4' if '4' in f else '__icon2' if '2' in f else '__icon1' if '1' in f else '__icon' if 'i' in f or 'p' in f or 'a' in f else ''
						p_prefix1 = 'twelvekeys__' if ('t' in f and icon[mode] != 'symbol') or code[mode] == 'number' else 'qwerty__'
						p_prefix2 = 'function__' if 'f' in f and 'b' not in f else 'keyicon__'
						p_suffix = '__popup' if 'p' in f else '' if code[mode] not in ['han_space', 'zen_space', 'tab'] and index2 else '__icon5' if '5' in f else '__icon4' if '4' in f else '__icon2' if '2' in f else '__icon1' if '1' in f else '__icon' if 'i' in f else ''
						xml = '' if 'm' in f else tag('', 'PopUp', ' mozc:popUpIcon="@raw/%s"' % (p_prefix1 + p_prefix2 + popup[mode] + p_suffix), '            ')
						xml = tag(xml, 'KeyEntity', ''' mozc:sourceId="%%d"%(high)s%(long)s
                     mozc:keyCode="@integer/%(code)s"
                     mozc:keyIcon="@raw/%(icon)s"''' % {
							'high': ' mozc:flickHighlight="true"' if 'f' not in f and row <= 5 else '',
							'long': '''
                     mozc:longPressKeyCode="@integer/%s"''' % (c_prefix + long[mode]) if long[mode] else '',
							'code': c_prefix + (chartype[code[mode]] if code[mode] in chartype else code[mode]),
							'icon': i_prefix1 + i_prefix2 + icon[mode] + i_suffix
						}, '          ')
						if 'f' in f:
							direct = '' if not index2 else 'left' if index2 == 1 else 'up' if index2 == 2 else 'right' if index2 == 3 else 'down'
						elif '1' in f:
							direct = '' if not index2 else 'up' if index2 == 1 else 'down' if index2 == 3 else 'left' if index else 'right'
						else:
							direct = '' if not index2 else 'left' if index2 == 2 else 'right' if index2 == 3 else 'down' if index else 'up'
						xmlstate += tag(xml % sourceId, 'Flick', (' mozc:direction="%s"' % direct) if direct else '', '        ')
						sourceId += 1
						if 'f' not in f and '1' not in f and (('L' in f and index2 == 2) or ('R' in f and index2 == 3)):
							xmlstate += tag(xml % sourceId, 'Flick', ' mozc:direction="%s"' % ('up' if index else 'down'), '        ')
							sourceId += 1
					xmlkey += tag(xmlstate, 'KeyState', [
						[
							[
								'',
								' mozc:metaState="shift|capsLock"',
							],
							[
								' mozc:nextMetaState="shift"',
								' mozc:metaState="shift" mozc:nextMetaState="capsLock"',
								' mozc:metaState="capsLock" mozc:nextMetaState="unmodified"',
							],
						],
						[
							[
								'',
								' mozc:metaState="alt"',
							],
							[
								' mozc:nextMetaState="alt"\n                mozc:keyBackground="twelvekeysFunctionLightOff"',
								' mozc:metaState="alt" mozc:nextMetaState="unmodified"\n                mozc:keyBackground="twelvekeysFunctionLightOn"',
							],
						],
					][1 if '1' in f or 'a' in f else 0][1 if 'm' in f else 0][index], '      ')
				xmlrow += tag(xmlkey, 'Key',
				 ((' mozc:keyBackground="penta%s%s' % ('U' if r % 2 else 'D', 'Function"\n        ' if 'f' in f and 'b' not in f else 'Regular"')) if row >= 6 else ' mozc:keyBackground="twelvekeysFunction"\n        ' if 'a' not in f and 'f' in f and 'b' not in f else '')
				  + (' mozc:keyWidth="%s"'  % (key['w']) if 'w' in key else '')
				  + (' mozc:keyHeight="%s"' % (key['h']) if 'h' in key else '')
				  + (' mozc:keyEdgeFlags="left"'  if 'L' in f else '')
				  + (' mozc:keyEdgeFlags="right"' if 'R' in f else '')
				  + (' mozc:isSticky="true"'      if 's' in f else '')
				  + (' mozc:isModifier="true"'    if 'm' in f else '')
				  + (' mozc:isRepeatable="true"'  if 'r' in f else ''),
				 '    ')
			xmlall += tag(xmlrow, 'Row', '', '  ')
		xmlall = '''\
<?xml version="1.0" encoding="utf-8"?>
<!--
 Copyright 2010-2013, Google Inc.
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are
 met:

     * Redistributions of source code must retain the above copyright
 notice, this list of conditions and the following disclaimer.
     * Redistributions in binary form must reproduce the above
 copyright notice, this list of conditions and the following disclaimer
 in the documentation and/or other materials provided with the
 distribution.
     * Neither the name of Google Inc. nor the names of its
 contributors may be used to endorse or promote products derived from
 this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
-->
<Keyboard
    xmlns:mozc="http://schemas.android.com/apk/res-auto"
    mozc:flickThreshold="32dip"
    mozc:keyBackground="twelvekeysRegular"
    mozc:keyWidth="%s" mozc:keyHeight="%s"
    mozc:horizontalGap="0dip" mozc:verticalGap="0dip"
    mozc:popUpWidth="@dimen/key_preview_height" mozc:popUpHeight="@dimen/key_preview_height"
    mozc:popUpXOffset="0dip" mozc:popUpYOffset="@dimen/mini_keyboard_vertical_correction">
  <Row mozc:rowEdgeFlags="top" mozc:keyHeight="0dip" mozc:verticalGap="4%%p" />
%s  <!-- Next sourceId: %d -->
</Keyboard>
''' % (w, h, xmlall, sourceId)	#    mozc:horizontalGap="0.2%%p" mozc:verticalGap="2%%p"
		save(root2 + xmldir + name, xmlall)
		save(root3 + xmldir + name, xmlall)
