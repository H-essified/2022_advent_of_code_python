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
	duplicate_elves = 0
	for pair in data:
		elf1 = range(int(pair.split(",")[0].split("-")[0]), int(pair.split(",")[0].split("-")[1]) + 1)
		elf2 = range(int(pair.split(",")[1].split("-")[0]), int(pair.split(",")[1].split("-")[1]) + 1)
		if all(i in elf2 for i in elf1) or all(i in elf1 for i in elf2):
			duplicate_elves += 1
	return duplicate_elves

if __name__ == "__main__":
	day = "04"
	solver = Solver(day, 2)
	solver.run_solution(solve_puzzle)