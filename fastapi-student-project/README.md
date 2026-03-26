## Project Structure

- `domain/`: Domain entities (Student)
- `repositories/`: Repository interfaces and implementations (In-memory)
- `services/`: Application services (StudentService)
- `entrypoints/`: API endpoints (FastAPI routers)

## Setup

1. Create a virtual environment:
   ```
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`

3. Install dependencies using uv (recommended for speed):
   ```
   uv pip install -r requirements.txt
   ```
   Or using pip:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Run the FastAPI server:
```
python main.py
```

The API will be available at http://localhost:8000

## Endpoints

- `GET /students`: Get all students
- `GET /students/{id}`: Get student by ID
- `POST /students`: Create a new student (send JSON with name and email)

## Example Usage

Create a student:
```
curl -X POST "http://localhost:8000/students" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
```

Get all students:
```
curl http://localhost:8000/students
```