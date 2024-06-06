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


def check_direction(view, tree):
	count = 0
	for height in view:
		count += 1
		if tree <= height:
			return count
	return count

def solve_puzzle(rows):
	scores = set()
	for (x, y) in [(x, y) for x in range(0, len(rows[0]) - 1) for y in range(0, len(rows) - 1)]:
		tree = int(rows[y][x])
		left = [int(height) for height in rows[y][:x]][::-1]
		right = [int(height) for height in rows[y][x + 1:]]
		up = [int(rows[j][x]) for j in range(y)][::-1]
		down = [int(rows[j][x]) for j in range(y + 1, len(rows))]
		scores.add(check_direction(left, tree) * check_direction(right, tree) * check_direction(up, tree) * check_direction(down, tree))
	return max(scores)


if __name__ == "__main__":
	day = "08"
	solver = Solver(day, 8)
	solver.run_solution(solve_puzzle)