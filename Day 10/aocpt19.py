import time

class Solver:
	def __init__(self, day, validation_answer):
		self.data = [line.replace("\n", "") for line in open(f"Day {day}/input{day}.txt", "r").readlines()]
		self.test_data = [line.replace("\n", "") for line in open(f"Day {day}/test_input{day}.txt", "r").readlines()]
		self.validation_answer = validation_answer

	def run_solution(self, solver):
		assert(solver(self.test_data) == self.validation_answer)
		start = time.time()
		solution = solver(self.data)
		end = time.time()
		elapsed_time = round(end * 1000 - start * 1000, 4)
		print(f"Solution: {solution}")
		print(f"Elapsed time: {elapsed_time} milliseconds")


def solve_puzzle(data):
	x = 1
	i = 1
	score = 0
	data.extend(["noop", "noop"])
	for command in data:
		if command.split(" ")[0] == "addx":
			for j in range(2):
				if (i - 20) % 40 == 0:
					score += x * i
				i += 1
			x += int(command.split(" ")[1])
		if command.split(" ")[0] == "noop":
			if (i - 20) % 40 == 0:
				score += x * i
			i += 1
	return score

if __name__ == "__main__":
	day = "10"
	solver = Solver(day, 13140)
	solver.run_solution(solve_puzzle)