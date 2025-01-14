from dashboard import db
from dashboard.models import Products
from faker import Faker
import random
import sys

def create_faker_products(n):
    """Generate fake product info"""
    faker = Faker()
    for i in range(n):
        product = Products(name=faker.name(),
                           description=faker.text(),
                           unit_price=random.uniform(100, 1000),
                           quantity_ordered=random.randint(0, 1000))
        db.session.add(product)
    db.session.commit()


if __name__ == '__main__':
    if len(sys.argv) <=1:
        print('Pass the number of products you want to create as an argument')
        sys.exit(1)
    create_faker_products(int(sys.argv[1]))
