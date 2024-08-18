from sqlalchemy import Table, Column, Integer, String, TIMESTAMP
from database import metadata1

operation = Table(
    'operation',
    metadata1,
    Column('id', Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=False),
    Column("date", TIMESTAMP),
    Column("type", String),
)
