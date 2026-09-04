import re

class IOCService:
    IP_PATTERN = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    URL_PATTERN = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    @staticmethod
    def extract_iocs(text: str) -> dict:
        ips = re.findall(IOCService.IP_PATTERN, text)
        urls = re.findall(IOCService.URL_PATTERN, text)
        return {
            "ips": list(set(ips)),
            "urls": list(set(urls))
        }
