# Add SSRF protection if enabling URL fetching
# Implement sanitization
from fastapi import Request
import logging

async def security_middleware(request: Request, call_next):
    # Log incoming request
    logging.info(f"Accessing {request.url.path}")
    response = await call_next(request)
    # Add Security Headers
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response
