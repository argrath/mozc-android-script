#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

root0 = './src/'
root1 = './backup/'
root2 = './custom/'
root3 = './src/'
xmldir = 'android/resources_oss/res/xml/'

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

def tag(inner, tag, attrs, indent):
	return indent + '<' + tag + attrs + ('>\n%s</%s>\n' % (inner + indent, tag) if inner else ' />\n')

# {'w': width, 'h': height, 'f': flags, '': keys}
# '`' => {'': '`'}
#
# keys
# {'': [key, shift|caps|flick key]}
# {'': '`']	=> ['': ['latin_small_letter_`', 'latin_capital_letter_`']}
#
# key
# {'': [[mozc:keyCode, mozc:keyIcon, mozc:popUpIcon, mozc:longPressKeyCode], `]}
# {'': ['`']]	=> {'': [['uchar_`', 'qwerty__keyicon__`', 'qwerty__keyicon__`']]}
#
# flags
# 'f': 'k'	key_ (default: uchar_)
# 'f': 't'	twelvekeys__ (default: qwerty__)
# 'f': 'f'	__function__ (default: __keyicon__)
# 			mozc:keyBackground="qwertyFunction"
# 'f': 'p'	__popup (default: )
# 			__icon (default: )
# 'f': 'i'	__icon (default: )
# 'f': '2'	__icon2 (default: )
# 'f': '4'	__icon4 (default: )
# 'f': 'b'	mozc:keyBackground="qwertyFunction"
# 'f': 'L'	mozc:keyEdgeFlags="left"
# 'f': 'R'	mozc:keyEdgeFlags="right"
# 'f': 's'	mozc:isSticky="true"
# 'f': 'm'	mozc:isModifier="true"
# 'f': 'r'	mozc:isRepeatable="true"
# 'w': '`'	mozc:keyWidth="`"
# 'h': '`'	mozc:keyHeight="`"
# 
# Spacer
# 'f': 'S'	Spacer
# 'f': 'L'	mozc:stick="left"
# 'f': 'R'	mozc:stick="right"
# 'w': '`'	mozc:horizontalGap="`"

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
		{'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'w': '3.14%p', 'f': 'S'},
		{'f': 'L', '': 'q'},
		'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'i', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'w': '4.00%p', 'f': 'SR'},
		{'h': '39%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
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
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
		{'f': 'Rfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
	],
	[
		{'w': '14.29%p', 'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
#		{'f': 'fkp', '': [['chartype_to_abc_123', 'number_alphabet']]},
#		{'f': 'fkp', '': [['chartype_to_kana_123', 'number_kana']]},
#		{'f': 'fkp', '': [['chartype_to_abc', 'text_alphabet', '', 'menu_dialog']]},
#		{'f': 'fkp', '': [['chartype_to_kana', 'text_kana', '', 'menu_dialog']]},
		{'w': '14.29%p', 'f': 'fkp', '': ['symbol']},
		{'w': '50.00%p', 'f': 'p', '': ['space']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]},
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
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'w': '15.38%p', 'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		{'w': '15.38%p', 'f': 'fkp', '': ['symbol']},
		{'w': '23.08%p', 'f': 'p', '': ['space']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]},
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
		{'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		{'f': 'fkp', '': ['symbol']},
		{'w': '25.00%p', 'f': 'p', '': ['space']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]},
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
		{'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		{'f': 'fkp', '': ['symbol']},
		{'w': '18.18%p', 'f': 'p', '': ['space']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]},
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
		{'f': 'R4', '': ['semicolon', 'plus_sign', 'colon', 'asterisk']},
	],
	[
		{'f': 'L', '': 'z'},
		'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'R4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		{'f': 'fkp', '': ['symbol']},
		{'f': 'p', '': ['space']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]},
		{'f': 'fkrp', '': [['backspace', 'delete']]},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'411': [
	[
		{'f': 'L4', '': ['latin_small_letter_q', 'latin_capital_letter_q', 'digit_one', 'exclamation_mark']},
		{'f': '4', '': ['latin_small_letter_w', 'latin_capital_letter_w', 'digit_two', 'quotation_mark']},
		{'f': '4', '': ['latin_small_letter_e', 'latin_capital_letter_e', 'digit_three', 'number_sign']},
		{'f': '4', '': ['latin_small_letter_r', 'latin_capital_letter_r', 'digit_four', 'dollar_sign']},
		{'f': '4', '': ['latin_small_letter_t', 'latin_capital_letter_t', 'digit_five', 'percent_sign']},
		{'f': '4', '': ['latin_small_letter_y', 'latin_capital_letter_y', 'digit_six', 'ampersand']},
		{'f': '4', '': ['latin_small_letter_u', 'latin_capital_letter_u', 'digit_seven', 'apostrophe']},
		{'f': '4', '': ['latin_small_letter_i', 'latin_capital_letter_i', 'digit_eight', 'left_parenthesis']},
		{'f': '4', '': ['latin_small_letter_o', 'latin_capital_letter_o', 'digit_nine', 'right_parenthesis']},
		{'f': '4', '': ['latin_small_letter_p', 'latin_capital_letter_p', 'digit_zero', 'vertical_line']},
		{'f': 'R4', '': ['commercial_at', 'grave_accent', ['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
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
		{'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		{'f': 'fkp', '': ['symbol']},
		{'w': '18.18%p', 'f': 'p', '': ['space']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]},
		{'w': '18.18%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'410': [
	[
		{'f': 'L4', '': ['latin_small_letter_q', 'latin_capital_letter_q', 'digit_one', 'exclamation_mark']},
		{'f': '4', '': ['latin_small_letter_w', 'latin_capital_letter_w', 'digit_two', 'quotation_mark']},
		{'f': '4', '': ['latin_small_letter_e', 'latin_capital_letter_e', 'digit_three', 'number_sign']},
		{'f': '4', '': ['latin_small_letter_r', 'latin_capital_letter_r', 'digit_four', 'dollar_sign']},
		{'f': '4', '': ['latin_small_letter_t', 'latin_capital_letter_t', 'digit_five', 'percent_sign']},
		{'f': '4', '': ['latin_small_letter_y', 'latin_capital_letter_y', 'digit_six', 'ampersand']},
		{'f': '4', '': ['latin_small_letter_u', 'latin_capital_letter_u', 'digit_seven', 'apostrophe']},
		{'f': '4', '': ['latin_small_letter_i', 'latin_capital_letter_i', 'digit_eight', 'left_parenthesis']},
		{'f': '4', '': ['latin_small_letter_o', 'latin_capital_letter_o', 'digit_nine', 'right_parenthesis']},
		{'f': 'R4', '': ['latin_small_letter_p', 'latin_capital_letter_p', 'digit_zero', 'vertical_line']},
	],
	[
		{'f': 'L', '': 'a'},
		's', 'd', 'f', 'g', 'h', 'j',
		{'f': '4', '': ['latin_small_letter_k', 'latin_capital_letter_k', ['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': '4', '': ['latin_small_letter_l', 'latin_capital_letter_l', 'commercial_at', 'grave_accent']},
		{'f': 'R4', '': ['semicolon', 'plus_sign', 'colon', 'asterisk']},
	],
	[
		{'f': 'L', '': 'z'},
		'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'R4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		{'f': 'fksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		{'f': 'fkp', '': ['symbol']},
		{'f': 'p', '': ['space']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['right', 'right_arrow']]},
		{'f': 'fkrp', '': [['backspace', 'delete']]},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
],

'416': [
	[
		{'w': '3.13%p', 'f': 'S'},
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
		{'w': '15.63%p', 'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfkp', '': ['symbol']},
		'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'i', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'w': '12.50%p', 'f': 'Rfp', '': ['space']},
		{'h': '48%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'w': '9.38%p', 'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'i', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'w': '3.13%p', 'f': 'SL'},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
	],
	[
		{'w': '12.50%p', 'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]},
	],
],

'415': [
	[
		{'w': '3.33%p', 'f': 'S'},
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
		{'w': '10.00%p', 'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfkp', '': ['symbol']},
		'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'i', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'w': '13.33%p', 'f': 'Rfp', '': ['space']},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'i', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]},
	],
],

'414': [
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
		{'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfkp', '': ['symbol']},
		'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'i', '': [['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': 'Rfp', '': ['space']},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'i', '': [['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		'z', 'x', 'c', 'v', 'b', 'n', 'm',
		{'f': 'i', '': [['comma', ['ideographic_comma']], 'less_than_sign']},
		{'f': 'i', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign']},
		{'f': 'i', '': [['solidus', ['katakana_middle_dot']], 'question_mark']},
		{'f': 'i', '': ['reverse_solidus', 'low_line']},
#		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
#		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]},
	],
],

'413': [
	[
		{'w': '3.85%p', 'f': 'S'},
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
		{'w': '11.54%p', 'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfkp', '': ['symbol']},
		'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
		{'f': 'i', '': ['commercial_at', 'grave_accent']},
		{'f': 'Rfp', '': ['space']},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		'z', 'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': '4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
#		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
#		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]},
	],
],

'314': [
	[
		{'f': 'Lfkp', '': ['symbol']},
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
		{'f': 'fp', '': ['space']},
		{'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
		{'f': 'i', '': ['semicolon', 'plus_sign']},
		{'f': 'i', '': ['colon', 'asterisk']},
		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
		{'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		'z', 'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': '4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]},
	],
],

'313': [
	[
		{'f': 'Lfkp', '': ['symbol']},
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
		{'f': 'fp', '': ['space']},
		{'f': 'Rfkrp', '': [['backspace', 'delete']]},
	],
	[
		{'f': 'Lfksm', '': [[['capslock', 'shift_off']], [['capslock', 'shift_on']], [['capslock', 'caps_on']]]},
		'a', 's', 'd', 'f', 'g', 'h', 'j',
		{'f': '4', '': ['latin_small_letter_k', 'latin_capital_letter_k', ['hyphen_minus', ['prolonged_sound_mark']], 'equals_sign']},
		{'f': '4', '': ['latin_small_letter_l', 'latin_capital_letter_l', 'commercial_at', 'grave_accent']},
		{'f': '4', '': ['semicolon', 'plus_sign', 'colon', 'asterisk']},
		{'w': '15.38%p', 'f': 'Rfrp', '': [['linefeed', 'enter']]},
	],
	[
		{'f': ['Lfkp', 'Lfkp', 'Ltfkp'], '': [[['chartype_to_abc', 'chartype_to_kana', 'chartype_to_123'], ['kana', 'alphabet'], ['alphabet', 'kana', 'number'], 'menu_dialog']]},
		'z', 'x', 'c', 'v', 'b', 'n',
		{'f': '4', '': ['latin_small_letter_m', 'latin_capital_letter_m', 'circumflex_accent', 'tilde']},
		{'f': '4', '': [['comma', ['ideographic_comma']], 'less_than_sign', ['left_square_bracket', ['left_corner_bracket']], 'left_curly_bracket']},
		{'f': '4', '': [['full_stop', ['ideographic_full_stop']], 'greater_than_sign', ['right_square_bracket', ['right_corner_bracket']], 'right_curly_bracket']},
		{'f': '4', '': [['solidus', ['katakana_middle_dot']], 'question_mark', ['reverse_solidus', ['yen_sign']], 'low_line']},
		{'f': 'tfkrp', '': [['left', 'left_arrow']]},
#		{'f': 'tfkrp', '': [['up', 'up_arrow']]},
#		{'f': 'tfkrp', '': [['down', 'down_arrow']]},
		{'f': 'Rtfkrp', '': [['right', 'right_arrow']]},
	],
],

}

for row, col in ((5, 14), (5, 13), (5, 12), (5, 11), (5, 10), (4, 11), (4, 10), (4, 16), (4, 15), (4, 14), (4, 13), (3, 14), (3, 13)):
	h = '%.2f%%p' % (96.0 / row)
	w = '%.2f%%p' % (100.0 / col)
	for mode, name in enumerate(('kbd_qwerty%d%d_kana.xml' % (row, col), 'kbd_qwerty%d%d_abc.xml' % (row, col), 'kbd_12keys_qwerty%d%d_abc.xml' % (row, col))):
		keyall = keydata['%d%d' % (row, col)]
		sourceId = 1
		xmlall = ''
		for keyrow in keyall:
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
				if 'm' not in f: k = [k, k[1:2] + k[0:1] + k[2:]] if 'f' not in f and len(k) >= 2 else [k]
				for index, keystate in enumerate(k):
					xmlstate = ''
					for index2, ids in enumerate(keystate):
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
						c_prefix = 'key_' if 'k' in f else 'uchar_'
						i_prefix1 = 'twelvekeys__' if 't' in f else 'qwerty__'
						i_prefix2 = '' if 'm' in f else 'function__' if 'f' in f or 'b' in f else 'keyicon__'
						i_suffix = '' if index2 else '__icon5' if '4' in f and ('L' in f or 'R' in f) else '__icon4' if '4' in f else '__icon2' if '2' in f else '__icon' if 'i' in f or 'p' in f else ''
						p_prefix1 = 'twelvekeys__' if 't' in f else 'qwerty__'
						p_prefix2 = 'function__' if 'f' in f else 'keyicon__'
						p_suffix = '__popup' if 'p' in f else '' if index2 else '__icon5' if '4' in f and ('L' in f or 'R' in f) else '__icon4' if '4' in f else '__icon2' if '2' in f else '__icon' if 'i' in f else ''
						xml = '' if 'm' in f else tag('', 'PopUp', ' mozc:popUpIcon="@raw/%s"' % (p_prefix1 + p_prefix2 + popup[mode] + p_suffix), '            ')
						xml = tag(xml, 'KeyEntity', ''' mozc:sourceId="%%d"%(high)s%(long)s
                     mozc:keyCode="@integer/%(code)s"
                     mozc:keyIcon="@raw/%(icon)s"''' % {
							'high': ' mozc:flickHighlight="true"' if 'f' not in f else '',
							'long': '''
                     mozc:longPressKeyCode="@integer/%s"''' % (c_prefix + long[mode]) if long[mode] else '',
							'code': c_prefix + code[mode],
							'icon': i_prefix1 + i_prefix2 + icon[mode] + i_suffix
						}, '          ')
						xmlstate += tag(xml % sourceId, 'Flick', '' if 'f' in f or not index2 else ' mozc:direction="%s"' % ('left' if index2 == 2 else 'right' if index2 == 3 else 'down' if index else 'up'), '        ')
						sourceId += 1
						if 'f' not in f and (('L' in f and index2 == 2) or ('R' in f and index2 == 3)):
							xmlstate += tag(xml % sourceId, 'Flick', ' mozc:direction="%s"' % ('up' if index else 'down'), '        ')
							sourceId += 1
					xmlkey += tag(xmlstate, 'KeyState', [
						[
							'',
							' mozc:metaState="shift|capsLock"',
						],
						[
							' mozc:nextMetaState="shift"',
							' mozc:metaState="shift" mozc:nextMetaState="capsLock"',
							' mozc:metaState="capsLock" mozc:nextMetaState="unmodified"',
						],
					][1 if 'm' in f else 0][index], '      ')
				xmlrow += tag(xmlkey, 'Key',
				 ((' mozc:keyBackground="qwertyFunction"\n        ') if 'f' in f or 'b' in f else '')
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
    mozc:keyBackground="qwertyRegular"
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
