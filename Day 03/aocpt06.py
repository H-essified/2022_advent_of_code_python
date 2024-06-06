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
	for i in range(len(data) // 3):
		common_letter = [item for item in data[i * 3] if item in data[i * 3 + 1] and item in data[i * 3 + 2]][0]
		score += ord(common_letter.lower()) - 96 if common_letter == common_letter.lower() else ord(common_letter.lower()) - 70
	return score

if __name__ == "__main__":
	day = "03"
	solver = Solver(day, 70)
	solver.run_solution(solve_puzzle)