"""
A deliberately overlong implementation: build a greeting string.

Behavior (keep exactly the same):
- Capitalize the first letter of the name and lower the rest.
- If name is None or only whitespace -> use "Friend".
- `times` ≥ 1; if a smaller number is passed, treat it as 1.
- If `excited=True`, use "!" else "." at the end.
- Separate repeated greetings with a single space.

Examples:
  format_greeting("alice", 1, False) -> "Hello, Alice."
  format_greeting("alice", 2, True)  -> "Hello, Alice! Hello, Alice!"
  format_greeting("   ", 3, True)    -> "Hello, Friend! Hello, Friend! Hello, Friend!"
"""

def format_greeting(name, times=1, excited=False):
    # --- BEGIN intentionally clunky code ---
    if name is None:
        n = "Friend"
    else:
        if isinstance(name, str):
            stripped = name.strip()
            if stripped == "":
                n = "Friend"
            else:
                first = stripped[0].upper()
                rest = stripped[1:].lower() if len(stripped) > 1 else ""
                n = first + rest
        else:
            n = "Friend"

    if times is None:
        t = 1
    else:
        try:
            t = int(times)
        except Exception:
            t = 1
    if t < 1:
        t = 1

    if excited is True:
        end = "!"
    else:
        end = "."

    # build message
    pieces = []
    i = 0
    while i < t:
        pieces.append("Hello, " + n + end)
        i = i + 1
    msg = ""
    j = 0
    while j < len(pieces):
        if j == 0:
            msg = pieces[j]
        else:
            msg = msg + " " + pieces[j]
        j = j + 1
    return msg
    # --- END intentionally clunky code ---
