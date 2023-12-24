from flask import Blueprint

orderRoutes = Blueprint('orders', __name__)
productRoutes = Blueprint('products', __name__)

from . import orderController
from . import productController