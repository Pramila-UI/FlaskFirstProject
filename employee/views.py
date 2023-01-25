from .models import EmployeeTable
from flask import render_template , redirect , request , flash ,url_for
from application import app , db


@app.route('/')  #home url route
@app.route('/home')
def home_page():
    return render_template('home.html')

########################################

@app.route('/employee/all_employee')
def all_employee_details():
    #to query the data from the table
    all_data = EmployeeTable.query.order_by(EmployeeTable.emp_id).all()
    context = {
        "EmployeeDetails" : all_data ,
        "Message" : "Employee data fetched succesfully"
    }
    return render_template('employee/emp_details.html' , context = context)


@app.route('/employee/insert_employee' , methods = ['POST','GET'])
def insert_new_employee():
    if request.method == "POST":
        try:
            fullname =  request.form['full_name']
            email =  request.form['email']
            address =  request.form['address']
            phone_number =  request.form['phone_number']

            # email_count = EmployeeTable.query.filter(EmployeeTable.email == email).count() 
            email_count = EmployeeTable.query.filter_by(email = email).count() 
            if email_count > 0 :
                flash("Employee already exists with this email id" , 'warning')
                return redirect(url_for('all_employee_details'))

            #creating the instance for the class 
            data =  EmployeeTable(fullname , email , phone_number , address)
            db.session.add(data)
            db.session.commit()

            #creating the flash message 
            flash("Employee Inserted succesfully" , 'success')
            return redirect(url_for('all_employee_details'))
            
        except Exception as e:
            flash(f"Exception while inserting new employee : {e}" , 'warning')
            return redirect(url_for('all_employee_details'))
    
    if request.method == 'GET':
            return redirect(url_for('all_employee_details'))


@app.route('/employee/delete/<int:id>', methods = ['DELETE' , 'GET'])
def delete_details(id):
    print(request.method)
    try:
        ## we can add the description to the get_or_404 method , that will display in the exception block
        emp_data = EmployeeTable.query.get_or_404(id ,  description="No employee found for the prvided id")
        db.session.delete(emp_data)
        db.session.commit()

        flash("Employee deleted succesfully" , 'success')
        return redirect(url_for('all_employee_details'))

    except Exception as e:
        flash(f"{e}" , 'warning')
        return redirect(url_for('all_employee_details'))


@app.route('/employee/update/<int:id>' , methods = ['PUT','POST' ,'GET'])
def update_emp_details(id):
    if request.method == 'GET':
        try:
            emp_data = EmployeeTable.query.get_or_404(id ,description="No employee found for the prvided id")
            return render_template('employee/update_emp_details.html' , emp_data= emp_data)

        except Exception as e:
            flash(f"{e}" , 'warning')
            return redirect(url_for('all_employee_details'))
    
    if request.method == 'POST':
        try:
            emp_data = EmployeeTable.query.get_or_404(id ,description="No employee found for the prvided id")

            fullname =  request.form['fullname']
            email =  request.form['email']
            address =  request.form['address']
            phone_number =  request.form['phone_number']

            if emp_data.email != email:
                email_count = EmployeeTable.query.filter_by(email = email).count() 
                if email_count > 0 :
                    flash("Employee already exists with this email id" , 'warning')
                    return redirect(url_for('all_employee_details'))

            # updating the new values to the emp_data instance
            emp_data.email = email
            emp_data.address = address
            emp_data.fullname = fullname
            emp_data.phone_number = phone_number

            db.session.commit() # saving data into the database

            flash("Employee details updated successfully" , 'success')

            return redirect(url_for('all_employee_details'))
            
        except Exception as e:
            flash(f"{e}" , 'warning')
            return redirect(url_for('all_employee_details'))
