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
	visited_locations = set([(0, 0)])
	pos = {}
	for i in range(2):
		pos[i] = (0, 0)
	for row in data:
		direction = row.split(" ")[0]
		distance = int(row.split(" ")[1]) * -1 if direction in ["L", "D"] else int(row.split(" ")[1])
		j = 0 if direction in ["R", "L"] else 1
		for move_num in range(0, abs(distance)):
			for i in pos.keys():
				if i == 0:
					multiplier = -1 if distance < 0 else 1
					pos[i] = (pos[i][0] + multiplier, pos[i][1]) if j == 0 else (pos[i][0], pos[i][1] + multiplier)
					continue
				moving = True
				while moving:
					moving = False
					if abs(pos[i - 1][0] - pos[i][0]) > 1:
						if pos[i][1] != pos[i - 1][1]:
							diagonal = 1 if pos[i][1] < pos[i - 1][1] else -1
							pos[i] = (pos[i][0], pos[i][1] + diagonal)
						multiplier = -1 if pos[i - 1][0] < pos[i][0] else 1
						pos[i] = (pos[i][0] + multiplier, pos[i][1]) 
						moving = True
					elif abs(pos[i - 1][1] - pos[i][1]) > 1:
						if pos[i][0] != pos[i - 1][0]:
							diagonal = 1 if pos[i][0] < pos[i - 1][0] else -1
							pos[i] = (pos[i][0] + diagonal, pos[i][1])
						multiplier = -1 if pos[i - 1][1] < pos[i][1] else 1
						pos[i] = (pos[i][0], pos[i][1] + multiplier)
						moving = True
				if i == max(pos.keys()):
					visited_locations.add((pos[i][0], pos[i][1]))
	return len(visited_locations)

if __name__ == "__main__":
	day = "09"
	solver = Solver(day, 13)
	solver.run_solution(solve_puzzle)