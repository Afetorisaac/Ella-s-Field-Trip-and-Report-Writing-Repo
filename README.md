# Ella's Field Trip and Report Writing Repo

This repository contains the completed field trip report for Korle-Bu Teaching Hospital (Emmanuella Nana Ama Weir) and a minimal working prototype (Flask backend + static frontend) that demonstrates the procurement request workflow.

Structure:
- report1_complete.md — completed field trip report (full document)
- backend/ — minimal Flask backend providing a simple API for procurement requests
- frontend/ — static HTML/JS demo UI to submit and list requests
- .github/workflows/ci.yml — example CI workflow

Quick start (local):
1. Install Python 3.10+ and pip
2. cd backend && pip install -r requirements.txt
3. python app.py  # runs server on http://127.0.0.1:5000
4. Open frontend/index.html in your browser to use the demo UI (it calls the backend at http://127.0.0.1:5000)

NOTE: This is a minimal prototype for demonstration. For production, follow the report's recommendations: use production-grade database, TLS, reverse proxy, and proper authentication.