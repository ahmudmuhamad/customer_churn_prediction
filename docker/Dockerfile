FROM python:3.12-slim

# Install uv (ultra fast Python package manager)
RUN pip install uv

# Set workdir
WORKDIR /app

# Copy requirements and source code
COPY requirements.txt ./
COPY src ./src

# Install dependencies with uv
RUN uv pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Start FastAPI app with uvicorn
CMD ["uvicorn", "churn.api.main:app", "--host", "0.0.0.0", "--port", "8000"]