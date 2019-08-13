y_n = [[0],[0],[0],[0]]

x2 = [[1,0,1,1],[1,1,0,1],[1,1,1,0],[0,1,1,1]]

x1 = [[1],[2],[3],[4]]







for i in range(4):

	for j in range(1):

		for k in range(4):

			y_n[i][j] += x2[i][k] * x1[k][j]



print(y_n)


