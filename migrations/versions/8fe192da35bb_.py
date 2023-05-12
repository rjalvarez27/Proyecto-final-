"""empty message

Revision ID: 8fe192da35bb
Revises: 
Create Date: 2023-05-11 17:09:42.883827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fe192da35bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('licores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('types', sa.String(length=50), nullable=False),
    sa.Column('marca', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('origen', sa.String(length=50), nullable=False),
    sa.Column('litres', sa.Integer(), nullable=False),
    sa.Column('style', sa.String(length=50), nullable=False),
    sa.Column('old', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('document_id', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=260), nullable=False),
    sa.Column('role', sa.Enum('admin', 'buyer', name='role'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('document_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cartitem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('licores_id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['licores_id'], ['licores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cartitem')
    op.drop_table('cart')
    op.drop_table('user')
    op.drop_table('licores')
    # ### end Alembic commands ###
