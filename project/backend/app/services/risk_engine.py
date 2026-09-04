class RiskEngine:
    @staticmethod
    def calculate_score(headers: dict, authentication_results: str) -> dict:
        """
        Determines a risk score based on evidence found in headers.
        """
        score = 0
        reasons = []

        # Simple example rules
        if not headers.get("from") or not headers.get("return_path"):
            score += 20
            reasons.append("Missing essential routing headers")

        if authentication_results and "fail" in authentication_results.lower():
            score += 50
            reasons.append("Authentication (SPF/DKIM/DMARC) failure detected")
        elif not authentication_results:
            score += 10
            reasons.append("Missing authentication results header")

        # Cap at 100
        score = min(score, 100)

        return {
            "score": score,
            "severity": "high" if score > 70 else "medium" if score > 30 else "low",
            "reasons": reasons
        }
