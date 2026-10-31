import pytest

from mailcheck.normalize import normalize_email


def test_basic_normalization():
    assert normalize_email("User@Example.COM") == "User@example.com"


def test_no_at_sign_returns_intact():
    assert normalize_email("noatsign") == "noatsign"


def test_type_error_on_non_str():
    with pytest.raises(TypeError):
        normalize_email(123)  # type: ignore[arg-type]


def test_type_error_on_none():
    with pytest.raises(TypeError):
        normalize_email(None)  # type: ignore[arg-type]


def test_local_part_preserved():
    assert normalize_email("First.Last+tag@Domain.ORG") == "First.Last+tag@domain.org"


def test_already_lowercase_domain():
    assert normalize_email("user@example.com") == "user@example.com"


def test_multiple_at_signs_uses_last():
    assert normalize_email("a@b@Example.COM") == "a@b@example.com"


def test_empty_string_returns_intact():
    assert normalize_email("") == ""


def test_only_at_sign():
    assert normalize_email("@") == "@"


def test_uppercase_local_unchanged():
    assert normalize_email("USER@EXAMPLE.COM") == "USER@example.com"
