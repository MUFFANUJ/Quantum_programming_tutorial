import ket
from ket import *


# Quantum teleportation example (ket-lang)
# This is a fully working program with detailed comments.


def entangle(a, b):
    """Create a Bell pair between qubits `a` and `b`.

    Steps:
      1. Apply H(a) to create superposition.
      2. Apply CNOT(a, b) to entangle them.

    Final state: (|00⟩ + |11⟩) / sqrt(2)
    """
    H(a)
    CNOT(a, b)
    return a, b


def teleport(quantum_message, entangled_qubit):
    """Alice's Bell-measurement step.

    This maps the Bell basis to the computational basis and measures.

    Steps:
      1. CNOT(message -> entangled_qubit)
      2. H(message)
      3. Measure both qubits.

    Returns:
        (m1, m2) — two classical bits (0/1) that Alice sends to Bob.
    """
    # Step 1: entangle the message qubit with Alice's entangled qubit
    CNOT(quantum_message, entangled_qubit)

    # Step 2: Hadamard on the message qubit
    H(quantum_message)

    # Step 3: measure both qubits to get classical bits
    m1 = measure(quantum_message).value
    m2 = measure(entangled_qubit).value

    return m1, m2


def decode(classical_message, qubit):
    """Bob's correction step.

    Given classical bits (m1, m2), apply:
      - X if m2 == 1
      - Z if m1 == 1
    to recover the original state on `qubit`.
    """
    m1, m2 = classical_message

    # Apply X if second bit is 1
    if m2 == 1:
        X(qubit)

    # Apply Z if first bit is 1
    if m1 == 1:
        Z(qubit)


def main():
    # Create a live ket process so gates and measurements act immediately
    p = ket.Process(execution="live")

    # --- Prepare the message qubit Alice wants to teleport ---
    alice_message = p.alloc()   # fresh qubit in |0⟩

    # Build a known test state |−⟩ = Z H |0⟩
    H(alice_message)  # |+⟩
    Z(alice_message)  # |−⟩

    # --- Create an entangled Bell pair shared between Alice and Bob ---
    q = p.alloc(2)
    alice_qubit, bob_qubit = entangle(q[0], q[1])

    # --- Alice teleports her message to Bob ---
    classical_message = teleport(alice_message, alice_qubit)

    # --- Bob receives the bits and decodes ---
    decode(classical_message, bob_qubit)

    # --- Verification step ---
    # If teleportation worked, Bob's qubit is now |−⟩.
    # For |−⟩, H|−⟩ = |1⟩, so measurement should be 1 with probability 1.
    H(bob_qubit)
    result = measure(bob_qubit).value

    print("Expected 1, got:", result)


if __name__ == "__main__":
    main()
