# 🔗 URL Shortener - Flask Edition

> **Transform long URLs into short, shareable links with style!**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?style=flat-square&logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-65.3%25-orange?style=flat-square&logo=html5)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)

---

## ✨ Features

- 🚀 **Lightning Fast URL Shortening** - Convert long URLs to short codes instantly
- 🎯 **Easy to Use** - Simple, intuitive web interface
- 📊 **Click Tracking** - Monitor how many times your shortened URLs are accessed
- 🔐 **Secure** - Safe URL validation and handling
- 💾 **Persistent Storage** - URLs are saved and retrievable
- 🎨 **Beautiful UI** - Modern, responsive design with HTML5
- 📱 **Mobile Friendly** - Works seamlessly on all devices
- ⚡ **Lightweight** - Minimal dependencies, fast deployment

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Backend logic & server-side processing (34.7%) |
| **Flask** | Lightweight web framework |
| **HTML5** | Frontend & user interface (65.3%) |
| **CSS3** | Styling & responsive design |
| **SQLite/Database** | URL storage & retrieval |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/vibecodersxdddddd/url-shortener-flasks.git
   cd url-shortener-flasks
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

---

## 🚀 Quick Start

### Shorten a URL
1. Open the application in your browser
2. Paste your long URL in the input field
3. Click "Shorten" button
4. Copy your new short URL and share it!

### Access Shortened URL
Simply visit your short URL, and you'll be redirected to the original link.

---

## 📝 API Endpoints

### Create Short URL
```bash
POST /api/shorten
Content-Type: application/json

{
  "url": "https://example.com/very/long/url/that/is/very/tedious"
}
```

**Response:**
```json
{
  "short_url": "http://localhost:5000/abc123",
  "original_url": "https://example.com/very/long/url/that/is/very/tedious",
  "clicks": 0
}
```

### Redirect to Original URL
```bash
GET /:short_code
```

### Get Statistics
```bash
GET /api/stats/:short_code
```

---

## 📊 Project Structure

```
url-shortener-flasks/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Home page
│   └── dashboard.html    # Stats dashboard
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── script.js     # Client-side logic
├── database/
│   └── urls.db           # SQLite database
└── README.md             # This file
```

---

## 🎨 Features in Detail

### 🔗 URL Shortening Algorithm
- Generates unique, collision-free short codes
- Uses alphanumeric characters for maximum compatibility
- Customizable short code length

### 📈 Analytics Dashboard
- Track total clicks per URL
- View creation timestamp
- Monitor original URL information

### 🔒 Security Features
- URL validation before storage
- Prevention of duplicate entries
- Sanitized input handling

---

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Database settings
DATABASE_PATH = 'database/urls.db'

# Short URL settings
SHORT_CODE_LENGTH = 6

# Server settings
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000
```

---

## 📚 Dependencies

```
Flask==2.3.0
Flask-SQLAlchemy==3.0.0
python-dotenv==1.0.0
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🚀 Deployment

### Deploy to Heroku
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Deploy to PythonAnywhere
1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload your code
3. Configure WSGI settings
4. Start your web app

### Deploy to AWS/GCP
Use Docker containerization for easy deployment:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

## 🐛 Troubleshooting

### Issue: Port 5000 already in use
```bash
# Use a different port
python app.py --port 5001
```

### Issue: Database errors
```bash
# Reset database
rm database/urls.db
python app.py  # Database will be recreated
```

### Issue: Module not found
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt
```

---

## 📈 Usage Statistics

Track your URL performance:
- **Total URLs shortened**: Stored in database
- **Click-through rate**: Monitor engagement
- **Most popular links**: Identify trending content

---

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📋 Roadmap

- [ ] User authentication & accounts
- [ ] Custom short codes
- [ ] QR code generation
- [ ] Advanced analytics dashboard
- [ ] URL expiration dates
- [ ] API rate limiting
- [ ] Dark mode UI
- [ ] Export statistics to CSV

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 👨‍💻 Author

**vibecodersxdddddd**
- GitHub: [@vibecodersxdddddd](https://github.com/vibecodersxdddddd)
- Project: [URL Shortener Flask](https://github.com/vibecodersxdddddd/url-shortener-flasks)

---

## 🌟 Support

If you found this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 💬 Sharing feedback
- 🤝 Contributing improvements

---

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/vibecodersxdddddd/url-shortener-flasks/issues)
- **Discussions**: [GitHub Discussions](https://github.com/vibecodersxdddddd/url-shortener-flasks/discussions)

---

<div align="center">

### Made with ❤️ by the URL Shortener Team

**Star this repo if you found it useful! ⭐**

</div>
