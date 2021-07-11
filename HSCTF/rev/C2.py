import sys

class Fibonacci:
	def getAt(self, index):
		# 0 1 2 3 5 8 13
		F = [0,1]
		total = 0

		for i in range(int(index)):
			nth = F[0] + F[1]
			F[0] = F[1]
			F[1] = nth
			total += nth
			print(total)

		print("Result:", total)

if __name__ == "__main__":
	a = Fibonacci()
	a.getAt(sys.argv[1])