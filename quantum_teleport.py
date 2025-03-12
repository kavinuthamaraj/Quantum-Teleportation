from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator  # ✅ FIXED: Import from qiskit_aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

#Quantum Circuit - 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

#Entanglement btwn qb1 & qb2
qc.h(1)
qc.cx(1, 2)


qc.x(0)  #Modify Intial State

#Alice - Applies teleportation protocol
qc.cx(0, 1)
qc.h(0)

#Alice's qubits
qc.measure([0, 1], [0, 1])

#Bob - Classical communication
qc.cx(1, 2)
qc.cz(0, 2)

#Bob's qubit
qc.measure(2, 2)


simulator = AerSimulator()

# Transpile & Execute 
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit)  # ✅ FIXED: Using `run()`
result = job.result()


counts = result.get_counts(qc)


print("Quantum Teleportation Results:", counts)

#Histogram
plot_histogram(counts)
plt.show()
