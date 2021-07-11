import socket
import sys

class attempt:
	def decode(self, sample):
		splitSample = []

		# split at a or m

		index = 0
		runningNumber = ""
		while index < len(sample):
			if sample[index] == 'a' or sample[index] == 'm':
				splitSample.append(runningNumber)
				splitSample.append(sample[index])
				runningNumber = ""
			else:
				runningNumber += sample[index]

			index += 1
		splitSample.append(runningNumber)

		print("Split List:", splitSample)

		sample = splitSample

		# addition
		sampleWithNoAdds = []

		index = 0
		while index < len(sample):
			if sample[index] == 'm':
				sampleWithNoAdds.append(sample[index])
			elif sample[index] == 'a':
				sampleWithNoAdds.append(int(sample[index+1]) + int(sampleWithNoAdds[-1]))
				sampleWithNoAdds.pop(-2)
				index += 1
			else:
				sampleWithNoAdds.append(int(sample[index]))

			index += 1

		print("No adds:", sampleWithNoAdds)

		sample = sampleWithNoAdds

		# remove m

		sampleWithNoMults = []

		for i in sample:
			if i != 'm':
				sampleWithNoMults.append(i)


		print("No Mults:", sampleWithNoMults)

		# calc score

		result = 1
		for i in sampleWithNoMults:
			result *= i

		print("Result:", result)

		if result > 4294967296-1:
			print("Use:", result % 4294967295)

		return result

if __name__ == "__main__":
	a = attempt()
	a.decode(sys.argv[1])
