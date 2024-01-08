from project import get_todays_word, get_valid_words, check_guess

def test_get_todays_word():
    assert len(get_todays_word()) == 5

def test_get_valid_words():
    assert len(get_valid_words()) == 12920

def test_check_guess():
    assert check_guess("AUDIO", {'guess': ['_', '_', '_', '_', '_'], 'colors': ['\x1b[37m', '\x1b[37m', '\x1b[37m', '\x1b[37m', '\x1b[37m']}, "LEERY") == {'guess': ['A', 'U', 'D', 'I', 'O'], 'colors': ['\x1b[37m', '\x1b[37m', '\x1b[37m', '\x1b[37m', '\x1b[37m']}
    assert check_guess("AUDIO", {'guess': ['_', '_', '_', '_', '_'], 'colors': ['\x1b[37m', '\x1b[37m', '\x1b[37m', '\x1b[37m', '\x1b[37m']}, "STAMP") == {'guess': ['A', 'U', 'D', 'I', 'O'], 'colors': ['\x1b[33m', '\x1b[37m', '\x1b[37m', '\x1b[37m', '\x1b[37m']}
    assert check_guess("SHINE", {'guess': ['_', '_', '_', '_', '_'], 'colors': ['\x1b[37m', '\x1b[37m', '\x1b[37m', '\x1b[37m', '\x1b[37m']}, "SLIMY") == {'guess': ['S', 'H', 'I', 'N', 'E'], 'colors': ['\x1b[32m', '\x1b[37m', '\x1b[32m', '\x1b[37m', '\x1b[37m']}