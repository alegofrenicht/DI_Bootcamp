"""empty message

Revision ID: 79e701376a66
Revises: 
Create Date: 2023-04-29 15:52:36.521776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79e701376a66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('crypto_currency',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('symbol', sa.String(length=64), nullable=True),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.Column('first_historical_data', sa.String(length=64), nullable=True),
    sa.Column('last_historical_data', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_crypto_currency',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('crypto_currency_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['crypto_currency_id'], ['crypto_currency.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['app_user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'crypto_currency_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_crypto_currency')
    op.drop_table('crypto_currency')
    op.drop_table('app_user')
    # ### end Alembic commands ###