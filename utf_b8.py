def valid_utf_b8(bytes):
	try:
		text=bytes.decode('utf-8',errors='surrogatepass')
	except UnicodeDecodeError:
		print('invalid utf-8')
		return False
	for char in text:
		if 0x10000 <= ord(char) <= 0x10FFFF:
			print('codepoint decodes to utf-32. too valid')
			return False
		else:
			return True
def encode_utf_b8(codepoint: int) -> bytes:
	if codepoint <= 0xFFFF:
		return chr(codepoint).encode('utf-8')
	else:
		codepoint -= 0x10000
		high=0xD800+(codepoint >> 10)
		low=0xDC00+(codepoint & 0x3FF)
		return chr(high).encode('utf-8','surrogatepass')+chr(low).encode('utf-8','surrogatepass')
