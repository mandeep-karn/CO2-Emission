# 🌍 AI Sustainability Emissions Calculator

## Overview

The AI Sustainability Emissions Calculator is an interactive Streamlit web application designed to raise awareness about the environmental impact of AI queries. By allowing users to estimate the carbon dioxide (CO2) emissions associated with different AI model interactions, this tool provides insights into the hidden environmental costs of artificial intelligence technologies.


## 🌱 Project Purpose

In an era of increasing AI usage, understanding the environmental footprint of digital technologies is crucial. This calculator helps:
- Raise awareness about AI's environmental impact
- Provide transparent estimates of CO2 emissions
- Educate users about the carbon cost of AI interactions

## ✨ Features

- Select from multiple AI models (ChatGPT-3.5, ChatGPT-4, Claude, Gemini)
- Calculate CO2 emissions based on number of queries
- Interactive visualization of emissions
- Comparative context for environmental impact
- User-friendly web interface

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

#
1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app.py
```

## 📊 Methodology

### Emission Calculations

The CO2 emission factors are estimated based on current research and represent approximate values for different AI models. Factors considered include:
- Computational resources
- Energy consumption
- Data center infrastructure

**Disclaimer:** Emissions are approximations and may vary based on specific computational environments.

## 🔍 Emission Factors

| AI Model       | CO2 per Query (kg) |
|----------------|-------------------|
| ChatGPT-3.5   | 0.0028            |
| ChatGPT-4     | 0.0045            |
| Claude        | 0.0032            |
| Gemini        | 0.0037            |



## 🙏 Acknowledgements

- Streamlit
- Plotly
- Research institutions studying AI environmental impact
