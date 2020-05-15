from sys import stdin

'took the whole program from your video'
'also forgot how to do python comments so useless strings will suffice'
def decode(binary, n):
	text = ""
	i = 0
	while (i < len(binary)):
		byte = binary[i:i+n]
		byte = int(byte,2)
		'it was 8 not 9  :)'
		if (byte == 8):
			'If backspace remove the last character'
			text = text.rstrip(text[len(text)-1])
		else:
			text += chr(byte)
		i += n
	return text

binary = stdin.read().rstrip("\n")

if(len(binary) % 7 == 0):
	text = decode(binary, 7)
	print text
if(len(binary) % 8 == 0):
	text = decode(binary, 8)
	print text