# Import necessary modules from Flask and WTForms
from flask import Flask, render_template 
from flask_wtf import FlaskForm  
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length 

# Initialize Flask application
app = Flask(__name__)  
# Secret key required for secure form submissions (CSRF protection)
app.config["SECRET_KEY"] = "secret_key"  

# Define the user registration form
class RegisterForm(FlaskForm):  
    name = StringField("Name", validators=[DataRequired(), Length(min=3)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

# Define the main route for registration
@app.route('/', methods=['GET', 'POST'])
def register():  
    form = RegisterForm() 
    
    if form.validate_on_submit(): 
        return f"Registered user: {form.name.data}, Email: {form.email.data}" 
    return render_template('register.html', form=form)  

# Run the application
if __name__ == "__main__":  
    app.run(debug=True)  