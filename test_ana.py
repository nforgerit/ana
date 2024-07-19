from ana import is_anagram


def test_for_empty_strings():
    res = is_anagram("", "")
    exp = True
    assert res == exp

def test_newline_edgecase():
    res = is_anagram("\nHumus", "Muhus\n")
    exp = True
    assert res == exp

def test_anagram_with_point():
    res = is_anagram("sun.light", "hustling.")
    exp = True
    assert res == exp

def test_fails_with_space_and_dot():
    res = is_anagram(" ", ".")
    exp = False
    assert res == exp

def test_no_anagram():
    res = is_anagram("muh", "kuh")
    exp = False
    assert res == exp

def test_no_anagram2():
    res = is_anagram("pointers", "thickens")
    exp = False
    assert res == exp

