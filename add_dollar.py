import re

address = "adress.txt"

def register_transformer( matchObject):
	if matchObject.group()[0] != '$':
		return '$' + matchObject.group()
	else:
		return matchObject.group()


def text_transformer( matchObject):
	return matchObject.group(1) + ':' + matchObject.group(2) +'\t'


def quote_transformer(matchObject):
	return matchObject[1] + '\\n' + matchObject[2].lstrip() + '\\n' + matchObject[3] 

def dot_transformer(matchObject):
	return '.' + matchObject[1] + '\n'



with open( address, "w") as f:
	tab_level = 
	for i in open("mips1.asm", "r"):
		s = i

		s = re.sub( r' (global|glob|glo){1}[\t\n ]+', r'globl\n', s)
		s = re.sub( r'(data|text|globl){1}[\t\n ]+', dot_transformer, s)				#.data
		s = re.sub( r'([\'\"])([a-zA-Z0-9\s]+)([\'\"])', quote_transformer, s)		# "Hello"
		s = re.sub( r'(\$?)[avts][0-9]', register_transformer, s)					# $t1

		s = re.sub( r'(\.?)(sp|space)[\t ]+', r'.space\t', s)							# .space
		s = re.sub( r'(\.?)(str|asciiz|asc)[\t ]+', r'.asciiz\t', s)						# .asciiz
		s = re.sub( r'(\.?)(num|word)[\t ]+', r'.word\t', s)							# .word

		s = re.sub( r'sys((call)|(cal)|(ca)|(c))', r'syscall', s)  					#sys
		s = re.sub( r'([a-zA-Z0-9_]{1,})([\t ]+\.(asciiz|word|space))', text_transformer, s)		#msg

		s = s.lstrip()
		
		if (re.search( r'(data|text|globl){1,}:', s) != None):
			f.write(s)
			global tab_level
			tab_level = 1

		else:
			f.write( tab_level*"\t" + s)
		print(tab_level, end ='')

	