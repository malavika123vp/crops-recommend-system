import sqlite3

def init_db():
    conn = sqlite3.connect("crops.db")
    cursor = conn.cursor()

    # Create crops table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        soil TEXT NOT NULL,
        fertilizer TEXT NOT NULL,
        image TEXT
    )
    """)

    # Sample data insert
    crops_data = [
    ("Tomato", "Loamy", "Nitrogen, Phosphorus, Potassium", "tomato.jpeg"),
    ("Carrot", "Sandy", "Compost, Potash", "carrot.jpeg"),
    ("Rice", "Clay", "Urea, DAP", "rice.jpeg"),
    ("Wheat", "Sandy Loam", "NPK, Farmyard Manure", "wheat.jpeg"),
    ("Maize", "Sandy Loam", "Urea, Potash", "maize.jpeg"),
    ("Sugarcane", "Clay Loam", "Nitrogen, Phosphorus", "sugarcane.jpeg"),
    ("Cotton", "Black Soil", "Potassium Sulphate, Superphosphate", "cotton.jpeg"),
    ("Groundnut", "Sandy Loam", "Gypsum, Urea", "groundnut.jpeg"),
    ("Onion", "Loamy", "Compost, Potash", "onion.jpeg"),
    ("Potato", "Sandy Loam", "Ammonium Sulphate, DAP", "potato.jpeg"),
    ("Chilli", "Sandy Loam", "Nitrogen, Phosphorus", "chilli.jpeg"),
    ("Brinjal", "Loamy", "NPK Mixture", "brinjal.jpeg"),
    ("Okra", "Sandy Loam", "Compost, Urea", "okra.jpeg"),
    ("Cabbage", "Loamy", "Compost, DAP", "cabbage.jpeg"),
    ("Cauliflower", "Loamy", "Superphosphate, Potash", "cauliflower.jpeg"),
    ("Mustard", "Clay Loam", "Urea, Potash", "mustard.jpeg"),
    ("Pea", "Sandy Loam", "Phosphate Fertilizer, Compost", "pea.jpeg"),
    ("Soybean", "Black Soil", "Superphosphate, Potash", "soybean.jpeg"),
    ("Barley", "Sandy Loam", "NPK, Urea", "barley.jpeg"),
    ("Sunflower", "Loamy", "Nitrogen, Potash", "sunflower.jpeg"),
    ("Banana", "Alluvial Soil", "Organic Manure, Potash", "banana.jpeg"),
    ("Mango", "Laterite Soil", "Farmyard Manure, Urea", "mango.jpeg"),
    ("Papaya", "Loamy", "Compost, Potash", "papaya.jpeg"),
    ("Pineapple", "Sandy Loam", "Superphosphate, Compost", "pineapple.jpeg"),
    ("Coconut", "Sandy Soil", "Farmyard Manure, Urea", "coconut.jpeg"),
    ("Tea", "Laterite Soil", "Ammonium Sulphate, Potash", "tea.jpeg"),
    ("Coffee", "Red Soil", "Urea, Superphosphate", "coffee.jpeg"),
    ("Pepper", "Loamy", "Compost, NPK", "pepper.jpeg"),
    ("Turmeric", "Sandy Loam", "Farmyard Manure, Potash", "turmeric.jpeg"),
    ("Ginger", "Loamy", "Compost, Phosphate", "ginger.jpeg")
]

    cursor.executemany("INSERT INTO crops (name, soil, fertilizer, image) VALUES (?, ?, ?, ?)", crops_data)

    conn.commit()
    conn.close()
    print("✅ Database created successfully (crops.db)!")

if __name__ == "__main__":
    init_db()