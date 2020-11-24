"""Change Admin to OrgAdmin

Revision ID: 113a4dfd7067
Revises: 314e77a901e4
Create Date: 2017-09-20 14:26:55.278305

"""
from alembic import op
import sqlalchemy as sa

import lifeloopweb.db.models
import lifeloopweb.db.utils
from sqlalchemy.dialects import mysql

from sqlalchemy.sql import table, column
from sqlalchemy import String, Binary, Integer

# revision identifiers, used by Alembic.
revision = '113a4dfd7067'
down_revision = '314e77a901e4'
branch_labels = None
depends_on = None


org_roles = table(
    'organization_roles',
    column('id', Binary),
    column('priority', Integer),
    column('description', String))


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    conn.execute(org_roles.update().where(org_roles.c.description == 'Administrator').values(description='Organization Administrator'))
    # ### end Alembic commands ###


def downgrade():
    print("Downgrades not supported")
