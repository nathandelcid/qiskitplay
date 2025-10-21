# ================================================================
# Function: get_inverse_cir
# ================================================================
# Purpose:
#   Given a QuantumCircuit object, this function returns a new circuit
#   that represents the *inverse* (or adjoint) of the input circuit.
#   Running input_cir followed by its inverse_cir should ideally act
#   as the identity operation on all qubits (i.e., return the state
#   back to its original configuration).
#
# Notes:
#   - Qiskit provides a built-in .inverse() method to automatically
#     generate the inverse of a circuit, as long as all its gates are
#     invertible.
#   - Some circuits cannot be inverted directly (for example, if they
#     contain final measurements). In that case, the code removes
#     measurement operations before inverting.
#
# To complete:
#   You may replace or extend this logic depending on your assignment
#   requirements — for example, to manually build or verify the inverse.
# ================================================================

from qiskit import QuantumCircuit
from qiskit.circuit.exceptions import CircuitError


def get_inverse_cir(input_cir: QuantumCircuit):
    """
    Return the inverse (adjoint) of the given QuantumCircuit.

    Args:
        input_cir (QuantumCircuit): The original circuit to invert.

    Returns:
        QuantumCircuit: A new circuit that is the inverse of input_cir.
    """

    # ------------------------------------------------------------
    # Attempt to use Qiskit's built-in circuit inversion
    # ------------------------------------------------------------
    try:
        # This will fail if the circuit includes non-invertible ops
        # such as measurements or resets.
        inverse_cir = input_cir.inverse()

    # ------------------------------------------------------------
    # Handle circuits that cannot be directly inverted
    # ------------------------------------------------------------
    except CircuitError:
        # Make a copy of the input circuit to avoid modifying it
        qc = input_cir.copy()

        # Remove any final measurement operations (these are not invertible)
        qc.remove_final_measurements()

        # Now safely generate the inverse of the measurement-free circuit
        inverse_cir = qc.inverse()

    # ------------------------------------------------------------
    # Return the resulting inverse circuit
    # ------------------------------------------------------------
    # When executed sequentially with input_cir, this should yield
    # an overall identity transformation on all qubits:
    #
    #     input_cir followed by inverse_cir ≈ Identity
    #
    # You may optionally verify this property by composing them and
    # simulating the result.
    # ------------------------------------------------------------

    return inverse_cir
