"""User table

Revision ID: 749bc2e5820c
Revises: 
Create Date: 2022-10-01 13:35:04.130640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749bc2e5820c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text(
            "TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text(
            "TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column('first_name', sa.VARCHAR(length=255), nullable=False),
        sa.Column('last_name', sa.VARCHAR(length=255), nullable=False),
        sa.Column('email', sa.VARCHAR(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('user')
