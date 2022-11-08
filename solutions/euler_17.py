"""euler_17.py Problem 17
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
usage."""

from __future__ import annotations

__num_to_words_1: dict[int, str] = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                                    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                                    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                                    16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
                                    30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                                    90: 'Ninety'}
__num_to_words_2: list[str] = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety',
                               'Hundred',
                               'Thousand']
__do_not_count: list[str] = [" ", "-"]


def number_to_words(number: int) -> tuple[str, int]:
    translation: str = ""
    translation_actual: str = ""
    # translation_actual: str = translation.translate(None, ''.join(__do_not_count))
    if translation := __num_to_words_1.get(number, None) is None:
        if 20 > number <= 99:
            pass
        elif 100 >= number > 1000:
            pass
        else:
            translation = f"{__num_to_words_1.get(1)} {__num_to_words_2.get(-1)}"
    elif temp := __num_to_words_1.get(number, None):
        translation = temp

    else:
        NotImplemented(f"Case for Number<{number}> Not Implemented.")

    print(f"{translation}")

    translation_actual = translation.replace(" ", "").replace(",", "")

    return translation, len(translation_actual)


def main() -> None:
    target: int = 1000
    results: dict[int, tuple[str, int]] = None

    for _, number in enumerate(range(1, target)):
        word, word_count = number_to_words(number=number)
        results[number] = tuple(word, word_count)


if __name__ == "__main__":
    main()
