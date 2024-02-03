"""
Create a base model, understand why
"""
import sqlalchemy.ext.declarative

# Dynamically created base class is needed to create db and tie together the classes
SQLAlchemyBase = sqlalchemy.ext.declarative.declarative_base()
