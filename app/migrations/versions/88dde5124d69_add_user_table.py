"""Add User table

Revision ID: 88dde5124d69
Revises: 
Create Date: 2023-03-11 10:08:50.590321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88dde5124d69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('email', sa.VARCHAR(), nullable=True),
                    sa.Column('password', sa.VARCHAR(), nullable=False),
                    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
                    sa.Column('created_at', sa.VARCHAR(), nullable=True),
                    sa.Column('last_updated_at', sa.VARCHAR(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
