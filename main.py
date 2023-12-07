import pymysql
# Establish a connection to the database
db = pymysql.connect(
    host='insurance-database.cdcuzzna0mo5.us-east-2.rds.amazonaws.com',
    user='admin',
    password='12345678',
    port = 3306,
    database="insdb"
)

# Create a cursor object
cursor = db.cursor()

# CUSTOMER: 
# CREATE TABLE customer (
#     ssn VARCHAR(255) PRIMARY KEY,
#     name VARCHAR(255),
#     age INT,
#     gender VARCHAR(255),
#     income FLOAT,
#     health_rating INT,
#     nChildren INT,
#     married BOOLEAN
# );

# Execute a SQL query
def queryExcutor():
    query = '''GRANT SUPER ON insdb.* TO 'admin'@'%';'''
    cursor.execute(query)
    
    query = '''FLUSH PRIVILEGES;'''
    cursor.execute(query)
    
    query = 'SET GLOBAL local_infile=1;'
    cursor.execute(query)
    query = '''
        LOAD DATA LOCAL INFILE './example.csv'
        INTO TABLE customer
        FIELDS TERMINATED BY ','
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;'''
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)

queryExcutor()

cursor.close()
db.close()