"""Application entry point."""
from eform_app import create_app

my_app = create_app()

if __name__ == "__main__":
    my_app.run(host='0.0.0.0', debug=True)
