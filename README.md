# 🚗 Car Rental Portal

A comprehensive Django-based car rental management system with modern features including REST API, advanced search, email notifications, and robust security.

## ✨ Features

### 🔐 Authentication & Security
- Secure password hashing and validation
- Session management with timeout
- CSRF and XSS protection
- Input validation and sanitization
- Role-based access control (Agent/Customer)

### 🚙 Car Management
- Add, view, and manage car inventory
- Car details with images
- Advanced search and filtering
- Availability checking
- Rent calculation

### 📅 Booking System
- Car booking with date validation
- Booking status tracking
- Customer booking history
- Trip management
- Driver assignment

### 📧 Notification System
- Email notifications for bookings
- Booking confirmations and cancellations
- Complaint acknowledgments
- Welcome emails for new users

### 🔍 Advanced Features
- REST API for mobile/frontend integration
- Search and filtering utilities
- Booking analytics and reporting
- Complaint management system
- Dashboard with key metrics

## 🛠️ Technology Stack

- **Backend**: Django 3.2+
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Authentication**: Django Auth with custom enhancements
- **Email**: SMTP integration
- **API**: Django REST Framework

## 📋 Prerequisites

- Python 3.8+
- MySQL 5.7+
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Shivarajkumar21/Car-Rental-Portal.git
cd Car-Rental-Portal
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE sem5;
EXIT;

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@carrentalportal.com
```

### 7. Run the Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📚 API Documentation

### Authentication Endpoints
- `POST /api/login/` - User login
- `POST /api/register/` - User registration

### Car Management
- `GET /api/cars/` - List cars with filtering
- `GET /api/search/?q=query` - Search cars

### Booking System
- `POST /api/book/` - Book a car
- `GET /api/bookings/` - Get user bookings

### Complaints
- `POST /api/complaint/` - Submit complaint

### API Usage Example
```javascript
// Login
fetch('/api/login/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        username: 'user@example.com',
        password: 'password123'
    })
})

// Get cars with filters
fetch('/api/cars/?company=Toyota&fuel_type=Petrol&max_rent=2000')

// Book a car
fetch('/api/book/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        car_id: 'CAR001',
        booking_date: '2024-01-15',
        to_place: 'Mumbai',
        no_of_days: '3'
    })
})
```

## 🏗️ Project Structure

```
carrent/
├── carrent/                 # Main project settings
│   ├── settings.py         # Enhanced with security settings
│   ├── urls.py            # URL routing with API endpoints
│   └── wsgi.py
├── owner/                  # Main application
│   ├── models.py          # Database models
│   ├── views.py           # Web views
│   ├── api_views.py       # REST API endpoints
│   ├── forms.py           # Enhanced forms with validation
│   ├── authentication.py   # Custom authentication utilities
│   ├── notifications.py    # Email notification system
│   ├── search_utils.py     # Search and analytics utilities
│   └── admin.py
├── templates/              # HTML templates
├── static/                # CSS, JS, images
├── media/                 # User uploaded files
├── logs/                  # Application logs
└── requirements.txt       # Python dependencies
```

## 🔧 Key Components

### Authentication System (`owner/authentication.py`)
- Password hashing and validation
- Email and mobile validation
- Authentication decorators
- Session management

### API Views (`owner/api_views.py`)
- RESTful endpoints for all operations
- JSON responses with proper error handling
- Pagination and filtering support

### Search Utilities (`owner/search_utils.py`)
- Advanced car filtering
- Booking analytics
- Dashboard data aggregation

### Notification System (`owner/notifications.py`)
- Email templates and sending
- Booking confirmations
- Complaint acknowledgments

## 🎯 Usage

### For Customers
1. Register/Login to the system
2. Search and filter available cars
3. Book cars for specific dates
4. View booking history
5. Submit complaints if needed

### For Agents
1. Login with agent credentials
2. Manage car inventory
3. View and manage bookings
4. Handle customer complaints
5. Generate reports and analytics

### For Administrators
1. Access Django admin panel
2. Manage users and permissions
3. Monitor system logs
4. Configure email settings

## 🔒 Security Features

- Password strength validation
- CSRF protection
- XSS prevention
- Secure session management
- Input validation and sanitization
- SQL injection prevention
- Secure headers (HSTS, X-Frame-Options)

## 📊 Analytics & Reporting

- Booking trends and statistics
- Revenue calculations
- Popular cars analysis
- Customer behavior insights
- Complaint analytics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shivarajkumar21**
- GitHub: [@Shivarajkumar21](https://github.com/Shivarajkumar21)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap for responsive UI components
- MySQL for reliable database management

---

⭐ **Star this repository if you find it helpful!**
