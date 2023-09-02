import ctypes

# If you want the answer for part 2, just manually tweak the input file and run this again.


def perform_operation(operation: str, left_input: int, right_input: int) -> int:
    if operation == 'LSHIFT':
        return left_input << right_input
    elif operation == 'RSHIFT':
        return left_input >> right_input
    elif operation == 'AND':
        return left_input & right_input
    elif operation == 'OR':
        return left_input | right_input
    else:
        raise ValueError(f'perform_operation does not recognize operation: {operation}')


def evaluate_wire(wire_defs: dict[str, str], wire_states: dict[str, int], identifier: str) -> int:
    if wire_states[identifier] != -1:
        return wire_states[identifier]

    definition = wire_defs[identifier]
    def_components = definition.split()

    if len(def_components) == 3:
        # handle all operators other than NOT
        left_val = int(def_components[0]) if def_components[0].isnumeric() \
            else evaluate_wire(wire_defs, wire_states, def_components[0])

        right_val = int(def_components[2]) if def_components[2].isnumeric() \
            else evaluate_wire(wire_defs, wire_states, def_components[2])

        wire_states[identifier] = perform_operation(def_components[1], left_val, right_val)
    elif len(def_components) == 2:
        # handle NOT
        input_wire = def_components[1]
        input_value = evaluate_wire(wire_defs, wire_states, input_wire)
        wire_states[identifier] = ~input_value
    else:
        # handle direct wire assignment
        input_value = evaluate_wire(wire_defs, wire_states, definition)
        wire_states[identifier] = input_value

    return wire_states[identifier]


if __name__ == '__main__':
    file = open("input.txt")

    circuit_defs: dict[str, str] = {}
    circuit_state: dict[str, int] = {}

    for line in file:
        front, back = line.split(' -> ')
        wire_name: str = back
        circuit_defs[wire_name.strip()] = front
        try:
            circuit_state[wire_name.strip()] = int(front)
        except ValueError:
            circuit_state[wire_name.strip()] = -1

    for wire_name, wire_state in circuit_state.items():
        if wire_state == -1:
            evaluate_wire(circuit_defs, circuit_state, wire_name)

    print("Circuit evaluation complete.")
    while True:
        wire_name = input("Enter the name of the wire you want to check: ")
        if wire_name in circuit_state.keys():
            print(ctypes.c_ushort(circuit_state[wire_name.strip()]).value)
        else:
            print(f'{wire_name} is not a valid wire name.')
