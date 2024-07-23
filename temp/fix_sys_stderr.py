import sys
if sys.stderr is None:
    import io
    sys.stderr = io.StringIO()
