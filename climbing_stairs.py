n = 0
def climbing(n):
	if n == 0:
		return 0
	u_prev = 0
	u_curr = 1
	for i in range(n):
		temp = u_curr
		u_curr = u_curr + u_prev
		u_prev = temp
	return u_curr