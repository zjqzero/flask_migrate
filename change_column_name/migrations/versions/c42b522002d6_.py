"""empty message

Revision ID: c42b522002d6
Revises: a13298656b8d
Create Date: 2016-04-27 23:00:55.372131

"""

# revision identifiers, used by Alembic.
revision = 'c42b522002d6'
down_revision = 'a13298656b8d'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id_name', sa.String(length=50), nullable=True))
    op.drop_column('user', 'name')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', mysql.VARCHAR(length=50), nullable=True))
    op.drop_column('user', 'id_name')
    ### end Alembic commands ###
