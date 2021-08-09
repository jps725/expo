"""created db schema table structure

Revision ID: c36c837facd8
Revises: ffdc0a98111c
Create Date: 2021-08-09 13:31:00.644458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c36c837facd8'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('restaurant_name', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'restaurant_name')
    # ### end Alembic commands ###