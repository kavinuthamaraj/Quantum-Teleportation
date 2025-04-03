# 🔗 Quantum Teleportation Simulation
This project simulates Quantum Teleportation using Qiskit, demonstrating how quantum information can be transferred between two parties (Alice & Bob) using entanglement and classical communication.

## 📌 Features
✅ Implements Quantum Teleportation for an arbitrary 1-qubit quantum state.
✅ Uses entanglement and classical communication for state transfer.
✅ Runs on the Qiskit AerSimulator for fast and accurate results.
✅ Generates a circuit diagram and a histogram of measurement results for visualization.

## 🛠️ Requirements
Make sure you have the following installed:

Python (>=3.8)

Qiskit (>=1.2)

Matplotlib (for visualization)

## 📜 Code Overview
1️⃣ Entanglement Setup
🔹 A 3-qubit quantum circuit is created.
🔹 Qubit 1 and 2 are entangled using a Hadamard + CNOT gate.

2️⃣ Quantum State Preparation
🔹 Alice prepares qubit 0 in an arbitrary quantum state.
🔹 A Hadamard gate puts it in superposition, and an Rz(π/4) gate applies an additional phase rotation.

3️⃣ Teleportation Protocol
🔹 Alice applies a CNOT + Hadamard transformation.
🔹 Alice measures her qubits, collapsing the quantum state.
🔹 The measurement results are sent classically to Bob.

4️⃣ Bob’s Correction
🔹 Bob applies conditional quantum gates (X & Z) based on Alice’s measurements.
🔹 The original quantum state is successfully reconstructed at Bob’s side.

5️⃣ Results & Visualization
🔹 The histogram of measurement outcomes is generated.
🔹 The circuit diagram is displayed for clarity.

## 📊 Expected Output

![Quantum Teleportation Circuit](images/circuit_diagram.png)

![Quantum Teleportation Circuit](images/histogram.png)



🏗️ Future Enhancements
🚀 Extend teleportation to multi-qubit quantum states.
🚀 Implement teleportation on IBM's real quantum hardware.
🚀 Add a GUI interface to visualize the teleportation process interactively.

📜 License
This project is licensed under the MIT License.
