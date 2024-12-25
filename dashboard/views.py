from datetime import datetime, timedelta
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.db import connection



def dashboard(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminInformation

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminInformation, UAOInformation, SAAOInformation, Farmer

# Admin Registration
def admin_registration(request):
    if request.method == 'POST':
        try:
            # Collect form data
            name = request.POST.get('name', '').strip()
            father_name = request.POST.get('father_name', '').strip()
            gender = request.POST.get('gender', '').strip()
            age = request.POST.get('age', '').strip()
            latitude = request.POST.get('latitude', '').strip()
            longitude = request.POST.get('longitude', '').strip()
            division = request.POST.get('division', '').strip()
            district = request.POST.get('district', '').strip()
            upazila = request.POST.get('upazila', '').strip()
            region = request.POST.get('region', '').strip()
            aez = request.POST.get('aez', '').strip()
            hotspot = request.POST.get('hotspot', '').strip()
            risk_area = request.POST.get('risk_area', '').strip()
            nid = request.POST.get('nid', '').strip()
            personal_phone = request.POST.get('personal_phone', '').strip()
            official_phone = request.POST.get('official_phone', '').strip()
            whatsapp_number = request.POST.get('whatsapp_number', '').strip()
            facebook_id = request.POST.get('facebook_id', '').strip()
            official_email = request.POST.get('official_email', '').strip()

            # Validate required fields
            if not name or not nid or not personal_phone:
                messages.error(request, "Name, NID, and Personal Phone are required fields.")
                return render(request, 'Admin_registration.html')

            # Save data to the database
            AdminInformation.objects.create(
                name=name,
                father_name=father_name,
                gender=gender,
                age=age,
                latitude=latitude,
                longitude=longitude,
                division=division,
                district=district,
                upazila=upazila,
                region=region,
                aez=aez,
                hotspot=hotspot,
                risk_area=risk_area,
                nid=nid,
                personal_phone=personal_phone,
                official_phone=official_phone,
                whatsapp_number=whatsapp_number,
                facebook_id=facebook_id,
                official_email=official_email,
            )

            # Display a success message and redirect to the dashboard page
            messages.success(request, "Admin information saved successfully!")
            return redirect('admin_dashboard')  # Replace with the correct URL name

        except Exception as e:
            # Handle any unexpected errors
            messages.error(request, f"An error occurred: {e}")
            return render(request, 'Admin_registration.html')

    # Render the form template
    return render(request, 'Admin_registration.html')

# Similar changes should be applied to UAO, SAAO, and Farmer registration functions.

# UAO Registration
def uao_registration(request):
    if request.method == 'POST':
        # Collect form data
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        division = request.POST.get('division')
        district = request.POST.get('district')
        upazila = request.POST.get('upazila')
        region = request.POST.get('region')
        aez = request.POST.get('aez')
        hotspot = request.POST.get('hotspot')
        risk_area = request.POST.get('risk_area')
        nid = request.POST.get('nid')
        personal_phone = request.POST.get('personal_phone')
        official_phone = request.POST.get('official_phone')
        whatsapp_number = request.POST.get('whatsapp_number')
        facebook_id = request.POST.get('facebook_id')
        official_email = request.POST.get('official_email')

        # Create new UAOInformation entry
        uao_information = UAOInformation(
            name=name,
            father_name=father_name,
            gender=gender,
            age=age,
            latitude=latitude,
            longitude=longitude,
            division=division,
            district=district,
            upazila=upazila,
            region=region,
            aez=aez,
            hotspot=hotspot,
            risk_area=risk_area,
            nid=nid,
            personal_phone=personal_phone,
            official_phone=official_phone,
            whatsapp_number=whatsapp_number,
            facebook_id=facebook_id,
            official_email=official_email
        )
        
        # Save the data to the database
        uao_information.save()

        # Display success message
        messages.success(request, 'UAO Registration saved successfully!')
        return redirect('uao_dashboard')  # Replace with the correct URL name
    
    return render(request, 'uao_registration.html')

# SAAO Registration
def saao_registration(request):
    if request.method == 'POST':
        try:
            # Collect form data
            name = request.POST.get('name')
            father_name = request.POST.get('father_name')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            division = request.POST.get('division')
            district = request.POST.get('district')
            upazila = request.POST.get('upazila')
            union = request.POST.get('union')
            block = request.POST.get('block')
            region = request.POST.get('region')
            aez = request.POST.get('aez')
            hotspot = request.POST.get('hotspot')
            risk_area = request.POST.get('risk_area')
            education = request.POST.get('education')
            nid = request.POST.get('nid')
            personal_phone = request.POST.get('personal_phone')
            official_phone = request.POST.get('official_phone')
            whatsapp_number = request.POST.get('whatsapp_number')
            facebook_id = request.POST.get('facebook_id')
            official_email = request.POST.get('official_email')

            # Create new SAAOInformation entry
            saao_information = SAAOInformation(
                name=name,
                father_name=father_name,
                gender=gender,
                age=age,
                latitude=latitude,
                longitude=longitude,
                division=division,
                district=district,
                upazila=upazila,
                union=union,
                block=block,
                region=region,
                aez=aez,
                hotspot=hotspot,
                risk_area=risk_area,
                education=education,
                nid=nid,
                personal_phone=personal_phone,
                official_phone=official_phone,
                whatsapp_number=whatsapp_number,
                facebook_id=facebook_id,
                official_email=official_email
            )
            
            # Save the data to the database
            saao_information.save()

            # Display success message
            messages.success(request, 'SAAO Registration saved successfully!')
            return redirect('saao_dashboard')  # Replace with the correct URL name

        except Exception as e:
            # Handle errors
            messages.error(request, f'Error occurred while saving data: {str(e)}')
            return redirect('saao_registration')  # Replace with the correct URL name
    
    return render(request, 'saao_registration.html')

# Farmer Registration
def farmer_registration(request):
    if request.method == 'POST':
        # Collect form data
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        gwid = request.POST.get('gwid')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        division = request.POST.get('division')
        district = request.POST.get('district')
        upazila = request.POST.get('upazila')
        union = request.POST.get('union')
        block = request.POST.get('block')
        villaige = request.POST.get('villaige')
        region = request.POST.get('region')
        aez = request.POST.get('aez')
        hotspot = request.POST.get('hotspot')
        risk_area = request.POST.get('risk_area')
        education = request.POST.get('education')
        nid = request.POST.get('nid')
        agril = request.POST.get('agril')
        personal_phone = request.POST.get('personal_phone')
        secondary_phone = request.POST.get('secondary_phone')
        whatsapp_number = request.POST.get('whatsapp_number')
        imo_number = request.POST.get('imo_number')
        facebook_id = request.POST.get('facebook_id')
        official_email = request.POST.get('official_email')

        # Create Farmer instance
        farmer = Farmer(
            name=name,
            father_name=father_name,
            gender=gender,
            age=age,
            gwid=gwid,
            latitude=latitude,
            longitude=longitude,
            division=division,
            district=district,
            upazila=upazila,
            union=union,
            block=block,
            villaige=villaige,
            region=region,
            aez=aez,
            hotspot=hotspot,
            risk_area=risk_area,
            education=education,
            nid=nid,
            agril=agril,
            personal_phone=personal_phone,
            secondary_phone=secondary_phone,
            whatsapp_number=whatsapp_number,
            imo_number=imo_number,
            facebook_id=facebook_id,
            official_email=official_email,
        )

        # Save the farmer data
        farmer.save()

        # Create table for farmer based on gwid
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS `{gwid}` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            temperature FLOAT,
            soil_moisture FLOAT,
            water_level FLOAT,
            require_water FLOAT,
            rain FLOAT,
            pump TINYINT,
            charge FLOAT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)

        # Success message
        messages.success(request, 'Farmer registration was successful!')
        return redirect('farmer_dashboard')  # Replace with the correct URL name

    return render(request, 'farmer_registration.html')


from django.shortcuts import render
from .models import PotentiometerData
from django.http import JsonResponse

def potentiometer_data(request):
    # Fetch the last 10 entries ordered by timestamp in descending order
    data = PotentiometerData.objects.all().order_by('-timestamp')[:10]

    # Prepare the data lists
    temperatures = [entry.temperature for entry in data]
    soil_moistures = [entry.soil_moisture for entry in data]
    water_levels = [entry.water_level for entry in data]
    timestamps = [entry.timestamp.strftime('%Y-%m-%d %H:%M:%S') for entry in data]

    # Check if the request is an AJAX request by inspecting the header
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'timestamps': timestamps,
            'temperatures': temperatures,
            'soil_moistures': soil_moistures,
            'water_levels': water_levels,
        })
    
    # Render the template with the context if it's not an AJAX request
    return render(request, 'potentiometer_data.html', {
        'timestamps': timestamps,
        'temperatures': temperatures,
        'soil_moistures': soil_moistures,
        'water_levels': water_levels,
    })


from django.shortcuts import render
from .models import LaserData
from django.http import JsonResponse

def laser_data(request):
    # Fetch the last 10 entries ordered by timestamp in descending order
    data = LaserData.objects.all().order_by('-timestamp')[:10]

    # Prepare the data lists
    temperatures = [entry.temperature for entry in data]
    soil_moistures = [entry.soil_moisture for entry in data]
    water_levels = [entry.water_level for entry in data]
    timestamps = [entry.timestamp.strftime('%Y-%m-%d %H:%M:%S') for entry in data]

    # Check if the request is an AJAX request by inspecting the header
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'timestamps': timestamps,
            'temperatures': temperatures,
            'soil_moistures': soil_moistures,
            'water_levels': water_levels,
        })
    
    # Render the template with the context if it's not an AJAX request
    return render(request, 'laser_data.html', {
        'timestamps': timestamps,
        'temperatures': temperatures,
        'soil_moistures': soil_moistures,
        'water_levels': water_levels,
    })


from django.shortcuts import render
from .models import UltraSoundData
from django.http import JsonResponse

def sonar_data(request):
    # Fetch the last 10 entries ordered by timestamp in descending order
    data = UltraSoundData.objects.all().order_by('-timestamp')[:10]

    # Prepare the data lists
    temperatures = [entry.temperature for entry in data]
    soil_moistures = [entry.soil_moisture for entry in data]
    water_levels = [entry.water_level for entry in data]
    timestamps = [entry.timestamp.strftime('%Y-%m-%d %H:%M:%S') for entry in data]

    # Check if the request is an AJAX request by inspecting the header
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'timestamps': timestamps,
            'temperatures': temperatures,
            'soil_moistures': soil_moistures,
            'water_levels': water_levels,
        })
    
    # Render the template with the context if it's not an AJAX request
    return render(request, 'sonar_data.html', {
        'timestamps': timestamps,
        'temperatures': temperatures,
        'soil_moistures': soil_moistures,
        'water_levels': water_levels,
    })
    

from django.shortcuts import render
from django.db import connection

# Function to fetch the last row of data from a given table
def fetch_data(table_name):
    with connection.cursor() as cursor:
        # SQL query to get the last row for 'require_water', 'rain', and 'timestamp'
        cursor.execute(f"""
            SELECT require_water, rain, timestamp
            FROM `{table_name}`
            ORDER BY timestamp DESC
            LIMIT 1;
        """)
        # Fetch the result and return it
        return cursor.fetchone()

def irrigation_status(request):
    # Fetch data from each table
    table_1123_data = fetch_data('1123')
    table_1124_data = fetch_data('1124')
    table_1125_data = fetch_data('1125')

    # Process the data for the table (calculate 'From Pump' value, ensure it's not negative)
    context = {
        'data': [
            {
                'device_id': 'Device 101',  # From table 1123
                'date': table_1123_data[2],  # Timestamp
                'water_requirement': table_1123_data[0],  # require_water
                'weather_forecast': table_1123_data[1],  # rain
                'from_pump': max(table_1123_data[0] - table_1123_data[1], 0)  # Ensure from_pump is not negative
            },
            {
                'device_id': 'Device 102',  # From table 1124
                'date': table_1124_data[2],
                'water_requirement': table_1124_data[0],
                'weather_forecast': table_1124_data[1],
                'from_pump': max(table_1124_data[0] - table_1124_data[1], 0)  # Ensure from_pump is not negative
            },
            {
                'device_id': 'Device 103',  # From table 1125
                'date': table_1125_data[2],
                'water_requirement': table_1125_data[0],
                'weather_forecast': table_1125_data[1],
                'from_pump': max(table_1125_data[0] - table_1125_data[1], 0)  # Ensure from_pump is not negative
            }
        ]
    }

    # Render the template with the context
    return render(request, 'irrigation_status.html', context)




def water_requirement(request):
    return render(request, 'water_requirement.html')

def send_feedback(request):
    return render(request, 'send_feedback.html')

def user_feedbacks(request):
    return render(request, 'user_feedbacks.html')
