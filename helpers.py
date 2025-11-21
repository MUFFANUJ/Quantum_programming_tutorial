from ket import *
import ket

def readable_dump(dump_obj):
    """
    Try to extract a plain-text representation from dump_obj.show()
    and print it. Falls back to repr(...) if necessary.
    """
    try:
        out = dump_obj.show()
        # If it's already a string -> print it
        if isinstance(out, str):
            print(out)
            return

        # Try common attributes that may contain latex/text
        for attr in ("data", "_repr_latex_", "latex", "text", "_repr_html_"):
            if hasattr(out, attr):
                val = getattr(out, attr)
                try:
                    to_print = val() if callable(val) else val
                except Exception:
                    to_print = val
                if isinstance(to_print, str) and to_print.strip():
                    print(to_print)
                    return

        # Try str() fallback
        s = str(out)
        if s and not s.startswith("<IPython.core.display"):
            print(s)
            return
    except Exception as e:
        print("dump.show() attempt raised:", repr(e))

    # Last resort: print repr and minimal __dict__
    try:
        print("Unable to extract plain text from dump object. repr(dump_obj):")
        print(repr(dump_obj))
        dct = getattr(dump_obj, "__dict__", None)
        if dct:
            simple = {k: (str(v)[:300]) for k, v in dct.items()}
            print("\nPartial dump.__dict__:")
            for k, v in simple.items():
                print(f"{k}: {v}")
    except Exception as e:
        print("Also failed inspecting dump object:", repr(e))
