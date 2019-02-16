"""empty message

Revision ID: 0a33dc997691
Revises: 34a5d4d750be
Create Date: 2019-02-16 17:09:33.925102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import table, column, Integer, String, Float

revision = '0a33dc997691'
down_revision = '34a5d4d750be'
branch_labels = None
depends_on = None


def upgrade():
    product_table = table('product',
                          column('id', Integer),
                          column('name', String),
                          column('unit_price', Float),
                          column('multiplier', Integer)
                          )
    op.bulk_insert(
        product_table,
        [
            {'id': 1, 'name': 'Millenium​ ​Falcon', 'unit_price': 550000.00, 'multiplier': 1},
            {'id': 2, 'name': 'X-Wing', 'unit_price': 60000.00, 'multiplier': 2},
            {'id': 3, 'name': 'Super​ ​Star​ ​Destroyer', 'unit_price': 4570000.00, 'multiplier': 1},
            {'id': 4, 'name': 'TIE​ ​Fighter', 'unit_price': 75000.00, 'multiplier': 2},
            {'id': 5, 'name': 'Lightsaber', 'unit_price': 600000, 'multiplier': 5},
            {'id': 6, 'name': 'DLT-19​ ​Heavy​ ​Blaster​ ​Rifle', 'unit_price': 5800.00, 'multiplier': 1},
            {'id': 7, 'name': 'DL-44​ ​Heavy​ ​Blaster​ ​Pistol', 'unit_price': 1500.00, 'multiplier': 10}
        ]
    )


def downgrade():
    pass
