import requests
import os

class ThreatIntelService:
    @staticmethod
    def lookup_ip(ip: str):
        # Placeholder for AbuseIPDB/VirusTotal
        return {"ip": ip, "reputation": "unknown", "provider": "local_mock"}

    @staticmethod
    def lookup_url(url: str):
        return {"url": url, "reputation": "unknown", "provider": "local_mock"}
