import datetime

import sqlalchemy
import sqlalchemy.orm as orm
from data_models.modelbase import SQLAlchemyBase


class Release(SQLAlchemyBase):
    __tablename__ = 'release'

    id: int = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    major_ver: int = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    minor_ver: int = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    build_ver: int = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)

    created_date: datetime.datetime = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    comment: str = sqlalchemy.Column(sqlalchemy.String)
    url: str = sqlalchemy.Column(sqlalchemy.String)
    size: int = sqlalchemy.Column(sqlalchemy.BigInteger)

    # Package relationship, remember the FK is on the database column
    package_id: str = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('package.id'))
    # lazy loaded object through orm, match it to ORM class
    package = orm.relationship('Package')

    @property
    def version_text(self):
        return '{}.{}.{}'.format(self.major_ver, self.minor_ver, self.build_ver)
