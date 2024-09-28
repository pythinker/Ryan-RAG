FROM python:3.9-slim

WORKDIR /app

# Copy the requirements file
COPY requirements.txt app.py ./

# Install other packages from requirements file
RUN pip install -r requirements.txt

EXPOSE 8501

# CMD ["streamlit", "run", "--server.address", "0.0.0.0", "app.py"]
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
