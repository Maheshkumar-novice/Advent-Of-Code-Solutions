import re


class ThreeBitComputer:  # noqa: D101
    def __init__(self, a: int, b: int, c: int) -> None:  # noqa: D107
        self.A = a
        self.B = b
        self.C = c
        self.instruction_pointer = 0
        self.output_register = []
        self.opcode_operations = {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv,
        }

    def run(self, program: list[int]) -> None:  # noqa: D102
        while self.instruction_pointer < len(program) - 1:
            opcode = program[self.instruction_pointer]
            operand = program[self.instruction_pointer + 1]
            operation = self.opcode_operations[opcode]
            operation(operand)

    def _adv(self, input_: int) -> None:
        operand = self._get_operand(input_, type_="combo")
        self.A = int(self.A / (2**operand))
        self.instruction_pointer += 2

    def _bxl(self, input_: int) -> None:
        operand = self._get_operand(input_, type_="literal")
        self.B = self.B ^ operand
        self.instruction_pointer += 2

    def _bst(self, input_: int) -> None:
        operand = self._get_operand(input_, type_="combo")
        self.B = operand % 8
        self.instruction_pointer += 2

    def _jnz(self, input_: int) -> None:
        operand = self._get_operand(input_, type_="literal")
        if self.A == 0:
            self.instruction_pointer += 2
            return
        self.instruction_pointer = operand

    def _bxc(self, input_: int) -> None:  # noqa: ARG002
        self.B = self.B ^ self.C
        self.instruction_pointer += 2

    def _out(self, input_: int) -> None:
        operand = self._get_operand(input_, type_="combo")
        self.output_register.append(operand % 8)
        self.instruction_pointer += 2

    def _bdv(self, input_: int) -> None:
        operand = self._get_operand(input_, type_="combo")
        self.B = int(self.A / (2**operand))
        self.instruction_pointer += 2

    def _cdv(self, input_: int) -> None:
        operand = self._get_operand(input_, type_="combo")
        self.C = int(self.A / (2**operand))
        self.instruction_pointer += 2

    def _get_operand(self, input_: int, type_: str) -> int:
        if type_ == "literal":
            return input_

        if 0 <= input_ <= 3:
            return input_

        if input_ == 4:
            return self.A

        if input_ == 5:
            return self.B

        if input_ == 6:
            return self.C
        return None


with open("input.txt") as f:
    A, B, C, program = re.findall(r": (\d+(?:,\d+)*)\b", f.read())
A, B, C = int(A), int(B), int(C)
program = list(map(int, program.split(",")))
computer = ThreeBitComputer(A, B, C)
computer.run(program)
print(",".join(map(str, computer.output_register)))
