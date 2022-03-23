"""empty message

Revision ID: 98ca22def39d
Revises: 58b77c13c14e
Create Date: 2022-03-22 20:11:41.775514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98ca22def39d'
down_revision = '58b77c13c14e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('property_location_key', 'property', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('property_location_key', 'property', ['location'])
    # ### end Alembic commands ###