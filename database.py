import sqlite3

# Connect to the database
conn = sqlite3.connect("hostel_chatbot.db")
cursor = conn.cursor()

# Create the FAQ table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS FAQ (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT UNIQUE,
    answer TEXT
)
''')

# Sample FAQs (cleaned, expanded, and deduplicated)
sample_data = [
    # ✅ Check-in
    ("What time is check-in?", "Check-in starts at 2:00 PM."),
    ("When can I check in?", "Check-in starts at 2:00 PM."),
    ("What are the check-in timings?", "Check-in starts at 2:00 PM."),
    ("What time do I check in?", "Check-in starts at 2:00 PM."),

    # ✅ Check-out
    ("What time is check-out?", "Check-out is at 12:00 PM."),
    ("When is check-out?", "Check-out is at 12:00 PM."),
    ("What are the check-out timings?", "Check-out is at 12:00 PM."),
    ("What time do I check out?", "Check-out is at 12:00 PM."),
    ("Can I check out late?", "Late check-out is available upon request, subject to availability."),
    ("Is there a late check-out?", "Late check-out is available upon request, subject to availability."),

    # ✅ Wi-Fi
    ("Is Wi-Fi available?", "Yes, free Wi-Fi is available in all rooms."),
    ("Do you have Wi-Fi?", "Yes, free Wi-Fi is available in all rooms."),

    # ✅ Parking
    ("Do you have parking?", "Yes, we offer free parking for guests."),
    ("Is parking available?", "Yes, we offer free parking for guests."),

    # ✅ Pets
    ("Are pets allowed?", "Pets are not allowed in the hotel."),
    ("Can I bring pets?", "Pets are not allowed in the hotel."),

    # ✅ Room Service
    ("Is room service available?", "Yes, room service is available 24/7."),
    ("Do you offer room service?", "Yes, room service is available 24/7."),

    # ✅ Breakfast
    ("Is breakfast included?", "It depends on your booking package."),
    ("What time is breakfast?", "Breakfast is served from 7:00 AM to 9:00 AM."),

    # ✅ Breakfast Menu
    (
    "What do you serve for breakfast?", "Our breakfast includes Halwa Puri, Nihari, Omelettes, Toast, and Tea/Coffee."),
    ("What is included in breakfast?", "We offer Halwa Puri, Nihari, Omelettes, Toast, and Tea/Coffee."),
    ("Tell me the breakfast dishes", "Halwa Puri, Nihari, Omelettes, Toast, and Tea/Coffee are included in breakfast."),

    # ✅ Lunch Menu
    ("What do you serve for lunch?",
     "Our lunch includes Chicken Biryani, Grilled Fish, Vegetable Pulao, and Mixed Salad."),
    ("What is included in lunch?",
     "We offer Chicken Biryani, Grilled Fish, Vegetable Pulao, and Mixed Salad for lunch."),
    ("Tell me the lunch dishes",
     "Chicken Biryani, Grilled Fish, Vegetable Pulao, and Mixed Salad are included in lunch."),

    # ✅ Dinner Menu
    ("What do you serve for dinner?",
     "Dinner options include Mutton Karahi, Chapli Kebabs, BBQ Platter, and a variety of desserts."),
    ("What is included in dinner?", "We serve Mutton Karahi, Chapli Kebabs, BBQ Platter, and desserts for dinner."),
    ("Tell me the dinner dishes", "Mutton Karahi, Chapli Kebabs, BBQ Platter, and desserts are included in dinner."),
    # ✅ Swimming Pool
    ("Do you offer a swimming pool?", "Yes, our swimming pool is open from 8:00 AM to 10:00 PM."),
    ("Is there a swimming pool?", "Yes, our swimming pool is open from 8:00 AM to 10:00 PM."),

    # ✅ Gym
    ("Do you have a fitness center?", "Yes, our fitness center is open 24/7."),
    ("Is there a gym?", "Yes, our fitness center is open 24/7."),

    # ✅ Laundry
    ("Do you offer laundry service?", "Yes, we offer laundry and dry-cleaning services."),
    ("Can I get my clothes washed?", "Yes, we offer laundry and dry-cleaning services."),

    # ✅ Extra Beds
    ("Do you provide extra beds?", "Yes, extra beds are available on request with additional charges."),
    ("Can I get an extra bed?", "Yes, extra beds are available on request with additional charges."),

    # ✅ Conference Rooms
    ("Do you have conference rooms?", "Yes, we have fully equipped conference and meeting rooms."),
    ("Can I book a conference room?", "Yes, we have fully equipped conference and meeting rooms."),

    # ✅ Booking / Cancellation
    ("Can I cancel my booking?", "Yes, cancellations are allowed based on the booking policy."),
    ("Can I modify my booking?", "Yes, modifications are allowed based on availability and booking terms."),

    # ✅ Luggage
    ("Can I store my luggage?", "Yes, we offer luggage storage at no extra cost."),
    ("Where can I leave my luggage?", "Yes, we offer luggage storage at no extra cost."),

    # ✅ Contact / Location (new)
    ("What is your contact number?", "You can call us at +92 324 5508254."),
    ("What is your phone number?", "Our contact number is +92 324 5508254."),
    ("Where is the hotel located?", "The Velvet Orchid Hotel is located at House No. 1, Danna, Thandiani Road, Abbottabad, Khyber Pakhtunkhwa, Pakistan."),
    ("What is your exact address?", "House No. 1, Danna, Thandiani Road, Abbottabad, Khyber Pakhtunkhwa, Pakistan."),
    ("Who is the owner of the hotel?", "The hotel is proudly owned by Malik Saifullah."),

    # ✅ Greetings
    ("Hello", "Hello! How can I assist you today?"),
    ("Hi", "Hi there! How can I help you today?"),
    ("Good morning", "Good morning! How can I assist you today?"),
    ("Good afternoon", "Good afternoon! How can I assist you today?"),
    ("Good evening", "Good evening! How can I assist you today?")
]

# Insert data using INSERT OR IGNORE to avoid duplicates
cursor.executemany('INSERT OR IGNORE INTO FAQ (question, answer) VALUES (?, ?)', sample_data)

# Commit and close
conn.commit()
conn.close()

print("Database and FAQ table created/updated successfully!")
