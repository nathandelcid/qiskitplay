# Quantum Playground

A comprehensive collection of quantum algorithms, circuits, and experiments designed for learning, experimentation, and exploration of quantum computing concepts using Qiskit and IBM's quantum processing units (QPUs).

## Overview

This repository serves as a playground for quantum computing enthusiasts, researchers, and students to explore various quantum algorithms and circuits. Each implementation includes detailed documentation, examples, and educational insights to help understand quantum computing principles. All implementations are built using Qiskit and can be run on IBM's quantum computers.

## What's Inside

### Current Implementations

- **Quantum Half Adder** (`quantum_half_adder.py`) - A quantum implementation of a half adder circuit using Qiskit, demonstrating quantum logic gates and measurement

### Planned Additions

- **Quantum Gates Library** - Collection of fundamental quantum gates with visualizations
- **Quantum Algorithms** - Implementations of famous algorithms (Deutsch-Jozsa, Grover's, Shor's)
- **Quantum Error Correction** - Examples of quantum error correction codes
- **Quantum Machine Learning** - Quantum machine learning algorithms and circuits
- **Quantum Cryptography** - Quantum key distribution and cryptographic protocols
- **Quantum Simulation** - Quantum simulation of physical systems
- **Quantum Optimization** - QAOA and other quantum optimization algorithms

## Prerequisites

- Python 3.8+
- Qiskit
- Qiskit Aer (for simulation)
- Qiskit IBM Runtime (for IBM QPU access)
- Jupyter Notebook (optional, for interactive examples)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd QPlay
```

2. Install required dependencies:
```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime
```

3. (Optional) Install Jupyter for interactive notebooks:
```bash
pip install jupyter
```

## Getting Started

### Running the Quantum Half Adder

```python
from quantum_half_adder import half_adder
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2 as Sampler

# Create a half adder circuit
qc = half_adder(1, 1)  # Input: a=1, b=1

# Simulate the circuit
ideal_simulator = AerSimulator()
sampler = Sampler(mode=ideal_simulator)
job = sampler.run([qc], shots=1024)
result = job.result()[0].data.meas.get_counts()

print("Measurement results:", result)
```

### Expected Output
For inputs `a=1, b=1`, you should see:
- **Sum**: `1 XOR 1 = 0` (stored in qubit 1)
- **Carry**: `1 AND 1 = 1` (stored in qubit 2)

## Learning Objectives

This playground is designed to help you:

- **Understand Quantum Gates**: Learn how quantum gates work and their classical counterparts
- **Build Quantum Circuits**: Create and manipulate quantum circuits using Qiskit
- **Simulate Quantum Systems**: Run quantum algorithms on simulators
- **Explore Quantum Algorithms**: Implement and understand famous quantum algorithms
- **Visualize Quantum States**: Understand quantum state evolution and measurement

## Educational Resources

Each implementation includes:

- **Detailed Documentation**: Comprehensive comments explaining the quantum mechanics
- **Mathematical Background**: Theoretical foundations of each algorithm
- **Circuit Diagrams**: Visual representations of quantum circuits
- **Example Runs**: Sample outputs and interpretations
- **Further Reading**: Links to relevant papers and resources

## Contributing

We welcome contributions! Here's how you can help:

1. **Add New Algorithms**: Implement quantum algorithms not yet covered
2. **Improve Documentation**: Enhance explanations and add more examples
3. **Fix Bugs**: Report and fix issues in existing implementations
4. **Add Visualizations**: Create circuit diagrams and state visualizations
5. **Write Tests**: Add unit tests for quantum circuits

### Contribution Guidelines

- Follow Python PEP 8 style guidelines
- Include comprehensive docstrings
- Add example usage in each module
- Update this README when adding new features
- Test your implementations thoroughly

## Project Structure

```
QPlay/
├── README.md                    # This file
├── .gitignore                   # Git ignore patterns
├── quantum_half_adder.py       # Quantum half adder implementation
├── algorithms/                  # Quantum algorithms (planned)
├── gates/                      # Quantum gates library (planned)
├── examples/                   # Example notebooks and scripts (planned)
├── tests/                      # Unit tests (planned)
└── docs/                       # Additional documentation (planned)
```

## Quantum Computing Concepts Covered

- **Quantum Gates**: X, CNOT, Toffoli, and other fundamental gates
- **Quantum Circuits**: Building and manipulating quantum circuits
- **Quantum Measurement**: Understanding measurement and collapse
- **Quantum Simulation**: Running quantum algorithms on simulators
- **Quantum Algorithms**: Various quantum algorithms and their applications

## External Resources

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Experience](https://quantum-computing.ibm.com/)
- [Quantum Computing Stack Exchange](https://quantumcomputing.stackexchange.com/)
- [Nielsen & Chuang - Quantum Computation and Quantum Information](https://www.cambridge.org/core/books/quantum-computation-and-quantum-information/)

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- IBM Qiskit team for the excellent quantum computing framework
- Quantum computing community for sharing knowledge and resources
- Contributors who help make this playground better

---

**Happy Quantum Computing!**

*Remember: Quantum computing is still in its early stages, but the possibilities are endless. This playground is here to help you explore those possibilities!*
