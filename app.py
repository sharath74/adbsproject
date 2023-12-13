from bottle import Bottle, run, template, request, redirect
import sqlite3

# Initialize the Bottle app
app = Bottle()

# SQLite database connection
db_path = 'movie_actor.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

# Routes
@app.route('/')
def index():
    # Fetch and display movies and actors
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch movies
    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()

    # Fetch actors
    cursor.execute('SELECT * FROM actors')
    actors = cursor.fetchall()

    # Close the connection
    conn.close()

    return template('index', movies=movies, actors=actors)

@app.route('/add', method='GET')
def add_form():
    return template('add')

@app.route('/add', method='POST')
def add():
    # Add a new movie or actor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    entity_type = request.forms.get('entity_type')
    name = request.forms.get('name')

    if entity_type == 'movie':
        cursor.execute('INSERT INTO movies (name) VALUES (?)', (name,))
    elif entity_type == 'actor':
        cursor.execute('INSERT INTO actors (name) VALUES (?)', (name,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    redirect('/')

@app.route('/edit/<entity_type>/<entity_id>', method='GET')
def edit_form(entity_type, entity_id):
    # Display the edit form for a movie or actor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if entity_type == 'movie':
        cursor.execute('SELECT * FROM movies WHERE id = ?', (entity_id,))
    elif entity_type == 'actor':
        cursor.execute('SELECT * FROM actors WHERE id = ?', (entity_id,))

    entity = cursor.fetchone()

    # Close the connection
    conn.close()

    return template('edit', entity_type=entity_type, entity=entity)

@app.route('/edit/<entity_type>/<entity_id>', method='POST')
def edit(entity_type, entity_id):
    # Update a movie or actor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    new_name = request.forms.get('name')

    if entity_type == 'movie':
        cursor.execute('UPDATE movies SET name = ? WHERE id = ?', (new_name, entity_id))
    elif entity_type == 'actor':
        cursor.execute('UPDATE actors SET name = ? WHERE id = ?', (new_name, entity_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    redirect('/')

@app.route('/delete/<entity_type>/<entity_id>')
def delete(entity_type, entity_id):
    # Delete a movie or actor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if entity_type == 'movie':
        cursor.execute('DELETE FROM movies WHERE id = ?', (entity_id,))
    elif entity_type == 'actor':
        cursor.execute('DELETE FROM actors WHERE id = ?', (entity_id,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    redirect('/')

# Run the application
run(app, host='localhost', port=8080, debug=True)
