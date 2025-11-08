import os
from dotenv import load_dotenv

load_dotenv() # This loads variables from the .env file

print(os.getenv('MY_VAR'))
