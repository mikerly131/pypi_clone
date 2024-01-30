from typing import List


def release_count() -> int:
    return 2_435_232

def package_count() -> int:
    return 274_000

def latest_packages(limit: int = 5) -> List:
    return [
        {'id': 'fastapi', 'summary': 'A great python web framework'},
        {'id': 'uvicorn', 'summary': 'An ASGI server'},
        {'id': 'httpx', 'summary': 'Requests for the async world'},
    ][:limit]