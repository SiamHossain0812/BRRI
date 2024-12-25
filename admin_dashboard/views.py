from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# views.py

# views.py

from django.shortcuts import render, redirect
from .models import AdminInfo

def login_page(request):
    if request.method == "POST":
        # Get username and password from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username and password match in the AdminInfo table
        try:
            admin_user = AdminInfo.objects.get(user_id=username)
            
            # If password matches
            if admin_user.password == password:
                # Password is correct, render register_device page
                return redirect(register_device)  # Or redirect to register_device if you prefer
            else:
                # Password does not match
                return render(request, 'login.html', {'error': 'Invalid password'})
        except AdminInfo.DoesNotExist:
            # If no matching user is found
            return render(request, 'login.html', {'error': 'Invalid username'})
    
    return render(request, 'login.html')



from django.shortcuts import render
from django.contrib import messages
from django.db import connection
from .models import UserInfo

from django.shortcuts import render
from django.contrib import messages
from django.db import connection
from .models import UserInfo

def register_device(request):
    if request.method == "POST":
        # Extract form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        user_id = request.POST.get('userID')
        password = request.POST.get('password')
        gateway_id = request.POST.get('gatewayID')

        try:
            # Step 1: Save the user data into the 'user_info' table
            user_info = UserInfo.objects.create(
                name=name,
                phone=phone,
                address=address,
                user_id=user_id,
                password=password,
                gateway_id=gateway_id
            )

            # Step 2: Create a new dynamic table for the given Gateway ID
            table_name = f"gwid_{gateway_id}"

            # SQL to create a new table dynamically with the required fields
            create_table_sql = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    entry INT AUTO_INCREMENT PRIMARY KEY,
                    id INT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    temperature FLOAT,
                    soil_moisture FLOAT,
                    water_level FLOAT,
                    battery_state INT
                );
            """

            # Execute the SQL query to create the table
            with connection.cursor() as cursor:
                cursor.execute(create_table_sql)

            # Step 3: Success message displayed on the same page
            messages.success(request, f"User {name} registered successfully, and a new table for Gateway ID {gateway_id} was created.")

        except Exception as e:
            # Handle errors, e.g., if the table creation fails
            messages.error(request, f"Error: {e}")

    return render(request, 'gw_registration.html')
