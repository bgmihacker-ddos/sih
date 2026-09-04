import re
import ipaddress

class RouteForensicService:
    @staticmethod
    def is_private_ip(ip_str: str) -> bool:
        try:
            ip = ipaddress.ip_address(ip_str)
            return ip.is_private
        except ValueError:
            return False

    @staticmethod
    def reconstruct_route(received_headers: list) -> list:
        hops = []
        if not received_headers:
            return hops

        for i, raw_header in enumerate(received_headers):
            # Complex regex for Received-chain
            from_match = re.search(r'from\s+([^\s]+)', raw_header, re.I)
            by_match = re.search(r'by\s+([^\s]+)', raw_header, re.I)

            # Simple IP extraction
            ip_match = re.search(r'\[([\d\.]+)\]', raw_header)
            ip = ip_match.group(1) if ip_match else None

            hop = {
                "hop_number": i + 1,
                "from": from_match.group(1) if from_match else None,
                "by": by_match.group(1) if by_match else None,
                "ip": ip,
                "is_private": RouteForensicService.is_private_ip(ip) if ip else None,
                "anomaly": False
            }

            # Detect anomaly: Transition from private to public?
            if i > 0 and hop["is_private"] == False and hops[i-1]["is_private"] == True:
                hop["anomaly"] = True # Potential external entry point

            hops.append(hop)
        return hops
