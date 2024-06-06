import os

def generate_files():
    for i in range(1,26):
        if i in [1, 2]:
            continue
        i = f"0{i}" if i < 10 else i
        if not os.path.exists(f"{os.getcwd()}/Day {i}"):
            os.makedirs(f"{os.getcwd()}/Day {i}")
        f = open(f"{os.getcwd()}/Day {i}/input{i}.txt", "w")
        f.close()
        f = open(f"{os.getcwd()}/Day {i}/test_input{i}.txt", "w")
        f.close()
        part1 = f"0{int(i) * 2 - 1}" if (int(i) * 2 - 1) < 10 else str(int(i) * 2 - 1)
        part2 = f"0{int(i) * 2}" if (int(i) * 2 - 1) < 10 else str(int(i) * 2)
        f = open(f"{os.getcwd()}/Day {i}/aocpt{part1}.py", "w")
        write_base_code(f, day=i)
        f.close()
        f = open(f"{os.getcwd()}/Day {i}/aocpt{part2}.py", "w")
        write_base_code(f, day=i)
        f.close()

def write_base_code(f, day):
    f.write('''import time

class Solver:
\tdef __init__(self, day, validation_answer):
\t\tself.data = [line.replace("\\n", "") for line in open(f"Day {day}/input{day}.txt", "r").readlines()]
\t\tself.test_data = [line.replace("\\n", "") for line in open(f"Day {day}/test_input{day}.txt", "r").readlines()]
\t\tself.validation_answer = validation_answer

\tdef run_solution(self, solver):
\t\tassert(solver(self.test_data) == self.validation_answer)
\t\tstart = time.time()
\t\tsolution = solver(self.data)
\t\tend = time.time()
\t\telapsed_time = round(end * 1000 - start * 1000, 4)
\t\tprint(f"Solution: {solution}")
\t\tprint(f"Elapsed time: {elapsed_time} milliseconds")


def solve_puzzle(data):
\tprint(data)
\treturn

if __name__ == "__main__":\r''')
    f.write(f"\tday = \"{day}\"\r")
    f.write('''\tsolver = Solver(day, 0)
\tsolver.run_solution(solve_puzzle)''')

    return

generate_files()

