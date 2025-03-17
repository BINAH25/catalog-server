from app import db, Product, app

with app.app_context():
    sample_products = [
        Product(name="Laptop", description="A high-end laptop", price=1200.00),
        Product(name="Phone", description="Latest smartphone", price=800.00),
    ]
    db.session.add_all(sample_products)
    db.session.commit()
    print("Database populated successfully!")
