# imaginal-backend


why python3.8-slim image?
The official Python image is based on a lightweight Linux distribution (Debian), and it already includes Python and pip. This means you can use it to set up a Python environment for your Flask application without the need for additional manual installations.
## Project setup
```bash
docker run -p 4000:5000 -v $(pwd):/app my-flask-api-dev
```
