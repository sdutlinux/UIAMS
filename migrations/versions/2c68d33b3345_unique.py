"""unique

Revision ID: 2c68d33b3345
Revises: 47142faf9121
Create Date: 2015-05-22 11:42:08.810784

"""

# revision identifiers, used by Alembic.
revision = '2c68d33b3345'
down_revision = '47142faf9121'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('major_name', table_name='major')
    op.drop_index('major_name_2', table_name='major')
    op.drop_index('unit_name', table_name='unit')
    op.drop_index('unit_name_2', table_name='unit')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('unit_name_2', 'unit', ['unit_name'], unique=True)
    op.create_index('unit_name', 'unit', ['unit_name'], unique=True)
    op.create_index('major_name_2', 'major', ['major_name'], unique=True)
    op.create_index('major_name', 'major', ['major_name'], unique=True)
    ### end Alembic commands ###
