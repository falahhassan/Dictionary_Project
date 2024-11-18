from difflib import get_close_matches


def close_match(word, file):
    matches = get_close_matches(word, file)
    return matches

