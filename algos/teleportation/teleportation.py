from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(3)
# Entangle A and B
qc.h(0)
qc.cx(0, 2)

# Combine message qubit C
qc.cx(0, 1)

fig = qc.draw("mpl")
fig.savefig('qc_01.png')