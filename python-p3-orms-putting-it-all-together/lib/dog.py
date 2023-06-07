import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    
    def __init__(self, name, breed):
        self.id = None
        self.name = name
        self.breed = breed
        
    @classmethod
    def create_table(cls):

        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS dogs(
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT
                
            )
        """)
        CONN.commit()

    def drop_table():
        CURSOR.execute("""
        DROP TABLE IF EXISTS dogs

        """)
        
        CONN.commit()

    def save(self):
        CURSOR.execute("""
        INSERT INTO dogs (name, breed) VALUES (?, ?)
        """, (self.name,self.breed))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls, name, breed):
        new_dog = cls(name, breed)  # Create a new instance of the Dog class
        new_dog.save()  # Save the new dog to the database
        return new_dog

    @classmethod
    def new_from_db(cls, row):
        id, name, breed = row # Unpack the row data into variables
        dog = cls(name, breed)  # Create a new instance of the Dog class
        dog.id = id  # Set the id attribute of the dog
        return dog

       
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM dogs")
        rows = CURSOR.fetchall()
        dogs = []
        for row in rows:
            dog = cls.new_from_db(row)
            dogs.append(dog)
        return dogs
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM dogs")
        rows = CURSOR.fetchall()
        dogs = []
        for row in rows:
            dog = cls.new_from_db(row)  # Create a Dog instance from each row
            dogs.append(dog)
        return dogs
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM dogs WHERE name=?", (name,))
        row = CURSOR.fetchone()
        if row:
            dog = cls.new_from_db(row)  # Create a Dog instance from the fetched row
            return dog
        else:
            return None
        
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM dogs WHERE id=?", (id,))
        row = CURSOR.fetchone()
        if row:
            dog = cls.new_from_db(row)  # Create a Dog instance from the fetched row
            return dog
        else:
            return None



