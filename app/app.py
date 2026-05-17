from flask import Flask, jsonify
import platform
import os
import datetime

app = Flask(__name__)
START_TIME = datetime.datetime.utcnow()

@app.route("/")
def root():
    return jsonify({
        "status": "ok",
        "message": "DevOps Portfolio API"
    })

@app.route("/health")
def health():
    uptime = (datetime.datetime.utcnow() - START_TIME).seconds
    return jsonify({
        "status": "healthy",
        "uptime_seconds": uptime,
        "hostname": platform.node(),
        "python": platform.python_version(),
        "environment": os.getenv("APP_ENV", "development")
    })

@app.route("/info")
def info():
    return jsonify({
        "app": "devops-portfolio",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "author": os.getenv("APP_AUTHOR", "Valentino Chiappiani")
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
