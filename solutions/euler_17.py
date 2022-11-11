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
HUNDRED = 'Hundred'
THOUSAND = 'Thousand'
__do_not_count: list[str] = [" ", "-"]


def number_to_words(number: int, *args, **kwargs) -> tuple[str, int]:
    translation: str = ""
    translation_actual: str = ""
    # translation_actual: str = translation.translate(None, ''.join(__do_not_count))
    if translation := __num_to_words_1.get(number, None) is None:
        if 20 < number <= 99:
            # This should be the only block of code executed in the recursive function.
            temp = (number // 10) * 10
            search = number - temp

            # e.g. Thirty-Two
            translation = f"{__num_to_words_1.get(temp)}-{__num_to_words_1.get(search)}"

        elif number < 1000 and (number - ((number // 100) * 100) == 0):
            # e.g. Three Hundred.
            temp = number // 100  # what 'Hundred' is it?
            translation = f"{__num_to_words_1.get(temp)} {HUNDRED}"

        elif number < 1000 and (number - ((number // 100) * 100) > 0):
            temp: int = number // 100 # what 'Hundred' is it?
            sec_temp: int = number - (temp * 100)
            sec_trans, _ = number_to_words(sec_temp, logging=False)  # Recursive to get the remainder of the word.
            translation = f"{__num_to_words_1.get(temp)} {HUNDRED} and {sec_trans}"
        else:
            # Its 1000, not processing, just accessing.
            translation = f"{__num_to_words_1.get(1)} {THOUSAND}"

    elif temp := __num_to_words_1.get(number, None):
        translation = temp  # In the dictionary already.

    else:
        NotImplemented(f"Case for Number<{number}> Not Implemented.")

    if logging := kwargs.get('logging', True) is True:
        print(f"{translation}")

    translation_actual = translation.replace(" and ", "").replace(" ", "").replace(",", ""). replace("-", "")

    return translation, len(translation_actual)


def main() -> None:
    target: int = 1000
    results: dict[int, tuple[str, int]] = {}

    for _, number in enumerate(range(1, target + 1)):
        word, word_count = number_to_words(number=number, logging=True)  # You can remove flag to check spelling yada.
        results[number] = word, word_count

    else:
        sum_of_words: int = sum([results.get(x)[1] for x in results])
        output: str = "If all the numbers from 1 to 1000 (One Thousand) inclusive were written out in words, " + \
                      f"{sum_of_words} letters would be used."
        print(output)


if __name__ == "__main__":
    main()
