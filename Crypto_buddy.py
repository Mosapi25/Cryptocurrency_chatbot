# 👋 Welcome to CryptoBuddy - Your First AI-Powered Financial Sidekick!

# Step 1: Define the chatbot personality
print("👋 Hello! I'm CryptoBuddy — your friendly AI crypto sidekick!")
print("💬 Ask me anything about trending or sustainable cryptocurrencies!\n")

# Step 2: Predefined crypto dataset
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

# Step 3: Start chatbot loop
def crypto_advisor():
    while True:
        user_query = input("You: ").lower()

        if "exit" in user_query or "bye" in user_query:
            print("CryptoBuddy: Goodbye and happy investing! 🚀")
            break

        elif "sustainable" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

        elif "trending" in user_query or "rising" in user_query:
            trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
            print(f"CryptoBuddy: These cryptos are trending up 📈: {', '.join(trending)}.")

        elif "long-term" in user_query or "growth" in user_query:
            for name, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] >= 0.7:
                    print(f"CryptoBuddy: {name} is trending up and has a top-tier sustainability score! 🚀")
                    break

        else:
            print("CryptoBuddy: Hmm 🤔 I’m not sure how to answer that. Try asking about trending or sustainable cryptos.")

# Run the chatbot
crypto_advisor()
