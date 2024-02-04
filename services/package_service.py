import sqlalchemy.orm
from sqlalchemy import select, func
from typing import List, Optional
from data_models.package import Package
from data_models.release import Release
from data_models import db_session


# hit db to get the count of releases
async def release_count() -> int:
    async with db_session.create_async_session() as session:
        query = select(func.count(Release.id))
        result = await session.execute(query)

        return result.scalar()


# hit the db to get a count of the packages
async def package_count() -> int:
    async with db_session.create_async_session() as session:
        query = select(func.count(Package.id))
        result = await session.execute(query)

        return result.scalar()


# hit db to get the latest packages published
async def latest_packages(limit: int = 5) -> List[Package]:
    async with db_session.create_async_session() as session:
        query = select(Release).options(sqlalchemy.orm.joinedload(Release.package)
                                        ).order_by(Release.created_date.desc()
                                                   ).limit(limit)
        result = await session.execute(query)
        releases = result.scalars()

        # set comprehension to make the returned releases unique, then make it a list for viewmodel
        return list({r.package for r in releases})


async def get_package_by_id(package_name: str) -> Optional[Package]:
    async with db_session.create_async_session() as session:
        query = select(Package).filter(Package.id == package_name)
        result = await session.execute(query)

        return result.scalar_one_or_none()


async def get_latest_release(package_name: str) -> Optional[Release]:
    async with db_session.create_async_session() as session:
        query = select(Release).filter(Release.package_id == package_name).order_by(Release.created_date.desc())
        result = await session.execute(query)
        release = result.scalar()

        return release


