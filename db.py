import mysql2.connector
# Connect to the MySQL database
conn = mysql2.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="btech"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT query
query = "SELECT * FROM customer"
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Process the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
