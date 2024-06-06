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


def solve_puzzle(rows):
	return (len(rows) * 2) + (len(rows[0]) * 2) - 4 + sum(int(rows[y][x]) > min([max(int(height) for height in rows[y][:x]), max(int(height) for height in rows[y][x + 1:]), max(int(rows[j][x]) for j in range(y)), max(int(rows[j][x]) for j in range(y + 1, len(rows)))]) for (x, y) in [(x, y) for x in range(1, len(rows[0]) - 1) for y in range(1, len(rows) - 1)])

if __name__ == "__main__":
	day = "08"
	solver = Solver(day, 21)
	solver.run_solution(solve_puzzle)

# print((len([line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()]) * 2) + (len([line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()][0]) * 2) - 4 + sum(int([line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()][y][x]) > min([max(int(height) for height in [line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()][y][:x]), max(int(height) for height in [line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()][y][x + 1:]), max(int([line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()][j][x]) for j in range(y)), max(int([line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()][j][x]) for j in range(y + 1, len([line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()])))]) for (x, y) in [(x, y) for x in range(1, len([line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()][0]) - 1) for y in range(1, len([line.replace("\n", "") for line in open("Day 08/input08.txt", "r").readlines()]) - 1)]))