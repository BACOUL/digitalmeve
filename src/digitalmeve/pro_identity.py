diff --git a/src/digitalmeve/pro_identity.py b/src/digitalmeve/pro_identity.py
index 0000000..1111111 100644
--- a/src/digitalmeve/pro_identity.py
+++ b/src/digitalmeve/pro_identity.py
@@ -1,999 +1,23 @@
+from __future__ import annotations
+
+from dataclasses import dataclass
+from typing import Optional
+
+
+@dataclass
+class ProIdentity:
+    """
+    Identité professionnelle minimale (extensible).
+    Ajuste les champs si tu veux plus tard (ex.: SIREN, department, etc.)
+    """
+
+    company: str
+    contact: Optional[str] = None
