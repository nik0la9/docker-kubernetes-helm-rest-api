# Use official Python image as base
FROM python:3.9-slim

# Install Flask
RUN pip install flask

# Copy application into container
COPY app.py /app/app.py
WORKDIR /app

# Run the application
CMD ["python", "app.py"]