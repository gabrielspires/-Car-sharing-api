# Car Sharing API

A simple car sharing API built with [FastAPI](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/).

## Features

- Search for cars by size and number of doors
- Add, update, and remove cars
- Add trips to cars
- HTML web interface for searching cars
- RESTful API endpoints

## Project Structure

```
src/
    carsharing.py         # Main application entrypoint
    db/
        db.py             # Database setup
    fast_api/
        schemas.py        # Data models and schemas
        cars.json         # Example car data
    routers/
        cars.py           # API routes for cars and trips
        web.py            # Web interface routes
    templates/
        home.html         # Home page template
        search_results.html # Search results template
tests/
    __init__.py           # Test package
```

## Getting Started

### Requirements

- Python 3.13+
- [Poetry](https://python-poetry.org/) (recommended for dependency management)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/carsharing-api.git
    cd carsharing-api
    ```

2. Install dependencies:

    ```sh
    poetry install
    ```

3. Run the application:

    ```sh
    poetry run python src/carsharing.py
    ```

4. Access the API docs at [http://localhost:8000/docs](http://localhost:8000/docs) and the web interface at [http://localhost:8000/](http://localhost:8000/).

## API Endpoints

- `GET /api/cars/` — List cars (filter by size and doors)
- `POST /api/cars/` — Add a new car
- `GET /api/cars/{id}` — Get car by ID
- `PUT /api/cars/{id}` — Update car details
- `DELETE /api/cars/{id}` — Remove a car
- `POST /api/cars/{car_id}/trips` — Add a trip to a car

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).  
See the [LICENSE](LICENSE) file for details.