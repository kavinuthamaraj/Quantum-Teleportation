from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(3, 2)

qc.h(0)  
qc.rz(3.14/4, 0) 

qc.h(1)
qc.cx(1, 2)

qc.cx(0, 1)
qc.h(0)

qc.measure(0, 0)
qc.measure(1, 1)

qc.cx(1, 2)
qc.cz(0, 2)

print("Quantum Teleportation Circuit:")
qc.draw("mpl")
plt.show()

backend = Aer.get_backend('qasm_simulator')

compiled_circuit = transpile(qc, backend)
job = backend.run(compiled_circuit, shots=1000)
result = job.result()

counts = result.get_counts()
print("Quantum Teleportation Results:", counts)

plot_histogram(counts)
plt.show()
