import os

# try hardcoding creds for now
# "connections": {"default": os.environ.get("DATABASE_URL")},


TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["src.database.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}
