import re
import ipaddress
import hashlib
import magic # Requires python-magic

class IOCService:
    @staticmethod
    def extract_and_normalize(text: str) -> dict:
        # Improved regex
        ips = list(set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)))
        domains = list(set(re.findall(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b', text)))
        return {"ips": ips, "domains": domains}

class AttachmentService:
    @staticmethod
    def analyze(file_path: str) -> dict:
        # Magic byte validation
        with open(file_path, "rb") as f:
            header = f.read(5)
            # Placeholder for magic byte database lookup
            detected_type = "image/png" if header.startswith(b'\x89PNG') else "unknown"

        # Hash
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)

        # Logic for mismatch detection
        return {
            "sha256": sha256.hexdigest(),
            "detected_type": detected_type,
            "suspicious": detected_type == "unknown"
        }
