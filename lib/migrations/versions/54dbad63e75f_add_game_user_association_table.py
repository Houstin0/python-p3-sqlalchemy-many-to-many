"""Add game_user Association Table

Revision ID: 54dbad63e75f
Revises: 51b66218e4c4
Create Date: 2023-09-03 16:31:15.824294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54dbad63e75f'
down_revision = '51b66218e4c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_users',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_game_users_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_game_users_user_id_users')),
    sa.PrimaryKeyConstraint('game_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_users')
    # ### end Alembic commands ###
