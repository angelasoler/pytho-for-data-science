def ft_tqdm(lst: range) -> None:
    """ print a loading bar of len(lst) elements

        lst: iterated list
    """
    for l in lst:
        perc = round(l / len(lst) * 100)
        n = round(perc / 10)
        bar = ("=====" * n) + ">"
        print(f'{perc:{3}}%|[{bar:{51}}]| {(l + 1):{3}}/{len(lst):{3}}', end='\r')
        yield l
