from ket import *
import ket

from helpers import readable_dump


def main():
    print("\n=== Example 1: Bell pair ===")

    # Create a live process (so gates execute immediately)
    p = ket.Process(execution="live")

    # Allocate 2 qubits (both start in |0⟩)
    a, b = p.alloc(2)

    # Apply Hadamard to the first qubit: |0⟩ -> (|0⟩ + |1⟩)/sqrt(2)
    H(a)

    # Apply CNOT: control = a, target = b
    # This entangles them into (|00⟩ + |11⟩)/sqrt(2)
    CNOT(a, b)

    # Dump and print the state in a readable form
    d = dump(a + b)
    readable_dump(d)


if __name__ == "__main__":
    main()
