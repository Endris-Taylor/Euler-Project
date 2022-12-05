"""euler_22.py Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""

from string import ascii_uppercase


_ALPHABET: 'list[str]' = [letter for letter in ascii_uppercase]


def get_letter_position(letter: str) -> int:
    if len(letter) > 1:
        raise NotImplemented("This only accounts for one letter at a time.")

    return _ALPHABET.index(letter) + 1


def get_name_score(index: int, name: str) -> int:
    values: 'list[int]' = []

    for letter in name:
        values.append(get_letter_position(letter))

    return index * sum(values)


def main() -> None:
    path_to_file: str = './resources/p022_names.txt'
    names: 'list[str]' = []
    scores: 'list[int]' = []
    name_scores_total: int = 0

    # Load names from file then close it.
    with open(path_to_file) as f:
        contents = f.readlines()  # Read File.
        names = contents[0].replace('"', '').split(',')  # Put contents in a workable format.

    for index, name in enumerate(names):
        temp = get_name_score(index + 1, name)
        scores.append(temp)

    name_scores_total = sum(scores)

    print(f"The total for all of the names scores in the file is {name_scores_total:,}.")


if __name__ == "__main__":
    main()
