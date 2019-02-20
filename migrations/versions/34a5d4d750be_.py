"""empty message

Revision ID: 34a5d4d750be
Revises: 23bc5b158d77
Create Date: 2019-02-16 17:09:30.332722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import table, column, Integer, String

revision = '34a5d4d750be'
down_revision = '23bc5b158d77'
branch_labels = None
depends_on = None


def upgrade():
    user_table = table('user',
                       column('id', Integer),
                       column('name', String),
                       )
    op.bulk_insert(
        user_table,
        [
            {'id': 1, 'name': 'Darth​ ​Vader'},
            {'id': 2, 'name': 'Obi-Wan​ ​Kenobi'},
            {'id': 3, 'name': 'Luke​ ​Skywalker'},
            {'id': 4, 'name': 'Imperador​ ​Palpatine'},
            {'id': 5, 'name': 'Han​ ​Solo'},
        ]
    )


def downgrade():
    pass
