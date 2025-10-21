# ================================================================
# Quantum Half Adder
# ================================================================
# This module implements a quantum half adder using Qiskit.
# The circuit takes two classical bits (a_val, b_val), encodes
# them as quantum states |a⟩ and |b⟩, computes:
#   sum   = a XOR b   (stored in qubit b)
#   carry = a AND b   (stored in qubit carry)
# It then measures all qubits to verify correctness.
# ================================================================

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2 as Sampler

def half_adder(a_val: int, b_val: int):
    """
    Builds and simulates a quantum half adder circuit.

    Args:
        a_val (int): Classical input bit (0 or 1) for input a.
        b_val (int): Classical input bit (0 or 1) for input b.

    Returns:
        QuantumCircuit: The constructed quantum circuit representing the half adder.
    """

    # Create a quantum circuit with 3 qubits:
    # q0 -> input a
    # q1 -> input b (also used for the sum output)
    # q2 -> carry output
    qc = QuantumCircuit(3)
    a, b, carry = 0, 1, 2

    # ------------------------------------------------------------
    # Initialize input qubits according to classical input values
    # ------------------------------------------------------------
    if a_val == 1:
        qc.x(a)  # set qubit a to |1⟩
    if b_val == 1:
        qc.x(b)  # set qubit b to |1⟩

    qc.barrier()

    # ------------------------------------------------------------
    # Quantum Half Adder Logic
    # ------------------------------------------------------------
    # Carry = a AND b (use Toffoli gate)
    qc.ccx(a, b, carry)

    # Sum = a XOR b (use CNOT gate)
    qc.cx(a, b)

    qc.barrier()

    # ------------------------------------------------------------
    # Measurement
    # ------------------------------------------------------------
    qc.measure_all()

    return qc


qc = half_adder(1, 1)
ideal_simulator = AerSimulator()
sampler = Sampler(mode=ideal_simulator)

job = sampler.run([qc], shots=5)
count_ideal = job.result()[0].data.meas.get_counts()
print('count_ideal:', count_ideal)