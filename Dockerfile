# Base image
FROM python:3.9


RUN pip install Flask-PyMongo==2.3.0


# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Command to run the application
CMD ["python", "app.py"]


