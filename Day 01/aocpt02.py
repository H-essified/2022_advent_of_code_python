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
	carriers = []
	current = 0
	for line in data:
		if len(line) == 0:
			carriers.append(current)
			current = 0
			continue
		current += int(line)
	carriers.append(current)
	carriers = sorted(carriers)
	return sum(carriers[-3:])

def single_line_solution(data):
	if data == [line.replace("\n", "") for line in open(f"Day {day}/input{day}.txt", "r").readlines()]:
		return sum(sorted([sum(list) for list in [[int(calories) for calories in elf.split("\n")] for elf in open("Day 01/input01.txt", "r").read().split("\n\n")]])[-3:])
	elif data == [line.replace("\n", "") for line in open(f"Day {day}/test_input{day}.txt", "r").readlines()]:
		return sum(sorted([sum(list) for list in [[int(calories) for calories in elf.split("\n")] for elf in open("Day 01/test_input01.txt", "r").read().split("\n\n")]])[-3:])

if __name__ == "__main__":
	day = "01"
	solver = Solver(day, 45000)
	solver.run_solution(solve_puzzle)
	solver.run_solution(single_line_solution)
