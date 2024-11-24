import sys
import string

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ':  '/'
}


def morse_code(s):
    """ prints the morse code equivalent to s

        s: string to traduce
    """
    s = ''.join([MORSE_CODE_DICT[s[i]] + ' ' for i in range(0, len(s))])
    print(s)


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "bad arguments"
        s = ''.join(sys.argv[1][i].upper() for i in range(0, len(sys.argv[1])))
        for i in range(0, len(s)):
            assert s[i] in string.ascii_uppercase or \
                    s[i] in string.digits or \
                    s[i] == ' ', "bad arguments"
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        sys.exit()
    morse_code(s)
