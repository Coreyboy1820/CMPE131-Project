from app import myapp_obj, models
import secrets
from datetime import date

myapp_obj.debug=True
myapp_obj.config['SECRET_KEY'] = secrets.token_hex(16)

# Fill in default values for database to function correctly
models.database_setup()

if __name__ == "__main__":
    myapp_obj.run(port=5000)
