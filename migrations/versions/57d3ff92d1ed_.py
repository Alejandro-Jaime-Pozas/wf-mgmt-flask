"""empty message

Revision ID: 57d3ff92d1ed
Revises: 
Create Date: 2022-12-12 17:42:09.382931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57d3ff92d1ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_admin_token'), ['token'], unique=True)

    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('job_title', sa.String(length=50), nullable=True),
    sa.Column('personal_email', sa.String(length=100), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('personal_email')
    )
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_employee_token'), ['token'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_employee_token'))

    op.drop_table('employee')
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_admin_token'))

    op.drop_table('admin')
    # ### end Alembic commands ###
