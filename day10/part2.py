from math import inf

from common import input_machines

EPS = 1e-9


def simplex(
    constraints: list[list[float]], objective_coefficients: list[float]
) -> tuple[float, list[float] | None]:
    def pivot(pivot_row: int, pivot_col: int) -> None:
        pivot_inverse = 1 / tableau[pivot_row][pivot_col]
        for i in range(constraint_count + 2):
            if i == pivot_row:
                continue
            for j in range(variable_count + 2):
                if j != pivot_col:
                    tableau[i][j] -= (
                        tableau[pivot_row][j] * tableau[i][pivot_col] * pivot_inverse
                    )
        for i in range(variable_count + 2):
            tableau[pivot_row][i] *= pivot_inverse
        for i in range(constraint_count + 2):
            tableau[i][pivot_col] *= -pivot_inverse
        tableau[pivot_row][pivot_col] = pivot_inverse
        basic_variables[pivot_row], nonbasic_variables[pivot_col] = (
            nonbasic_variables[pivot_col],
            basic_variables[pivot_row],
        )

    def find(phase: int) -> int:
        while True:
            if (
                tableau[constraint_count + phase][
                    pivot_col := min(
                        (
                            i
                            for i in range(variable_count + 1)
                            if phase or nonbasic_variables[i] != -1
                        ),
                        key=lambda x: (
                            tableau[constraint_count + phase][x],
                            nonbasic_variables[x],
                        ),
                    )
                ]
                > -EPS
            ):
                return 1

            if (
                pivot_row := min(
                    (i for i in range(constraint_count) if tableau[i][pivot_col] > EPS),
                    key=lambda x: (
                        tableau[x][-1] / tableau[x][pivot_col],
                        basic_variables[x],
                    ),
                    default=-1,
                )
            ) == -1:
                return 0

            pivot(pivot_row, pivot_col)

    constraint_count = len(constraints)
    variable_count = len(constraints[0]) - 1
    nonbasic_variables = [*range(variable_count), -1]
    basic_variables = [*range(variable_count, variable_count + constraint_count)]
    tableau: list[list[float]] = [
        *([*constraints[i], -1] for i in range(constraint_count)),
        objective_coefficients + [0] * 2,
        [0] * (variable_count + 2),
    ]
    for i in range(constraint_count):
        tableau[i][-2], tableau[i][-1] = tableau[i][-1], tableau[i][-2]
    tableau[-1][variable_count] = 1
    pivot_row = min(range(constraint_count), key=lambda x: tableau[x][-1])

    if tableau[pivot_row][-1] < -EPS:
        pivot(pivot_row, variable_count)
        if not find(1) or tableau[-1][-1] < -EPS:
            return -inf, None

    for i in range(constraint_count):
        if basic_variables[i] == -1:
            pivot(
                i,
                min(
                    range(variable_count),
                    key=lambda x: (tableau[i][x], nonbasic_variables[x]),
                ),
            )

    if not find(0):
        return -inf, None

    solution_vector = [0.0] * variable_count
    for i in range(constraint_count):
        if 0 <= basic_variables[i] < variable_count:
            solution_vector[basic_variables[i]] = tableau[i][-1]

    objective_value = sum(
        objective_coefficients[i] * solution_vector[i] for i in range(variable_count)
    )

    return objective_value, solution_vector


def branch_and_bound(constraints: list[list[float]]) -> int | None:
    variable_count = len(constraints[0]) - 1
    best_objective_value = inf
    best_solution = None

    def branch(constraints: list[list[float]]) -> None:
        nonlocal best_objective_value, best_solution

        objective_value, solution_vector = simplex(constraints, [1] * variable_count)
        if (
            objective_value + EPS >= best_objective_value
            or objective_value == -inf
            or solution_vector is None
        ):
            return

        fractional_variable_index, fractional_variable_value = next(
            (
                (i, int(e))
                for i, e in enumerate(solution_vector)
                if abs(e - round(e)) > EPS
            ),
            (-1, 0),
        )
        if fractional_variable_index == -1:
            if objective_value + EPS < best_objective_value:
                best_objective_value, best_solution = (
                    objective_value,
                    [round(x) for x in solution_vector],
                )
        else:
            s = [0.0] * variable_count + [fractional_variable_value]
            s[fractional_variable_index] = 1
            branch(constraints + [s])
            s = [0.0] * variable_count + [~fractional_variable_value]
            s[fractional_variable_index] = -1
            branch(constraints + [s])

    branch(constraints)

    return round(best_objective_value) if best_objective_value != inf else None


def build_constraints(buttons: list[int], joltage: list[int]) -> list[list[float]]:
    variable_count = len(joltage)
    button_count = len(buttons)

    constraints = [
        [0.0] * (button_count + 1) for _ in range(2 * variable_count + button_count)
    ]

    for i in range(len(buttons)):
        constraints[~i][i] = -1
        for bit_position in range(variable_count):
            if buttons[i] >> bit_position & 1:
                constraints[bit_position][i] = 1
                constraints[bit_position + variable_count][i] = -1

    for i in range(variable_count):
        constraints[i][-1] = joltage[i]
        constraints[i + variable_count][-1] = -joltage[i]

    return constraints


total_score = sum(
    presses
    for _, buttons, joltage in input_machines()
    if (presses := branch_and_bound(build_constraints(buttons, joltage))) is not None
)

assert total_score == 15883
