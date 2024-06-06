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
	directories = {"/": [0, set()]}
	current_dir_path = "/"
	for row in data:
		row_parts = row.split(" ")
		if row_parts[0] == "$":
			if row_parts[1] == "cd":
				if row_parts[2] == "/":
					current_dir_path = "/"
				elif row_parts[2] == "..":
					current_dir_path = "/".join(current_dir_path.split("/")[:-2]) + "/"
				else:
					current_dir_path += row_parts[2] + "/"
					if current_dir_path not in directories:
						directories[current_dir_path] = [0, set()]
		elif row_parts[0] == "dir":
			if current_dir_path + row_parts[1] + "/" not in directories:
				directories[current_dir_path + row_parts[1] + "/"] = [0, set()]
		else:
			size = int(row_parts[0])
			file_name = row_parts[1]
			if file_name not in directories[current_dir_path][1]:
				directories[current_dir_path][1].add(file_name)
				directories[current_dir_path][0] += size
				for i in range(2, len(current_dir_path.split("/"))):
					directories["/".join(current_dir_path.split("/")[:-i]) + "/"][0] += size
	target_value = 30000000 - (70000000 - directories["/"][0])
	return min(value[0] for value in directories.values() if value[0] > target_value) 
	

if __name__ == "__main__":
	day = "07"
	solver = Solver(day, 24933642)
	solver.run_solution(solve_puzzle)