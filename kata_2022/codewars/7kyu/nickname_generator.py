def nickname_generator(name: str) -> str:
    if len(name) < 4:
        return "Error: Name too short"

    return name[:4] if name[2] in "aeiou" else name[:3]


class TestNickNameGenerator:
    def test_nickname_generator(self):
        assert nickname_generator(name="Jimmy") == "Jim"
        assert nickname_generator(name="Jeannie") == "Jean"
        assert nickname_generator(name="TH") == "Error: Name too short"

"""
Problem
* You should make nickname_generator function that return name is shorten by specific conditions.

Solution
* You should write codes by conditions below

Conditions
    * Happy path
        1. A 3rd letter is consonant, should return the first 3 letters.
        2. A 3rd letter is a vowel, should return the first 4 letters
    * Unhappy path
        3. The string that maybe argument name is less than 4 characters, should return "Error:Name too short."
    * Common
        4. Input will always have the first lettter capitalised and the rest lowercase

Steps

Verification
    * Happy path
        1. A 3rd letter is consonant, should return the first 3 letters.
        2. A 3rd letter is a vowel, should return the first 4 letters
    * Unhappy path
        3. The string that maybe argument name is less than 4 characters, should return "Error:Name too short."
"""