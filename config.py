from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    # Thay chuỗi dưới đây bằng connection string của Supabase Postgres
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        "postgresql://postgres.aqordtsfzxoayznwtglt:sieupkcool@aws-0-us-east-2.pooler.supabase.com:6543/postgres"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False