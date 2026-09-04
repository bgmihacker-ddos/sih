import pytest
from app.services.forensic_engine import ForensicEngine
import os

# Create a dummy EML for testing
def test_parse_eml_header():
    # Setup
    eml_content = b"From: test@example.com\nSubject: Test Email\n\nBody content"
    with open("test.eml", "wb") as f:
        f.write(eml_content)

    # Action
    msg = ForensicEngine.parse_eml("test.eml")
    headers = ForensicEngine.extract_headers(msg)

    # Assert
    assert headers["from"] == "test@example.com"
    assert headers["subject"] == "Test Email"

    # Cleanup
    os.remove("test.eml")
