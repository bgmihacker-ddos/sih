import os
import hashlib
import shutil
import uuid
from pathlib import Path
from typing import BinaryIO

# Security: Path traversal protection
# Ensure the UPLOAD_DIR is absolute and immutable outside of this context.
UPLOAD_DIR = Path(os.getenv("STORAGE_PATH", "./storage/evidence")).resolve()
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

class EvidenceService:
    @staticmethod
    def _calculate_hashes(file_stream: BinaryIO) -> tuple[str, str]:
        sha256 = hashlib.sha256()
        md5 = hashlib.md5()

        # Read in chunks to handle memory efficiency
        for chunk in iter(lambda: file_stream.read(4096), b""):
            sha256.update(chunk)
            md5.update(chunk)

        # Reset stream for reuse (or re-open)
        file_stream.seek(0)
        return sha256.hexdigest(), md5.hexdigest()

    @classmethod
    def save_evidence(cls, file_stream: BinaryIO, original_filename: str) -> dict:
        """
        Securely saves evidence file, calculates hashes, and returns metadata.
        """
        # Generate random storage name to prevent collisions and path traversal
        file_uuid = uuid.uuid4()
        extension = Path(original_filename).suffix
        storage_filename = f"{file_uuid}{extension}"
        storage_path = UPLOAD_DIR / storage_filename

        # Hash before save
        sha256, md5 = cls._calculate_hashes(file_stream)

        # Write file
        with open(storage_path, "wb") as buffer:
            shutil.copyfileobj(file_stream, buffer)

        return {
            "evidence_id": str(file_uuid),
            "storage_path": str(storage_path),
            "sha256": sha256,
            "md5": md5,
            "original_filename": original_filename,
            "size": os.path.getsize(storage_path)
        }
