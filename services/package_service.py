import datetime
from typing import List, Optional
from data_models.package import Package
from data_models.release import Release


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


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name, "This the summary", "www.google.com",
        "MIT", "Sergey Brin", "Full detail description"
    )
    return package


def get_latest_release(package_name: str) -> Optional[Release]:
    return Release("1.2.0", datetime.datetime.now())
