class SimpleCPU:
    def __init__(self, checkpoints: list[int]):
        self.cycle = 0
        self.register = 1
        self.operation = {}
        self.checkpoints = checkpoints
        self.signal_strength = 0

    def load_operation(self, instruction: str):
        try:
            self.operation["adjustment"] = int(instruction.split()[-1])
            self.operation["counter"] = 2
        except ValueError:
            self.operation["adjustment"] = 0
            self.operation["counter"] = 1

    def run_operation(self):
        while self.operation["counter"] > 0:
            if abs(self.cycle % 40 - self.register) <= 1:
                print("#", end="")
            else:
                print(" ", end="")
            self.cycle += 1
            if self.cycle % 40 == 0:
                print()
            if self.cycle in self.checkpoints:
                self.signal_strength += self.cycle * self.register
            if self.operation["counter"] == 1:
                self.register += self.operation["adjustment"]
            self.operation["counter"] += -1

    def process_instructions(self, instructions: list[str]):
        for instruction in instructions:
            self.load_operation(instruction)
            self.run_operation()


if __name__ == "__main__":
    import aoctty.utils.read_puzzle

    cpu = SimpleCPU(range(20, 221, 40))
    puzzle_input = aoctty.utils.read_puzzle.get_raw_puzzle("puzzle.txt")
    cpu.process_instructions(puzzle_input)
    print(cpu.signal_strength)
