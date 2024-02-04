FROM python:3.11.7-slim

RUN mkdir -p /app
# Copy the files from the src/app directory to the /app directory inside the image
COPY src/app /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
# Run the main.py file from the app directory
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]
