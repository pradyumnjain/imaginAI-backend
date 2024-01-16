# imaginAI-backend

## Project setup

### local setup
```bash
## Docker Build
docker build -t imaginai-backend:latest -f Dockerfile.dev .
## Docker Run
docker run -p 4000:5000 -v $(pwd):/app imaginai-backend:latest # docker run
```
### run unit tests

```bash
python -m unittest tests/test_app.py
```


## Resources:
1. https://www.freecodecamp.org/news/how-to-setup-a-ci-cd-pipeline-with-github-actions-and-aws/
2. https://github.com/krishnaik06/bostonhousepricing


## Frequently asked questions
*Question:* why python3.8-slim image?
- The official Python image is based on a lightweight Linux distribution (Debian), and it already includes Python and pip. This means you can use it to set up a Python environment for your Flask application without the need for additional manual installations.

## Todo:
1. create a home api that fetches random images from mongo with pagination and session id.