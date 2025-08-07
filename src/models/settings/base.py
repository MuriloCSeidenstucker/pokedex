"""Define a base declarativa para os modelos ORM do SQLAlchemy.

Todas as entidades do projeto devem herdar desta base para que sejam
reconhecidas pelo SQLAlchemy como modelos válidos.
"""

from sqlalchemy.orm import declarative_base

Base = declarative_base()
