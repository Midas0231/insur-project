from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, IntegerField, SelectField, BooleanField


app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'secret'
bootstrap = Bootstrap(app)
@app.route('/')
def index():
    return render_template('index.html')


class QuoteForm(Form):
    age = IntegerField('Age')
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    income = IntegerField('Income')
    health_rating = IntegerField('Health Rating')
    nChildren = IntegerField('# of Children')
    married = BooleanField('Married')
    purchased = BooleanField('Purchased Before?')
    
class RegisterForm(Form):
    AccID = StringField('* Account Name')
    password = StringField('password')
    email= StringField('email')
    ssn = StringField('SSN')
    name = StringField('Name')
    age = IntegerField('Age')
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    income = IntegerField('Income')
    health_rating = IntegerField('Health Rating')
    nChildren = IntegerField('# of Children')
    married = BooleanField('Married')
    purchased = BooleanField('Purchased Before?')
    
class PurchaseForm(Form):
    plan = SelectField('Plan', choices=[('planA', 'planA'), ('planB', 'planB'), ('planC', 'planC')])
    amount = IntegerField('Purchase Value')

@app.route('/get_quote', methods=['GET', 'POST'])
def get_quote():
    form = QuoteForm(request.form)
    quote = ''
    if request.method == 'POST' and form.validate():
        age = form.age.data
        gender = form.gender.data
        income = form.income.data
        health_rating = form.health_rating.data
        nChildren = form.nChildren.data
        married = form.married.data
        purchased = form.purchased.data

        # Calculate quote based on input fields
        def calculate_quote( age, gender, income, health_rating, nChildren, married, purchased):
            return 100 / health_rating * 5000; 

        quote = calculate_quote(age, gender, income, health_rating, nChildren, married, purchased)

    return render_template('get_quote.html', form=form, quote = quote)


@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    regForm = RegisterForm(request.form)
    
    if request.method == 'POST' and regForm.validate():
        AccID = regForm.AccID.data
        password = regForm.password.data
        email = regForm.email.data
        name = regForm.name.data 
        
        
        age = regForm.age.data
        gender = regForm.gender.data
        income = regForm.income.data
        health_rating = regForm.health_rating.data
        nChildren = regForm.nChildren.data
        married = regForm.married.data
        purchased = regForm.purchased.data
    
    pForm = PurchaseForm(request.form)
    if request.method == 'POST' and pForm.validate():
        plan = pForm.plan.data
        amount = pForm.amount.data
        
        
    return render_template('purchase.html', regForm=regForm, pForm = pForm)





if __name__ == '__main__':
    app.run()
