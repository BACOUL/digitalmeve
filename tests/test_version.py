diff --git a/tests/test_version.py b/tests/test_version.py
index 0000000..0000000 100644
--- a/tests/test_version.py
+++ b/tests/test_version.py
@@ -1,3 +1,6 @@
-def test_version():
-    import digitalmeve
-
-    assert digitalmeve.__version__ == "1.7.1-dev"
+def test_version():
+    import digitalmeve
+
+    # Vérifie que la version exposée par le package
+    # correspond bien à celle définie dans src/digitalmeve/__init__.py
+    assert hasattr(digitalmeve, "__version__")
+    assert digitalmeve.__version__ == "1.7.1-dev"
