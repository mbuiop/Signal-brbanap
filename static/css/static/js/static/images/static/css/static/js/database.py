import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('ads.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS ads
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT NOT NULL,
                  price TEXT NOT NULL,
                  contact TEXT NOT NULL,
                  image_path TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    conn.commit()
    conn.close()

def get_db():
    return sqlite3.connect('ads.db')

def save_ad(title, description, price, contact, image_path):
    conn = get_db()
    c = conn.cursor()
    
    c.execute("INSERT INTO ads (title, description, price, contact, image_path) VALUES (?, ?, ?, ?, ?)",
              (title, description, price, contact, image_path))
    
    conn.commit()
    conn.close()

def get_all_ads():
    conn = get_db()
    c = conn.cursor()
    
    c.execute("SELECT * FROM ads ORDER BY created_at DESC")
    ads = c.fetchall()
    
    conn.close()
    return ads
