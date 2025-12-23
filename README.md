# Maji Rahisi — USSD Application

Maji Rahisi is a multilingual USSD application that enables users with basic mobile phones to access water-related services: check water prices, report issues, find water points, and learn about the initiative.

## Table of Contents
- [Features](#features)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [Development Notes](#development-notes)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features
- Multilingual support: English, Kiswahili, Sheng.
- Water price lookup (e.g., 20L jerrican) and comparisons across locations.
- Issue reporting (poor quality, unavailability, high prices) with confirmation.
- Nearby water point discovery.
- Intuitive navigation controls: `0` (back), `00` (home), `e` (exit).
- Proper USSD session handling (use `CON` for continuing menus and `END` to terminate).

## Quick Start

Prerequisites:
- Python 3.8+ and `pip`
- An Africa's Talking account (USSD gateway credentials)

Install dependencies:

```bash
pip install -r requirements.txt
```

Set required environment variables (example):

Windows (PowerShell):

```powershell
$env:AT_USERNAME="your_username"
$env:AT_API_KEY="your_api_key"
```

Run the Flask app locally:

```bash
python app.py
# or
flask run --host=0.0.0.0 --port=5000
```

## Usage

The application exposes a `/ussd` endpoint that accepts POST requests from Africa's Talking. Africa's Talking sends the `text` parameter that contains the user's input (separated by `*`).

Example local curl request:

```bash
curl -X POST http://localhost:5000/ussd \
	-d "sessionId=12345" \
	-d "serviceCode=*123#" \
	-d "phoneNumber=254700000000" \
	-d "text="
```

## Testing

- Local testing: use `curl` or Postman to POST to `/ussd`.
- End‑to‑end: use the Africa’s Talking USSD simulator to validate session flows and termination (CON/END).

## Deployment

This project is deployed on Render (connected to GitHub). Configure Africa's Talking to send USSD requests to your deployed `/ussd` endpoint.

## Development Notes

- Navigation is parsed from the `text` string using `*` as a separator.
- The app supports returning to previous menus (`0`), returning home (`00`), and exiting (`e`).
- Use `CON` replies for intermediate menus and `END` to terminate sessions per Africa's Talking requirements.

## Future Enhancements

- Persist reported issues to a database.
- Integrate real-time pricing data.
- Add optional location detection to improve nearby water-point results.
- Add analytics and richer logging/monitoring.

## Contributing

- Open issues or submit pull requests to improve features, localization, or testing.

## License

No license specified. Add a `LICENSE` file if you wish to set one.

---

If you'd like, I can also add a short example `requirements.txt`, an `.env.example`, or update `app.py` with a brief README-linked comment explaining environment variables and run commands.