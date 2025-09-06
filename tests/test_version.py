diff --git a/tests/test_version.py b/tests/test_version.py
index 3b6c9aa..b1f2a71 100644
--- a/tests/test_version.py
+++ b/tests/test_version.py
@@ -1,10 +1,12 @@
 import digitalmeve
 
 
 def test_version():
     # le package doit exposer __version__
     assert hasattr(digitalmeve, "__version__")
-    # valeur attendue (définie dans src/digitalmeve/__init__.py)
-    assert digitalmeve.__version__ == "1.7.1-dev"
+    # accepte la version release ou la suffixée -dev pour la branche principale
+    v = digitalmeve.__version__
+    assert isinstance(v, str)
+    assert v.startswith("1.7.1"), f"unexpected version: {v}"
