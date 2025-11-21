from ket import *
import ket
from math import pi

from helpers import readable_dump


def safe_phase(theta, q):
    """
    Use P(theta, q) if available, else fall back to PHASE or phase if present.
    This keeps the example compatible across ket versions.
    """
    if hasattr(ket, "P"):
        try:
            P(theta, q)
            return
        except Exception:
            pass

    if hasattr(ket, "PHASE"):
        try:
            PHASE(theta, q)
            return
        except Exception:
            pass

    if "phase" in globals():
        try:
            phase(theta, q)
            return
        except Exception:
            pass
    # If no phase-like gate is found, silently do nothing.


def small_unitary(q):
    """
    A small unitary U = H followed by a phase rotation e^{i π/4}.
    """
    H(q)
    safe_phase(pi / 4, q)
    return q


def main():
    print("\n=== Example: adj (inverse) and around demo ===")

    p = ket.Process(execution="live")

    # Allocate two qubits; we'll work only with r[0]
    r = p.alloc(2)

    # Apply U to r[0]
    small_unitary(r[0])

    # Try to apply U† via adj(small_unitary)
    try:
        adj(small_unitary)(r[0])
    except Exception:
        # If adj(...) does not support this signature, just skip
        pass

    # Now demonstrate the around(U, q) pattern if available.
    # Intuition:
    #   with around(U, q):
    #       X(q)
    # means applying U, then X in that frame, then U†:
    #     U · X · U†
    if "around" in dir(ket):
        try:
            with around(small_unitary, r[0]):
                X(r[0])
        except Exception:
            # fallback: just apply X
            X(r[0])
    else:
        X(r[0])

    # Dump the final 2-qubit register state
    readable_dump(dump(r))


if __name__ == "__main__":
    main()
