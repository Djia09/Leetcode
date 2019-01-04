s = "PAYPALISHIRING"
numRows = 4

# output = "PAHNAPLSIIGYIR"
output = "PINALSIGYAHRPI"

def zigag(s, numRows):
	print('Input: ', s)
	if numRows <= 1:
		return s
	t = ""
	for row in range(numRows):
		print("Row n°%d" % (row))
		for i in range(row,len(s),numRows+(numRows-2)):
			print(i, s[i])
			if row != 0 and row < numRows-1:
				try:
					t += s[i]+s[i+2*(numRows-row-1)]
				except IndexError:
					t += s[i]
			else:
				t += s[i]
	print('Real output: ', output)
	print('Obtained output: ', t)
	return t