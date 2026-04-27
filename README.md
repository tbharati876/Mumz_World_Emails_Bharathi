# 📩 Analyze emails of MUMZ World (EN + AR)

## Summary
This project is an AI-powered system that analyzes emails and outputs structured insights including intent, urgency, reasoning, confidence score, and replies in English and Arabic.

---

## Problem Statement
Support teams manually process emails, which is slow and inconsistent.

This system automates:
- Intent classification
- Urgency detection
- Response generation
- Multilingual support (EN + AR)

---

## Features
- Structured JSON output
- Multilingual responses
- Confidence scoring
- Reasoning generation
- Failure handling
- Streamlit UI

---

## Example Input and Output
I received a damaged product and want a refund.
Output:
- Intent: refund
- Urgency: high
- Confidence: 0.9

---

## Architecture
User Input -> LLM -> JSON -> Validation -> UI

---

## Tooling
- OpenRouter API
- Ngrok Auth Token
- Google Colab
- Streamlit
- Python and HTML/CSS

---

## AI Usage
Used OpenRouter and some ChatGPT with structured prompts and JSON extraction.

---

## Time Spent
nearly 5 hours.

---

## Clone the repository
https://github.com/tbharati876/Mumz_World_Emails_Bharathi

--- 
## Install the requirements and packages and enter the OpenAPI Key and Ngrok AUTH Token

---
## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
