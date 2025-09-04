diff --git a/src/digitalmeve/pro_identity.py b/src/digitalmeve/pro_identity.py
index f719a50..d41d8cd 100644
--- a/src/digitalmeve/pro_identity.py
+++ b/src/digitalmeve/pro_identity.py
@@ -1,15 +1,15 @@
-from __future__ import annotations
-
-from dataclasses import dataclass
-from typing import Optional
-
-
-@dataclass
-class ProIdentity:
-    """Identité professionnelle minimale (extensible)."""
-
-    company: str
-    contact: Optional[str] = None
+from __future__ import annotations
+
+from dataclasses import dataclass
+from typing import Optional
+
+
+@dataclass
+class ProIdentity:
+    """Identité professionnelle minimale (extensible)."""
+
+    company: str
+    contact: Optional[str] = None
diff --git a/src/digitalmeve/official_identity.py b/src/digitalmeve/official_identity.py
index bc9cc2f..d41d8cd 100644
--- a/src/digitalmeve/official_identity.py
+++ b/src/digitalmeve/official_identity.py
@@ -1,15 +1,15 @@
-from __future__ import annotations
-
-from dataclasses import dataclass
-from typing import Optional
-
-
-@dataclass
-class OfficialIdentity:
-    """Identité 'officielle'/institutionnelle minimale (extensible)."""
-
-    authority: str
-    contact: Optional[str] = None
+from __future__ import annotations
+
+from dataclasses import dataclass
+from typing import Optional
+
+
+@dataclass
+class OfficialIdentity:
+    """Identité 'officielle'/institutionnelle minimale (extensible)."""
+
+    authority: str
+    contact: Optional[str] = None
