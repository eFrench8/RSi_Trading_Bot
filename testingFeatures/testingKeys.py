import os

# Access the secret key from environment variables
my_secret_key = os.getenv("MY_SECRET_KEY")

if my_secret_key:
    print(f"The secret key is: {my_secret_key}")
else:
    print("Secret key not found.")