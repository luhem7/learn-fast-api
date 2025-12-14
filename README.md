# FastAPI Learning Repository

A comprehensive learning repository for mastering FastAPI, the modern, fast (high-performance) web framework for building APIs with Python 3.13 based on standard Python type hints.

## 🎯 Learning Objectives

By the end of this learning journey, you'll understand:
- FastAPI fundamentals and core concepts
- Creating RESTful APIs with proper HTTP methods
- Request/response handling and validation
- Database integration and ORM usage
- Authentication and authorization
- API documentation with automatic OpenAPI/Swagger
- Testing FastAPI applications
- Deployment strategies

## 🛠️ Tech Stack

- **Python**: 3.13
- **FastAPI**: Modern, fast web framework for APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Pydantic**: Data validation using Python type annotations
- **SQLAlchemy**: SQL toolkit and ORM (for database examples)
- **pytest**: Testing framework

## 📋 Prerequisites

- Basic Python knowledge (functions, classes, decorators)
- Understanding of HTTP methods (GET, POST, PUT, DELETE)
- Basic understanding of REST APIs
- Familiarity with command line/terminal

## 🚀 Getting Started

### 1. Environment Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd learn-fast-api

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/Mac:
source .venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Your First FastAPI App

```bash
# Start the development server
uvicorn main:app --reload

# Visit the interactive API docs
# http://localhost:8000/docs (Swagger UI)
# http://localhost:8000/redoc (ReDoc)
```