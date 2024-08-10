from app import create_app
import os

app = create_app()

def main():
    app.run(host="0.0.0.0", port=5000)
    app.run()


if __name__ == "__main__":
    main()
