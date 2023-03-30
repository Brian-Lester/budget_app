
from budget_app import app

from flask import Flask, render_template, request, redirect, session, flash

from budget_app.models import users, main_bills ,budget, sub_bills


@app.route('/expenses/newbill') #works will just need to render to proper page
def new_bill():
    if 'user_info' not in session:
        return redirect ('/')
    use = users.User.get_one_by_id({'id': session['user_info']})#might be extra
    return render_template('create_main_bill.html', use = use, )
    
@app.route('/expenses/newbill/create', methods = ['POST'])
def create_bill():
    if 'user_info' not in session:
        return redirect ('/')
    data = {
        'bill_type' : request.form['bill_type'],
        'budget_main_bills_id': session['user_info']
    }
    new_b = main_bills.Main_bill.save(data)
    print(f'this is the new bill{new_b}')
    return redirect('/dashboard')