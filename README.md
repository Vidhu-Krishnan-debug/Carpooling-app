# CarpoolHub - Carpooling Web Application

A modern web application that connects drivers with passengers for shared rides. Built with Flask, SQLAlchemy, and Bootstrap.

## Features

- User registration and authentication
- Offer rides as a driver
- Search and book available rides
- Real-time seat availability
- User dashboard
- Responsive design

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/carpool_app.git
cd carpool_app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
carpool_app/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── static/            # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── templates/         # HTML templates
    ├── index.html
    └── ...
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
