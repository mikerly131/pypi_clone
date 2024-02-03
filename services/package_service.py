import sqlalchemy.orm
from typing import List, Optional
from data_models.package import Package
from data_models.release import Release
from data_models import db_session


# hit db to get the count of releases
def release_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(Release).count()
    finally:
        session.close()


# hit the db to get a count of the packages
def package_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(Package).count()
    finally:
        session.close()


# hit db to get the latest packages published
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

    # set  comprehension to make the returned releases unique, then make it a list for viewmodel
    return list({r.package for r in releases})


def get_package_by_id(package_name: str) -> Optional[Package]:
    session = db_session.create_session()

    try:
        package = session.query(Package).filter(Package.id == package_name).first()
        return package
    finally:
        session.close()


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

