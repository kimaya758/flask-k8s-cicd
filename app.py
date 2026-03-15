from flask import Flask
app = Flask(_name_)
@approute("/")
def home():
return "Welcome to Updated Version of Flask CI/CD!"
if _name_ == "_main_":
app.run(host="0.0.0.0",port=5000)
