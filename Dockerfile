FROM python:3.11.7-slim

RUN mkdir -p /app
RUN mkdir -p /app/src
# Copy the files from the arxiv-hunter/src directory to the /app directory inside the image
COPY . /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 9000

ENV PYTHONPATH=/app

# Run the main.py file from the app subdirectory
# CMD [ "src.app.main:app" ]
CMD ["uvicorn", "src.app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "9000"]

# http http://127.0.0.1:8000/
# uvicorn src.app.main:app