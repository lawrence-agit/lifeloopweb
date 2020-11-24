"""Drop Group Notes

Revision ID: caa2785a330b
Revises: 53adcad32e45
Create Date: 2017-11-07 22:16:58.535262

"""
from alembic import op
import sqlalchemy as sa

import lifeloopweb.db.models
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'caa2785a330b'
down_revision = '53adcad32e45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group_notes')
    # ### end Alembic commands ###


def downgrade():
    print("Downgrades not supported")