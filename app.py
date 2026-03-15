from flask import Flask
app = Flask(_name_)
@approute("/")
def home():
return "Welcome to Flask CI/CD with Kubernetes!"
if _name_ == "_main_":
app.run(host="0.0.0.0",port=5000)
