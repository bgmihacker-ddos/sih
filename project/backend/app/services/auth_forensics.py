import re

class AuthForensicService:
    @staticmethod
    def interpret_auth_results(auth_results: list, spf_header: list, dkim_header: list, dmarc_header: list) -> dict:
        """
        Interprets authentication headers, distinguishing provider-reported
        results from local policy.
        """
        analysis = {
            "spf": {"status": "none", "evidence": "none"},
            "dkim": {"status": "none", "evidence": "none"},
            "dmarc": {"status": "none", "evidence": "none"},
            "raw_auth_results": auth_results
        }

        # Interpret SPF Header
        if spf_header:
            analysis["spf"]["evidence"] = spf_header[0]
            if "pass" in spf_header[0].lower():
                analysis["spf"]["status"] = "pass"
            elif "fail" in spf_header[0].lower():
                analysis["spf"]["status"] = "fail"

        # Expand for DKIM and DMARC similarly
        # ... logic implementation ...

        return analysis
