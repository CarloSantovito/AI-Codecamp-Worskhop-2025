from greeting import format_greeting

def test_single_plain():
    assert format_greeting("alice") == "Hello, Alice."

def test_repetition_excited():
    assert format_greeting("alice", 2, True) == "Hello, Alice! Hello, Alice!"

def test_blank_name_defaults():
    assert format_greeting("   ", 3, True) == (
        "Hello, Friend! Hello, Friend! Hello, Friend!"
    )

def test_none_name_and_times_guard():
    assert format_greeting(None, 0) == "Hello, Friend."

def test_mixed_case_normalization():
    assert format_greeting("jOsE") == "Hello, Jose."
