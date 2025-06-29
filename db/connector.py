from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv
import os

# .env読み込み
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def load_sql(filename: str) -> str:
    """SQLファイルを読み込んで文字列として返す"""
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, "sql", filename)
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

def fetch_query_from_file(sql_filename: str, params: dict = None) -> pd.DataFrame:
    """SQLファイルとパラメータを指定してクエリを実行し、DataFrameを返す"""
    query = load_sql(sql_filename)
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), params or {})
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            return df
    except Exception as e:
        print(f"SQL実行エラー（{sql_filename}）:", e)
        return pd.DataFrame()

def get_connection():
    """
    データベース接続を返す
    """
    return engine.connect()
