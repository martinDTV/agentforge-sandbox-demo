"""Validación de direcciones de correo electrónico."""

import re

from mailcheck.normalize import normalize_email

_LOCAL_RE = re.compile(r"^[A-Za-z0-9._%+\-]+$")
_LABEL_RE = re.compile(r"^[A-Za-z0-9]([A-Za-z0-9\-]*[A-Za-z0-9])?$")
_TLD_RE = re.compile(r"^[A-Za-z]{2,}$")


def validate_email(address: str) -> bool:
    """Devuelve True si ``address`` cumple las reglas descritas en README.md."""
    if not isinstance(address, str):
        raise TypeError(f"Expected str, got {type(address).__name__}")

    # Normalize: lowercase domain only, local part intact
    address = normalize_email(address)

    # Rule 6: no whitespace
    if any(c.isspace() for c in address):
        return False

    # Rule 1: exactly one '@'
    if address.count("@") != 1:
        return False

    local, domain = address.split("@")

    # Rule 1: local and domain non-empty
    if not local or not domain:
        return False

    # Rule 2: total length <= 254, local length <= 64
    if len(address) > 254 or len(local) > 64:
        return False

    # Rule 3: local part characters
    if not _LOCAL_RE.match(local):
        return False

    # Rule 3: no leading/trailing dot, no consecutive dots
    if local.startswith(".") or local.endswith("."):
        return False
    if ".." in local:
        return False

    # Rule 4: domain must have at least two labels
    labels = domain.split(".")
    if len(labels) < 2:
        return False

    # Rule 4: each label 1-63 chars, letters/digits/hyphen, no leading/trailing hyphen
    for label in labels:
        if not label or len(label) > 63:
            return False
        if not _LABEL_RE.match(label):
            return False

    # Rule 5: TLD only letters, at least two
    tld = labels[-1]
    if not _TLD_RE.match(tld):
        return False

    return True
