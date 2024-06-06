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
	score = 0
	for rucksack in data:
		compartment1 = rucksack[:len(rucksack) // 2]
		compartment2 = rucksack[len(rucksack) // 2:]
		common_letter = [letter for letter in compartment1 if letter in compartment2][0]
		score += ord(common_letter.lower()) - 96 if common_letter == common_letter.lower() else ord(common_letter.lower()) - 70
	return score

if __name__ == "__main__":
	day = "03"
	solver = Solver(day, 157)
	solver.run_solution(solve_puzzle)