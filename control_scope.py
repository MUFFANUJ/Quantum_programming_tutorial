from ket import *
import ket

from helpers import readable_dump


def main():
    print("\n=== Controlled-scope example ===")

    p = ket.Process(execution="live")

    # Allocate three qubits: two controls (c0, c1) and one target (t)
    c0, c1, t = p.alloc(3)

    # X(t) is applied only when both c0 and c1 are |1⟩
    with control(c0, c1):
        X(t)

    # Dump the 3-qubit state: |c0 c1 t⟩
    readable_dump(dump(c0 + c1 + t))


if __name__ == "__main__":
    main()
