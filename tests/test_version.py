# tests/test_version.py

import digitalmeve


def test_version():
    # le package doit exposer __version__
    assert hasattr(digitalmeve, "__version__")
    # valeur attendue (définie dans src/digitalmeve/__init__.py)
    assert digitalmeve.__version__ == "1.7.1-dev"
