def test_version():
    import digitalmeve

    # Vérifie que la version exposée par le package
    # correspond bien à celle définie dans src/digitalmeve/__init__.py
    assert hasattr(digitalmeve, "__version__")
    assert digitalmeve.__version__ == "1.7.1-dev"
