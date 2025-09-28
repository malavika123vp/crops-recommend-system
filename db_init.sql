PRAGMA foreign_keys = ON;

CREATE TABLE soils(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  notes TEXT,
  image TEXT
);

CREATE TABLE crops(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  soil_preference TEXT,
  short_note TEXT,
  fertilizer TEXT,
  image TEXT
);

CREATE TABLE crop_soil(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  crop_id INTEGER NOT NULL,
  soil_id INTEGER NOT NULL,
  FOREIGN KEY(crop_id) REFERENCES crops(id),
  FOREIGN KEY(soil_id) REFERENCES soils(id)
);

-- Sample soils
INSERT INTO soils(name,notes,image) VALUES
('Loamy','Well-drained, ideal for many crops','/static/images/soil_loamy.jpg'),
('Sandy','Drains quickly, good for root crops','/static/images/soil_sandy.jpg'),
('Clay','High water retention, needs organic matter','/static/images/soil_clay.jpg');

-- Sample crops
INSERT INTO crops(name,soil_preference,short_note,fertilizer_image) VALUES
('Tomato','Loamy','Warm-season crop; needs watering','N:80 P:50 K:70','/static/images/tomato.jpg'),
('Carrot','Sandy','Root crop; loose soil preferred','N:40 P:50 K:60','/static/images/carrot.jpg'),
('Rice','Clay','Flooded fields; needs plenty of water','N:100 P:50 K:50','/static/images/rice.jpg');

-- Links
INSERT INTO crop_soil(crop_id,soil_id) VALUES
((SELECT id FROM crops WHERE name='Tomato'),(SELECT id FROM soils WHERE name='Loamy')),
((SELECT id FROM crops WHERE name='Carrot'),(SELECT id FROM soils WHERE name='Sandy')),
((SELECT id FROM crops WHERE name='Rice'),(SELECT id FROM soils WHERE name='Clay'));