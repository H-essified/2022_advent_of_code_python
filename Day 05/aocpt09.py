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
	# Create list of crates
	stacks = {}
	split_row = data.index("") - 1
	for row in data[:split_row]:
		columns = row.replace("    ", " ").replace("[", "").replace("]", "").split(" ")
		for i, column in enumerate(columns):
			if column == "": continue
			stacks[i] = column if i not in stacks.keys() else stacks[i] + column

	# Follow instructions
	for i, row in enumerate(data[split_row + 2:]):
		row_moves = row.split(" ")
		move_tuple = [int(row_moves[i]) for i in [1, 3, 5]]
		move_pieces = stacks[move_tuple[1] - 1][:move_tuple[0]]
		stacks[move_tuple[2] - 1] = move_pieces[::-1] + stacks[move_tuple[2] - 1]
		stacks[move_tuple[1] - 1] = stacks[move_tuple[1] - 1][move_tuple[0]:]
	return "".join(stack[0] for i, stack in sorted(stacks.items()))

if __name__ == "__main__":
	day = "05"
	solver = Solver(day, "CMZ")
	solver.run_solution(solve_puzzle)