### 1. Install dependencies
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

pip install -r requirements.txt

### 2. Create the database
```
In PostgreSQL:
```

CREATE DATABASE mydb;
CREATE USER username WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE mydb TO username;
```

3. Configure the database connection
```
In src/app/database.py:

DATABASE_URL = "postgresql+asyncpg://username: password@localhost:5432/mydb"
```
4. Run the application
```
uvicorn main:app --reload
