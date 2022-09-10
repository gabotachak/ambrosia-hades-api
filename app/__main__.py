"""Run flask app."""

from app import create_app

app = create_app(start_orm=True)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4000, debug=True)
