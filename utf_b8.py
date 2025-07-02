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
