from app import create_app
import os

app = create_app()

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

    app.run()

if __name__ == "__main__":
    main()
