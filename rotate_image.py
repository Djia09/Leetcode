matrix = [
  [1,2,3,4,21],
  [5,6,7,8,22],
  [9,10,11,12,23],
  [13,14,15,16,24],
  [17,18,19,20,25]
]
matrix = [
	[2,29,20,26,16,28],
	[12,27,9,25,13,21],
	[32,33,32,2,28,14],
	[13,14,32,27,22,26],
	[33,1,20,7,21,7],
	[4,24,1,6,32,34]
	]
n = 5
matrix = [list(range(i*n, (i+1)*n)) for i in range(n)]
def rotate(matrix):
	n = len(matrix)
	
	# # First method
	# matrix_save = []
	# for i in range(n):
	# 	row_save = []
	# 	for j in range(n):
	# 		row_save.append(matrix[i][j])
	# 	matrix_save.append(row_save)
	# matrix_save = matrix
	# for j in range(n):
	# 	for i in range(n):
	# 		print(j, i, n-1-i, matrix_save[i][j], matrix_save[n-1-i][j])
	# 		matrix[j][i] = matrix_save[n-1-i][j]
	# 	# 	row_90.append(matrix[i][j])
	# 	# 	matrix[i][j] = matrix_save
	# 	# matrix_90.append(row_90)
	# print(matrix_save)
	# print(matrix)

	# Second method
	for x in range(n):
		print(matrix[x])
	for k in range(n//2):
		for l in range(0, n-1-k*2):
			print("l: ", l)
			temp00 = matrix[k][k+l]
			matrix[k][k+l] = matrix[n-1-k-l][k]

			temp01 = matrix[k+l][n-1-k]
			matrix[k+l][n-1-k] = temp00

			temp00 = matrix[n-1-k][n-1-k-l]
			matrix[n-1-k][n-1-k-l] = temp01

			matrix[n-1-k-l][k] = temp00		
			
			print(matrix)