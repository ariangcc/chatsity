"""empty message

Revision ID: d947bd076a39
Revises: 4655c045283d
Create Date: 2020-07-20 04:00:36.964550

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd947bd076a39'
down_revision = '4655c045283d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklisted_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('message', 'body',
               existing_type=mysql.VARCHAR(length=1000),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('message', 'body',
               existing_type=mysql.VARCHAR(length=1000),
               nullable=False)
    op.drop_table('blacklisted_token')
    # ### end Alembic commands ###
