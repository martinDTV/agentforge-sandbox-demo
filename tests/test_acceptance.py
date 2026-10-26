"""Pruebas de aceptación: definen el comportamiento exigido. No se modifican."""

import pytest

from mailcheck import validate_email

VALID = [
    "user@example.com",
    "First.Last+tag@Sub.Example.ORG",
    "a_b%c-d@ex-ample.co",
    "x@y.io",
]

INVALID = [
    "",
    "plainaddress",
    "@example.com",
    "user@",
    "user@@example.com",
    "us er@example.com",
    "user@example.com ",
    ".user@example.com",
    "user.@example.com",
    "us..er@example.com",
    "user@example",
    "user@-example.com",
    "user@example-.com",
    "user@example.c0m",
    "user@example.c",
    "a" * 65 + "@example.com",
    "u@" + "a" * 64 + ".com",
    "a" * 60 + "@" + ("b" * 63 + ".") * 3 + "com",
]


@pytest.mark.parametrize("address", VALID)
def test_accepts_valid_addresses(address: str) -> None:
    assert validate_email(address) is True


@pytest.mark.parametrize("address", INVALID)
def test_rejects_invalid_addresses(address: str) -> None:
    assert validate_email(address) is False


@pytest.mark.parametrize("value", [None, 42, b"user@example.com"])
def test_non_string_input_raises_type_error(value: object) -> None:
    with pytest.raises(TypeError):
        validate_email(value)  # type: ignore[arg-type]
