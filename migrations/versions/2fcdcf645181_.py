"""empty message

Revision ID: 2fcdcf645181
Revises: f8a457929666
Create Date: 2017-04-15 19:10:47.246728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fcdcf645181'
down_revision = 'f8a457929666'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('sqlite_sequence')
    # op.create_unique_constraint(None, 'client_status', ['text_color'])
    # op.create_unique_constraint(None, 'client_status', ['color'])
    # op.create_unique_constraint(None, 'users', ['username'])
    op.add_column('clients', sa.Column('created_timestamp', sa.String(), nullable=True))
    op.add_column('clients', sa.Column('updated_timestamp', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('clients', 'updated_timestamp')
    op.drop_column('clients', 'created_timestamp')
    op.drop_constraint(None, 'client_status', type_='unique')
    op.drop_constraint(None, 'client_status', type_='unique')
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    # ### end Alembic commands ###
