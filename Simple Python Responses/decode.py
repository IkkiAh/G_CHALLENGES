input = "\u0050 \u0075 \u007a \u007a \u006c \u0065 \u0073 \u0020  \u0061 \u0072 \u0065 \u0020 \u0066 \u0075 \u006e \u002e  \u0020 \u0053 \u0065 \u0061 \u0072 \u0063 \u0068 \u0020 \u006f \u006e \u002e"
list = input.split(' ',0)

for x in list:
	decoded = x.decode('unicode-escape')
	set =  decoded.replace("  ", '*DOUBLESPACE*')
	set2 = set.replace(' ','')
	revert = set2.replace('*DOUBLESPACE*', ' ')
	print revert
