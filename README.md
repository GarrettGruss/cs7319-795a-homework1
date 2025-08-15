# CS7319-795A Homework 1

This is a Kuzu GraphRAG application with a Streamlit frontend, running in a containerized environment.

## Features

- **Streamlit Frontend**: Interactive web interface for graph database operations
- **Kuzu Database**: High-performance graph database backend
- **Dockerized**: Complete containerized deployment
- **GraphRAG Ready**: Foundation for retrieval-augmented generation workflows

## Quick Start

### Using Docker Compose (Recommended)

```bash
# Build and run the application
docker-compose up --build

# Access the application
open http://localhost:8501
```

### Manual Setup

```bash
# Install dependencies
uv sync --dev

# Run the Streamlit app
uv run streamlit run app.py
```

## Project Structure

```
├── app.py                 # Streamlit frontend application
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Multi-service deployment
├── pyproject.toml         # Python dependencies
└── .github/workflows/     # CI/CD pipelines
    ├── ruff.yml           # Code linting
    ├── mypy.yml           # Type checking
    ├── pytest.yml         # Testing
    └── pylint.yml         # Code analysis
```

## Development

### Development Commands

```bash
# Run all tests
uv run pytest

# Run linting
uv run ruff check .

# Format code
uv run ruff format .

# Check formatting (without changes)
uv run ruff format --check .

# Run type checking
uv run mypy .
```

### CI/CD

The project includes GitHub Actions workflows for:
- **Ruff**: Code formatting and linting
- **MyPy**: Static type checking
- **PyTest**: Unit testing
- **Pylint**: Code analysis

## Database

The application uses Kuzu, a high-performance graph database optimized for analytics. The database files are persisted in the `kuzu_db/` directory via Docker volume mounting.