import time

class Solver:
	def __init__(self, day, validation_answer):
		self.data = [line.replace("\n", "") for line in open(f"Day {day}/input{day}.txt", "r").readlines()]
		self.test_data = [line.replace("\n", "") for line in open(f"Day {day}/test_input{day}.txt", "r").readlines()]
		self.validation_answer = validation_answer

	def run_solution(self, solver):
		# assert(solver(self.test_data) == self.validation_answer)
		start = time.time()
		solution = solver(self.data)
		end = time.time()
		elapsed_time = round(end * 1000 - start * 1000, 4)
		print(f"Solution: {solution}")
		print(f"Elapsed time: {elapsed_time} milliseconds")


def draw_dot(i, x, rows):
	if i // 40 not in rows.keys():
		rows[i // 40] = []
	if i - (40 * (i // 40)) in [x - 1, x, x + 1]:
		rows[i // 40].append("#")
	else:
		rows[i // 40].append(".")
	return rows


def solve_puzzle(data):
	x = 1
	i = -1
	rows = {}
	data.extend(["noop", "noop"])
	for command in data:
		if command.split(" ")[0] == "addx":
			for j in range(2):
				i += 1
				rows = draw_dot(i , x, rows)
			x += int(command.split(" ")[1])
		if command.split(" ")[0] == "noop":
			i += 1
			rows = draw_dot(i, x, rows)

	for row in rows.values():
		print("".join(item for item in row))
	return 

if __name__ == "__main__":
	day = "10"
	solver = Solver(day, 0)
	solver.run_solution(solve_puzzle)