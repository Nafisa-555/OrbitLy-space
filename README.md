# 🚀 Space Data API - Full Stack Flask Project

A full-stack web application that pulls **live data from NASA's APIs** and displays it
in a modern, space-themed UI. Built with Python (Flask) on the backend and vanilla
HTML/CSS/JS on the frontend.

# 🌍 Live Demo Link - https://orbitly-space.onrender.com
---

## 📁 Project Structure

```
space-data-api/
│
├── app.py                  ← Flask backend (all API routes + page routes)
├── requirements.txt        ← Python dependencies
│
├── templates/              ← Jinja2 HTML templates
│   ├── base.html           ← Shared layout (navbar, footer, starfield)
│   ├── index.html          ← Home page
│   ├── apod.html           ← Astronomy Picture of the Day
│   ├── mars.html           ← Mars Rover photo gallery
│   └── iss.html            ← ISS live tracker
│
└── static/
    ├── css/
    │   └── style.css       ← All styles (space dark theme)
    └── js/
        └── stars.js        ← Animated star field background
```

---

## ⚙️ Setup & Run (Step by Step)

### 1. Clone / download the project
```bash
# If using git:
git clone <your-repo-url>
cd space-data-api

# Or just navigate to the folder:
cd space-data-api
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate
# Mac / Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get a FREE NASA API key (optional but recommended)
- Visit https://api.nasa.gov
- Click **"Generate API Key"** - it's instant and free
- Open `app.py` and replace `"DEMO_KEY"` with your key:
  ```python
  NASA_API_KEY = "your_actual_key_here"
  ```
> The `DEMO_KEY` works fine for testing but has stricter rate limits.

### 5. Run the app
```bash
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## 🔗 How Frontend Connects to Backend

Flask serves the HTML pages **and** the API endpoints from the same server.

```
Browser                           Flask (app.py)
──────                            ──────────────
GET /               ──────────►  renders templates/index.html
GET /apod-page      ──────────►  renders templates/apod.html

JavaScript (fetch)  ──────────►  JSON API routes:
  fetch("/apod")                   /apod       → NASA APOD data
  fetch("/mars-photos")            /mars-photos → Curiosity Rover images
  fetch("/iss-location")           /iss-location → Live ISS coords
```

The fetch calls happen **in the browser** after the page loads,
so data always reflects the latest from NASA/ISS APIs.

---

## 📡 API Endpoints (JSON)

| Endpoint        | Method | Description                         |
|-----------------|--------|-------------------------------------|
| `/apod`         | GET    | Astronomy Picture of the Day        |
| `/mars-photos`  | GET    | 12 Mars Rover photos (Sol 1000)     |
| `/iss-location` | GET    | Live ISS latitude & longitude       |

Test them directly: `http://127.0.0.1:5000/apod`

---

## 🛠️ Tech Stack

| Layer     | Technology           |
|-----------|----------------------|
| Backend   | Python 3, Flask      |
| HTTP      | requests library     |
| Frontend  | HTML5, CSS3, JS (ES6)|
| Fonts     | Google Fonts (Orbitron + Sora) |
| Map       | OpenStreetMap embed (no key needed) |
| Data      | NASA APOD API, NASA Mars Rover API, Open Notify ISS API |

---

## 💡 Features

- 🌌 **APOD Viewer** — daily NASA space photo with full explanation + HD link
- 🔴 **Mars Gallery** — 12-photo grid with lightbox viewer
- 🛰️ **ISS Tracker** — live coordinates + map, auto-refreshes every 5 seconds
- ✨ **Animated star field** background (pure canvas JS)
- ⏳ **Loading spinners** while fetching data
- ⚠️ **Error messages** if an API call fails
- 📱 **Responsive** — works on mobile and desktop

---

## Built for Portfolio

This project demonstrates:
- REST API integration (NASA + Open Notify)
- Full-stack Python web development
- Clean code structure with error handling
- Modern UI design without any CSS framework
