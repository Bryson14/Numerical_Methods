import time


def dynamic_fib(n):
	f = [0]*(n+1)
	f[0] = 0
	f[1] = 1

	for i in range(2, n+1):
		f[i] = f[i-1] + f[i-2]

	return f[n]


def recur_fib(n):
	if n <= 1:
		return n
	return recur_fib(n-1) + recur_fib(n-2)


start = time.time()
print(recur_fib(30))
print("time for recursive function: ", time.time() - start)
mid = time.time()
ans = dynamic_fib(10000)
print(len(str(ans)))
print(ans)
print("time for dynamic function: ",time.time() - mid)