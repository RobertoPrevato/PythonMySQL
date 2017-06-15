# PythonMySQL
Example for using Python with MySQL and SQLAlchemy.

## How to use
1. Download or clone this repository
```bash
# clone repository:
git clone https://github.com/RobertoPrevato/PythonMySQL.git
```

### 2. Create Python virtual environment and restore dependencies

```bash
# Linux:
python3 -m venv env

env/bin/pip install -r requirements.txt
```

```bash
# Windows:
py -3 -m venv env
env\Scripts\pip install -r requirements.txt
```

### 3. Activate Python virtual environment (Optional)

```bash
# Linux:
source env/bin/activate
```

```bash
# Windows:
env\Scripts\activate.bat
```

### 4. Configure the Connection String to your database
Edit the file /app/configuration.py with the connection string to your MySQL instance:

```
mysql+pymysql://USERNAME:PASSWORD@IP_ADDRESS_OF_MYSQL_SERVER:3306/DATABASE_NAME
```

**NB**: the connection string depends on the connector we are using (PyMySQL), and SQLAlchemy itself.

### 5. Create the example database and tables in your instance of MySQL Server
Use provided /db/create_example_db.sql

### 6. Run
Run the example file using the prepared environment, `runexample.py`.

# Database first example
To generate classes from an existing database, use the `sqlacodegen` tool from the virtual environment.

```bash
# Linux:
env/bin/sqlacodegen mysql+pymysql://USERNAME:PASSWORD@IP_ADDRESS_OF_MYSQL_SERVER:3306/DATABASE_NAME > entities.py

# Windows (I didn't test this):
env\Scripts\sqlacodegen mysql+pymysql://USERNAME:PASSWORD@IP_ADDRESS_OF_MYSQL_SERVER:3306/DATABASE_NAME > entities.py
```
