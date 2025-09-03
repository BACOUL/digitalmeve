diff --git a/tests/test_version.py b/tests/test_version.py
index 773c6d3..c6f0c9a 100644
--- a/tests/test_version.py
+++ b/tests/test_version.py
@@ -1,2 +1,8 @@
-def test_version():
-    import digitalmeve
+"""
+Tests de version du package digitalmeve
+"""
+
+
+def test_version():
+    import digitalmeve
+
+    # Vérifie que le package expose bien un attribut __version__
+    assert hasattr(digitalmeve, "__version__")
+
+    # Vérifie que la version est bien celle attendue
+    assert digitalmeve.__version__ == "1.7.1-dev"
