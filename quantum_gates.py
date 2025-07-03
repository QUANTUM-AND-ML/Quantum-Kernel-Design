# Define single-qubit gates that do not require parameters
# These gates have fixed matrix representations
single_qubit_gates_without_parameters = [
    'i',    # Identity gate
    'x',    # Pauli-X gate
    'y',    # Pauli-Y gate
    'z',    # Pauli-Z gate
    'h',    # Hadamard gate
    's',    # S gate (phase gate with π/2 phase)
    'sdg',  # S† gate (inverse of the S gate)
    't',    # T gate (phase gate with π/4 phase)
    'tdg',  # T† gate (inverse of the T gate)
    'sx',   # square-root of X gate
    'sxdg'  # inverse square-root of X gate
]

# Define single-qubit gates that require parameters
# These usually take a rotation angle as a parameter
single_qubit_gates_with_parameters = [
    'rx',   # rotation around the X axis
    'ry',   # rotation around the Y axis
    'rz'    # rotation around the Z axis
]

# Define two-qubit gates
two_qubit_gates = [
    'cx',   # controlled-X gate (CNOT)
    'cz',   # controlled-Z gate
    'swap'  # swap gate
]