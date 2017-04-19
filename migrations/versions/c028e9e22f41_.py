"""empty message

Revision ID: c028e9e22f41
Revises: 2fcdcf645181
Create Date: 2017-04-18 18:08:52.136494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c028e9e22f41'
down_revision = '2fcdcf645181'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('timestamp', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # op.drop_table('sqlite_sequence')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'client_status', type_='unique')
    op.drop_constraint(None, 'client_status', type_='unique')
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.drop_table('client_history')
    # ### end Alembic commands ###
