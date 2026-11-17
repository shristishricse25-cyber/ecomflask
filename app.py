from flask import Flask
SHOPPING_ANNOUNCEMENT="arriving soon"

@app.route('/')
def home():
    return "Welcome"
