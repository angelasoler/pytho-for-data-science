import sys
from ft_filter import ft_filter


def filter_string(s, size):
    """ Prints the list of words on s that are greater than size

    Args:
        s (string): string to filter its words
        size (int): length that the word should be greater than
    """
    f_len = lambda string: len(string) > size  # noqa: E731
    word_list = [word for word in s.split()]
    ret = ft_filter(f_len, word_list)
    print(ret)


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit()

    try:
        n = int(sys.argv[2])
    except ValueError:
        e = "the arguments are bad"
        print(f"AssertionError: {e}")
        sys.exit()
    filter_string(sys.argv[1], n)


if __name__ == "__main__":
    main()
