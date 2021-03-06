"""empty message

Revision ID: cbfd00853b0f
Revises: a13298656b8d
Create Date: 2016-04-27 23:06:57.963954

"""

# revision identifiers, used by Alembic.
revision = 'cbfd00853b0f'
down_revision = 'a13298656b8d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('detail', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'user', sa.Column('sex', sa.String(length=10), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'user', 'sex')
    op.drop_table('address')
    ### end Alembic commands ###
