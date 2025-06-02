# 💰 CryptoBuddy: Your First AI-Powered Financial Sidekick! 🌟

## 🤖 Overview
**CryptoBuddy** is a beginner-friendly rule-based chatbot that gives cryptocurrency investment advice based on **profitability** and **sustainability**. It helps users decide which cryptocurrencies are trending and environmentally friendly.

This project was created as part of learning about:
- AI-driven decision-making
- Rule-based conversation logic
- Simple crypto data analysis using Python


## 🚀 Features
- Answers user questions like:
  - “Which crypto is trending up?”
  - “What’s the most sustainable coin?”
  - “Which crypto is best for long-term growth?”
- Uses predefined data for Bitcoin, Ethereum, and Cardano
- Friendly chatbot tone
- Simple if-else logic (no AI libraries needed!)


## 📊 Sample Dataset

```python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}
