"""initial

Revision ID: 6cea7b5305d5
Revises: 
Create Date: 2022-04-05 21:08:38.368087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cea7b5305d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bd_stat',
    sa.Column('bd_user_id', sa.BigInteger(), nullable=False),
    sa.Column('bd_user_name', sa.String(length=100), nullable=False),
    sa.Column('bd_year', sa.Integer(), nullable=False),
    sa.Column('congo_id', sa.BigInteger(), nullable=False),
    sa.Column('congo_name', sa.String(length=100), nullable=False),
    sa.Column('congratzed_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('bd_user_id', 'bd_year', 'congo_id', name='bdstat_pk')
    )
    op.create_table('botinfo',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('version', sa.String(length=5), nullable=False),
    sa.Column('languages', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('released_on', sa.Date(), nullable=True),
    sa.Column('created_on', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('holidays',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('holiday_date', sa.Date(), nullable=False),
    sa.Column('holiday_name', sa.String(length=255), nullable=False),
    sa.Column('holiday_code', sa.String(length=128), nullable=False),
    sa.Column('hide_link', sa.String(), nullable=True),
    sa.Column('where', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'holiday_code', name='holidays_pk')
    )
    op.create_table('users',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('user_bd', sa.Date(), nullable=True),
    sa.Column('sex', sa.String(length=1), nullable=True),
    sa.Column('lang_code', sa.String(length=2), nullable=True),
    sa.Column('rating', sa.SmallInteger(), nullable=True),
    sa.Column('preferred_date_order', sa.String(), nullable=True),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_user_bd'), 'users', ['user_bd'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_bd'), table_name='users')
    op.drop_table('users')
    op.drop_table('holidays')
    op.drop_table('botinfo')
    op.drop_table('bd_stat')
    # ### end Alembic commands ###
