# CodeLeap Backend Test

This is a RESTful API built with Django and Django REST Framework for the CodeLeap recruitment test.

- **API Root:** [https://codeleap-backend-test-afonsobrum.onrender.com]
- **Endpoints:** `/careers/`

- Python 3
- Django 5.x
- Django REST Framework
- Docker / Render (Deploy)

## Notes for the Reviewer (Hosting Limitations)
This project is hosted on **Render Free Tier**, which has specific behaviors:
1.  Initial Delay: The server spins down after inactivity. The first request may take up to 50 seconds to load properly.
2.  Ephemeral Data: It uses SQLite on an ephemeral filesystem. Data created via the API will reset if the instance restarts or redeploys.


