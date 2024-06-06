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
	# Loss = 0, Draw = 3, Win = 6
	# X = Rock, Y = Paper, Z = Scissors
	# A = Rock, B = Paper, C = Scissors
	scores = {"B X": 1, "C Y": 2, "A Z": 3, "A X": 4, "B Y": 5, "C Z": 6, "C X": 7, "A Y": 8, "B Z": 9}
	score = sum(scores[row.upper()] for row in data)
	return score

def single_line_solution(data):
	if data == [line.replace("\n", "") for line in open(f"Day {day}/input{day}.txt", "r").readlines()]:
		return sum({"B X": 1, "C Y": 2, "A Z": 3, "A X": 4, "B Y": 5, "C Z": 6, "C X": 7, "A Y": 8, "B Z": 9}[row.upper()] for row in [line.replace("\n", "") for line in open(f"Day 02/input02.txt", "r").readlines()])
	elif data == [line.replace("\n", "") for line in open(f"Day {day}/test_input{day}.txt", "r").readlines()]:
		return sum({"B X": 1, "C Y": 2, "A Z": 3, "A X": 4, "B Y": 5, "C Z": 6, "C X": 7, "A Y": 8, "B Z": 9}[row.upper()] for row in [line.replace("\n", "") for line in open(f"Day 02/test_input02.txt", "r").readlines()])

if __name__ == "__main__":
	day = "02"
	solver = Solver(day, 15)
	solver.run_solution(solve_puzzle)
	solver.run_solution(single_line_solution)
