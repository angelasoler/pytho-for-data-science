import sys


def main():
    if (len(sys.argv) < 2):
        sys.exit()

    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        e = "argument is not an integer"
        print(f"AssertionError: {e}")
        sys.exit()
    if n % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


if __name__ == "__main__":
    main()
