import sqlalchemy.orm
from typing import List, Optional
from data_models.package import Package
from data_models.release import Release
from data_models import db_session


def release_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(Release).count()
    finally:
        session.close()


def package_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(Package).count()
    finally:
        session.close()


def latest_packages(limit: int = 5) -> List[Package]:
    session = db_session.create_session()

    try:
        releases = (
            session.query(Release)
            .options(sqlalchemy.orm.joinedload(Release.package))
            .order_by(Release.created_date.desc())
            .limit(limit)
            .all()
        )
    finally:
        session.close()

    return list({r.package for r in releases})


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name, "This the summary", "www.google.com",
        "MIT", "Sergey Brin", "Full detail description"
    )
    return package


def get_latest_release(package_name: str) -> Optional[Release]:
    session = db_session.create_session()

    try:
        release = (
            session.query(Release)
            .filter(Release.package_id == package_name)
            .order_by(Release.created_date.desc())
            .first()
        )

        return release
    finally:
        session.close()

