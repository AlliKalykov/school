FROM python:3.8.10

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt to the working directory
COPY req.txt /app

# Update pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r req.txt

COPY . /app

# run the command to start runserver
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
