# Using SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///catalog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()  # FIXED: Corrected query
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": p.price
    } for p in products])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensures the database and tables are created
    app.run(host="0.0.0.0", port=5000)
