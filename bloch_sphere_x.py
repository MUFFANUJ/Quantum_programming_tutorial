from ket import *
import ket


def main():
    print("\n=== Bloch sphere (Pauli X) example ===")

    # Live process
    p = ket.Process(execution="live")

    # Single qubit initialized to |0⟩
    q = p.alloc()

    # Pauli X flips |0⟩ to |1⟩
    X(q)

    # Dump the state and show Bloch sphere info
    d = dump(q)
    # In a notebook, d.sphere() would show a 3D Bloch sphere.
    print(d.sphere().show())


if __name__ == "__main__":
    main()
