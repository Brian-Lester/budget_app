
from budget_app.config.mysqlconnection import connectToMySQL

from budget_app.models import users, main_bills

from flask import flash

class Sub_bills:
    db = 'budget_app'

    def __init__(self,data):
        self.id = data['id']
        self.sub_bill_name = data['sub_bill_name']
        self.amount = data['amount']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod 
    def save(cls,data):
        query = 'INSERT INTO sub_bills (sub_bill_name, amount , main_bill_id) VALUES(%(bill_type)s,%(amount)s,, %(main_bill_id)s)'
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return result
    
    @classmethod
    def update_sub_bill (cls, data):
        query = "UPDATE sub_bills SET sub_bill_name = %(sub_bill_name)s, amount = %(amount)s WHERE id = %(id)s"
        connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_sub_bill(cls, data):
        query = 'DELETE FROM sub_bills WHERE id = %(id)s'
        results = connectToMySQL(cls.db).query_db( query, data )
        return results
    
    @staticmethod
    def validate_sub_bill_name(bill):
        is_valid = True
        if len(bill['sub_bill_name']) < 2:
            flash("Name must be at least 2 characters long.")
            is_valid = False
        if bill['amount'] < 1:
            flash("Amount must be greater than one.")
            is_valid = False
        return is_valid 

        return result
