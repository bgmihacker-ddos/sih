import email
from email import policy
import re
from bs4 import BeautifulSoup

class RobustForensicEngine:
    @staticmethod
    def parse_eml_deep(file_path: str):
        with open(file_path, "rb") as f:
            msg = email.message_from_binary_file(f, policy=policy.default)

        analysis = {
            "headers": {},
            "parts": [],
            "iocs": {"ips": [], "urls": []}
        }

        # Header Parsing
        for header in msg.keys():
            analysis["headers"][header.lower()] = msg.get(header)

        # Recursive Part Extraction
        for part in msg.walk():
            content_type = part.get_content_type()
            payload = part.get_payload(decode=True)

            part_data = {
                "content_type": content_type,
                "filename": part.get_filename(),
            }

            # HTML specific analysis
            if content_type == "text/html" and payload:
                soup = BeautifulSoup(payload, "html.parser")
                part_data["links"] = [a.get("href") for a in soup.find_all("a", href=True)]
                analysis["iocs"]["urls"].extend(part_data["links"])

            analysis["parts"].append(part_data)

        return analysis
