def normalize_email(address: str) -> str:
    """Normalize an email address by lowercasing the domain part.

    - If address is not a str, raise TypeError.
    - If address contains no '@', return it intact.
    - Otherwise, lowercase only the domain (part after the last '@'),
      leaving the local part unchanged.
    """
    if not isinstance(address, str):
        raise TypeError(f"Expected str, got {type(address).__name__!r}")
    if "@" not in address:
        return address
    local, _, domain = address.rpartition("@")
    return f"{local}@{domain.lower()}"
