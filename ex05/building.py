import sys
import string


def count_strconst(s, str_const):
    """Return the total char of str_const type

    s:
        string to count from
    str_const:
        string class const type
    """
    n = 0
    for char in str_const:
        n = n + s.count(char)
    return n

def main():
    try:
        assert len(sys.argv) <= 2, "Too many arguments"
    except AssertionError as e:
        print("Assertion Error: {e}")
    if (len(sys.argv) == 1):
        try:
            text = input("What is the text to count?\n")
        except EOFError:
            sys.exit()
        text += '\n'
    else:
        text = sys.argv[1]
    print("The text contains 13 characters:")
    print(f"{count_strconst(text, string.ascii_uppercase)} upper letters")
    print(f"{count_strconst(text, string.ascii_lowercase)} lower letters")
    print(f"{count_strconst(text, string.punctuation)} punctuation marks")
    print(f"{count_strconst(text, string.whitespace)} spaces")
    print(f"{count_strconst(text, string.digits)} digits")

if __name__ == "__main__":
    main()

