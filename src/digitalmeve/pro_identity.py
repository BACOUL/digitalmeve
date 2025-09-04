diff --git a/src/digitalmeve/official_identity.py b/src/digitalmeve/official_identity.py
index bc9cc2f..fee2d06 100644
--- a/src/digitalmeve/official_identity.py
+++ b/src/digitalmeve/official_identity.py
@@ -1,9 +1,10 @@
 from __future__ import annotations
 
-from typing import Optional
+from dataclasses import dataclass
+from typing import Optional
 
 
 @dataclass
 class OfficialIdentity:
     """Identité 'officielle'/institutionnelle minimale (extensible)."""
 
     authority: str
     contact: Optional[str] = None
