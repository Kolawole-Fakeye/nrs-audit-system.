# 1. Use a lightweight Python 'Kitchen'
FROM python:3.12-slim

# 2. Set the working area
WORKDIR /app

# 3. Copy our code and data into the container
COPY main.py .
COPY nrs_audited_results.csv .

# 4. Install the tools
RUN pip install fastapi uvicorn pandas

# 5. Start the engine
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

