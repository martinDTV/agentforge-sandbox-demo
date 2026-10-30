"""Pruebas unitarias propias para validate_email."""

import pytest

from mailcheck import validate_email


def test_simple_valid() -> None:
    assert validate_email("user@example.com") is True


def test_subdomain_valid() -> None:
    assert validate_email("a@b.c.org") is True


def test_mixed_case_valid() -> None:
    assert validate_email("User@Example.COM") is True


def test_plus_tag_valid() -> None:
    assert validate_email("user+tag@example.com") is True


def test_underscore_valid() -> None:
    assert validate_email("u_s_e_r@example.io") is True


def test_percent_valid() -> None:
    assert validate_email("u%er@example.io") is True


def test_hyphen_in_domain_valid() -> None:
    assert validate_email("user@my-host.com") is True


def test_empty_string_invalid() -> None:
    assert validate_email("") is False


def test_no_at_invalid() -> None:
    assert validate_email("userexample.com") is False


def test_double_at_invalid() -> None:
    assert validate_email("user@@example.com") is False


def test_empty_local_invalid() -> None:
    assert validate_email("@example.com") is False


def test_empty_domain_invalid() -> None:
    assert validate_email("user@") is False


def test_leading_dot_local_invalid() -> None:
    assert validate_email(".user@example.com") is False


def test_trailing_dot_local_invalid() -> None:
    assert validate_email("user.@example.com") is False


def test_consecutive_dots_local_invalid() -> None:
    assert validate_email("us..er@example.com") is False


def test_local_too_long_invalid() -> None:
    assert validate_email("a" * 65 + "@example.com") is False


def test_total_too_long_invalid() -> None:
    local = "a" * 60
    domain = "b" * 63 + "." + "c" * 63 + "." + "d" * 63 + ".com"
    assert validate_email(f"{local}@{domain}") is False


def test_single_label_domain_invalid() -> None:
    assert validate_email("user@localhost") is False


def test_tld_with_digit_invalid() -> None:
    assert validate_email("user@example.c0m") is False


def test_tld_one_char_invalid() -> None:
    assert validate_email("user@example.c") is False


def test_leading_hyphen_domain_invalid() -> None:
    assert validate_email("user@-example.com") is False


def test_trailing_hyphen_domain_invalid() -> None:
    assert validate_email("user@example-.com") is False


def test_space_in_local_invalid() -> None:
    assert validate_email("us er@example.com") is False


def test_trailing_space_invalid() -> None:
    assert validate_email("user@example.com ") is False


@pytest.mark.parametrize("value", [None, 42, b"user@example.com", 3.14])
def test_non_string_raises_type_error(value: object) -> None:
    with pytest.raises(TypeError):
        validate_email(value)  # type: ignore[arg-type]
