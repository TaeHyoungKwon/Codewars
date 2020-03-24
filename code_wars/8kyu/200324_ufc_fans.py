MCGREGOR_QUOTE = "I'd like to take this chance to apologize.. To absolutely NOBODY!"
GEORGE_SAINT_PIERRE_QUOTE = "I am not impressed by your performance."

GEORGE_SAINT_PIERRE = 'george saint pierre'


def quote(fighter):
    if fighter.lower() == GEORGE_SAINT_PIERRE:
        return GEORGE_SAINT_PIERRE_QUOTE
    return MCGREGOR_QUOTE