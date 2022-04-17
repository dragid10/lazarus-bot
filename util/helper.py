def null_or_empty(input: str) -> bool:
    return input is None or input.casefold().strip() == ""
