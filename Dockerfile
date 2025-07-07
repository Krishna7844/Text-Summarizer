# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements if available, else only app.py
COPY ./requirements.txt ./
COPY ./app.py ./
COPY ./templates/ /app/templates/

# Install dependencies
RUN pip install flask google-genai flask-cors|| true

# Expose Flask default port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]