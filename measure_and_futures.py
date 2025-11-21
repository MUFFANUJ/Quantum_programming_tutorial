from ket import *
import ket


def main():
    print("\n=== Measurement & Futures Example ===")

    p = ket.Process(execution="live")

    # Allocate two qubits in |00⟩
    a, b = p.alloc(2)

    # Create a Bell state: apply H to a, then CNOT(a, b)
    CNOT(H(a), b)

    # Measure both qubits; measure(...) returns a "future" object.
    m0 = measure(a)
    m1 = measure(b)

    # Accessing .value triggers execution and yields classical bits 0 or 1
    print("Measurements:", m0.value, m1.value)


if __name__ == "__main__":
    main()
