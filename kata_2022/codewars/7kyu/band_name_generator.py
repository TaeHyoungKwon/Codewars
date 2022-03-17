def band_name_generator(name: str) -> str:
    if name.endswith(name[0]):
        combined = name[:-1] + name
        return combined.capitalize()
    else:
        return f"The {name.capitalize()}"


class TestBandNameGenerator:
    def test_band_name_generator(self):
        assert band_name_generator(name="dolphin") == "The Dolphin"
        assert band_name_generator(name="carrier") == "The Carrier"

    def test_band_name_generator_on_name_starts_and_ends_with_the_same_letter(self):
        assert band_name_generator(name="alaska") == "Alaskalaska"
        assert band_name_generator(name="swiss") == "Swisswiss"


"""
Problem
    * Complete the function that takes a noun as a string, and returns solution as conditions
Solution
    * Write a code as conditions
Conditions
    * if name is not a noun starts and ends with the same letter,
        * should be adding 'The' in front of name with Capitalized first letter
    * if name is a noun starts and endfs with the same letter,
        * should be repeating the name twice and connect them together with the first and last letter, combined into
        one word
Step
    1. Check name if it is a noun startrs and ends with the same letter or not
        if it is false,
            * we should return name that is capitalied first letter with 'The' in front of that
        if it is true,
            * Combine two same two words with slicing like this
                * first one -> result[:-1] / second one -> result(origin)
            * And return combined name that is capitalized first letter
Test
    1. "dolphin" -> "The Dolphin"
    2. "alaska" -> "Alaskalaska"
"""
