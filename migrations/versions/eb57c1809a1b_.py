# -*- coding: utf-8 -*-
"""empty message

Revision ID: eb57c1809a1b
Revises: 33b67525b8b5
Create Date: 2019-02-15 02:29:18.277849

"""
from alembic import op


# revision identifiers, used by Alembic.
from sqlalchemy import table, column
from sqlalchemy import String, Integer

revision = 'eb57c1809a1b'
down_revision = '33b67525b8b5'
branch_labels = None
depends_on = None


def upgrade():
    user_table = table('user',
                       column('id', Integer),
                       column('name', String)
                       )
    op.bulk_insert(
        user_table,
        [
            {'id': 1, 'name': 'Darth Vader'},
            {'id': 2, 'name': 'Obi-Wan Kenoby'},
            {'id': 3, 'name': 'Luke​ ​Skywalker'},
            {'id': 4, 'name': 'Imperador​ ​Palpatine'},
            {'id': 5, 'name': 'Han​ ​Solo'}
        ]
    )


def downgrade():
    pass
