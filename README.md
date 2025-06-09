# WhatsApp Chat Analyzer with ML & UI

A powerful tool to analyze WhatsApp chat exports using machine learning and interactive visualizations.

## Features

- 📊 Basic Statistics (message count, unique users, date range)
- 👥 Most Active Users Analysis
- 📈 Message Activity Over Time
- ☁️ Word Cloud Generation
- 😊 Sentiment Analysis
- 📋 Raw Data Preview

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ML-whatsappchat-analyzer
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Export your WhatsApp chat:
   - Open the WhatsApp chat you want to analyze
   - Click on the three dots (menu)
   - Select "More" > "Export chat"
   - Choose "Without Media"
   - Save the .txt file

2. Run the application:
```bash
streamlit run app.py
```

3. Upload your WhatsApp chat export file through the web interface

## Project Structure

```
ML-whatsappchat-analyzer/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── src/
    ├── chat_processor.py # WhatsApp chat parsing and cleaning
    └── sentiment_analyzer.py # Sentiment analysis module
```

## Features in Detail

1. **Basic Statistics**
   - Total message count
   - Number of unique users
   - Date range of the chat

2. **User Analysis**
   - Most active users
   - Message distribution by user

3. **Temporal Analysis**
   - Messages over time
   - Daily activity patterns

4. **Content Analysis**
   - Word cloud visualization
   - Sentiment analysis (positive/neutral/negative)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 