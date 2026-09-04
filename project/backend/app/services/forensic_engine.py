    @staticmethod
    def detect_anomalies(headers: dict) -> list:
        anomalies = []

        # From/Reply-To mismatch
        if headers.get("from") and headers.get("reply_to"):
            if headers["from"][0] != headers["reply_to"][0]:
                anomalies.append("FROM_REPLYTO_MISMATCH")

        # Received header inconsistency (if more than 5 hops)
        if headers.get("received") and len(headers["received"]) > 5:
            anomalies.append("EXCESSIVE_RECEIVED_HOPS")

        return anomalies
