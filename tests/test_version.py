diff --git a/src/digitalmeve/utils.py b/src/digitalmeve/utils.py
index e69de29..d95f3ad 100644
--- a/src/digitalmeve/utils.py
+++ b/src/digitalmeve/utils.py
@@ -0,0 +1,2 @@
+# src/digitalmeve/utils.py
+from __future__ import annotations
diff --git a/tests/test_version.py b/tests/test_version.py
index 3180fce..bdfd123 100644
--- a/tests/test_version.py
+++ b/tests/test_version.py
@@ -1,3 +1,7 @@
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
