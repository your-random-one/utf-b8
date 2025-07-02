def is_high(codepoint):
	return 0xD800<=codepoint<=0xDBFF
def is_low(codepoint):
	return 0xDC00<=codepoint<=0xDFFF
def validate(bytes):
	try:
		text=bytes.decode('utf-8',errors='surrogatepass')
	except UnicodeDecodeError:
		print('invalid utf-8')
		return False
	surflag=False
	for char in text:
		if 0x10000 <= ord(char) <= 0x10FFFF:
			print('codepoint decodes to utf-32. too valid')
			return False
		elif is_high(ord(char)) and not surflag:
			surflag=True
		elif is_high(ord(char)) and surflag:
			print('invalid utf-16 surrogate pairing')
			return False
		elif not 0xD800<=ord(char)<=0xDFFF and surflag:
			print('invalid utf-16 surrogate pairing')
			return False
		elif is_low(ord(char)) and surflag:
			surflag=False
		elif is_low(ord(char)) and not surflag:
			print('invalid utf-16 surrogate pairing')
			return False
	return True
def encode(string):
	encoded=b''
	for c in string:
		codepoint=ord(c)
		if codepoint <= 0xFFFF:
			encoded+=chr(codepoint).encode('utf-8')
		else:
			codepoint -= 0x10000
			high=0xD800+(codepoint>>10)
			low=0xDC00+(codepoint&0x3FF)
			encoded+=chr(high).encode('utf-8','surrogatepass')+chr(low).encode('utf-8','surrogatepass')
	return encoded
def decode(bytes):
	if not validate(bytes):
		return 'Error'
	text=bytes.decode('utf-8','surrogatepass')
	decoded=''
	surbuf=0
	surflag=False
	for char in text:
		if is_high(ord(char)):
			surbuf=(ord(char)-0xD800)<<10
			surflag=True
		elif surflag:
			decoded+=chr(0x10000+surbuf+(ord(char)-0xDC00))
			surflag=False
		else:
			decoded+=char
	return decoded
