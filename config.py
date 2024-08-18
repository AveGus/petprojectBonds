from dotenv import load_dotenv
import os

load_dotenv()

#our database
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

# secret phrase for jwt
SECRET = os.getenv("SECRET")

#SMTP (Send email)
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

#db for testing pytest
DB_HOST_TEST = os.getenv("DB_HOST_TEST")
DB_USER_TEST = os.getenv("DB_USER_TEST")
DB_PASS_TEST = os.getenv("DB_PASS_TEST")
DB_NAME_TEST = os.getenv("DB_NAME_TEST")
DB_PORT_TEST = os.getenv("DB_PORT_TEST")


