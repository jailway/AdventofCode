def load_data() -> [(str, str)]:
    """
    Loads instruction set from input file sorted by second step

    :return: instruction set as a list of tuples
    """
    instructions = list()
    with open('07_input.txt', 'r') as f:
        for l in f.readlines():
            instructions.append((l[5], l[36]))

    def oposite_order(e: (str, str)) -> (str, str):
        return e[1], e[0]

    instructions.sort(key=oposite_order)
    return instructions


def get_all_steps(instructions: [(str, str)]) -> [str]:
    """
    Gets a list of unique steps
    :param instructions: instructions list
    :return: sorted list of instructions
    """
    steps = set()
    steps.update([i[0] for i in instructions])
    steps.update([i[1] for i in instructions])
    return sorted(list(steps))


def requires(succedent: str, antecedent: str, instructions: [(str, str)]) -> bool:
    """
    Check is a preceding step is required, recursively

    :param succedent: second step
    :param antecedent: first step
    :param instructions: instruction set
    :return: True if the step is required
    """
    for i in instructions:
        if i[1] == succedent:
            if i[0] == antecedent:
                return True
            elif requires(i[0], antecedent, instructions):
                return True
    return False


def sort_steps(steps: [str], instructions: [(str, str)]) -> [str]:
    """
    Sorts step by order of execution, based on requirements and alphabet
    :param steps: steps to be sorted as a list
    :param instructions: set of instructions
    :return: sorted list of steps
    """
    s = steps

    for i in reversed(range(0, len(s))):
        for j in reversed(range(0, i)):
            if requires(s[j], s[i], instructions) or (s[i] < s[j] and not requires(s[i], s[j], instructions)):
                s[j], s[i] = s[i], s[j]
    return s


def work_parallel(steps: [str], instructions: [(str, str)], num_workers: int) -> int:
    """
    Calculates processing time with parallel workers

    :param steps: steps in order of execution
    :param instructions: instruction limits set
    :param num_workers: parallelization degree, number of workers
    :return: time in seconds
    """

    def duration(step: str) -> int:
        return ord(step) - 4

    time = 0
    workers = dict()
    for i in range(0, num_workers):
        workers[i] = (None, 0)
    done = set()

    while len(done) != len(steps):
        for w in range(0, num_workers):
            if workers[w][0] is not None and time >= workers[w][1] + duration(workers[w][0]):
                done.add(workers[w][0])
                workers[w] = (None, 0)
            if workers[w][0] is None:
                for i in range(0, len(steps)):
                    if (steps[i] not in [wk[0] for wk in workers.values()]) and (steps[i] not in done):
                        step_available = True
                        for j in range(0, i):
                            if steps[j] not in done and requires(steps[i], steps[j], instructions):
                                step_available = False
                                break
                        if step_available:
                            workers[w] = (steps[i], time)
                            break

                # w[1] = time
        time += 1
    return time - 1


if __name__ == "__main__":
    instr = load_data()
    steps = get_all_steps(instr)
    steps = sort_steps(steps, instr)
    print('Answer to star 1 is: ', ''.join(steps))
    print('Answer to star 2 is: ', work_parallel(steps, instr, 5))
