from flask import Flask, jsonify, render_template
import requests # type: ignore
import os

app = Flask(__name__)

NASA_API_KEY = os.environ.get("NASA_API_KEY", "3ikI8GUqpdiljpyfo6R18P7wGLbDjm8XqsPBgGEJ")


# Pages 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/apod-page")
def apod_page():
    return render_template("apod.html")

@app.route("/mars-page")
def mars_page():
    return render_template("mars.html")

@app.route("/iss-page")
def iss_page():
    return render_template("iss.html")


# API endpoints 

@app.route("/apod")
def apod():
    """Astronomy Picture of the Day from NASA."""
    try:
        url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Return only what the frontend needs
        return jsonify({
            "title":       data.get("title", "No title"),
            "date":        data.get("date", ""),
            "explanation": data.get("explanation", ""),
            "url":         data.get("url", ""),
            "media_type":  data.get("media_type", "image"),
            "hdurl":       data.get("hdurl", data.get("url", "")),
        })

    except requests.exceptions.Timeout:
        return jsonify({"error": "NASA API timed out. Please try again."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch APOD: {str(e)}"}), 502


@app.route("/mars-photos")
def mars_photos():
    API_KEY = "3ikI8GUqpdiljpyfo6R18P7wGLbDjm8XqsPBgGEJ"

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2022-06-01&api_key={API_KEY}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            fallback = [
                {
                    "img_src": "https://mars.nasa.gov/system/resources/detail_files/25622_PIA23764-16.jpg",
                    "camera": "Fallback Camera",
                    "earth_date": "N/A",
                    "id": 1
                }
            ]
            return jsonify({
                "photos": fallback,
                "total": len(fallback)
            })

        data = response.json()
        photos = data.get("photos", [])

        if not photos:
            fallback = [
                {
                    "img_src": "https://mars.nasa.gov/system/resources/detail_files/25622_PIA23764-16.jpg",
                    "camera": "No Data - Sample",
                    "earth_date": "N/A",
                    "id": 1
                }
            ]
            return jsonify({
                "photos": fallback,
                "total": len(fallback)
            })

        result = []
        for photo in photos[:8]:
            result.append({
                "img_src": photo.get("img_src"),
                "camera": photo.get("camera", {}).get("full_name"),
                "earth_date": photo.get("earth_date"),
                "id": photo.get("id")
            })

        return jsonify({
            "photos": result,
            "total": len(result)
        })

    except Exception as e:
        fallback = [
        {
        "img_src": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa",
        "camera": "Mars Sample Image",
        "earth_date": "N/A",
        "id": 1
        }
        ]
        return jsonify({
            "photos": fallback,
            "total": len(fallback)
        })


@app.route("/iss-location")
def iss_location():
    """Current ISS position from Open Notify API."""
    try:
        response = requests.get(
            "http://api.open-notify.org/iss-now.json", timeout=10
        )
        response.raise_for_status()
        data = response.json()

        pos = data["iss_position"]
        return jsonify({
            "latitude":  float(pos["latitude"]),
            "longitude": float(pos["longitude"]),
            "timestamp": data.get("timestamp"),
            "message":   data.get("message", "success"),
        })

    except requests.exceptions.Timeout:
        return jsonify({"error": "ISS API timed out. Please try again."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch ISS location: {str(e)}"}), 502


# Run 

if __name__ == "__main__":
    app.run(debug=True)
