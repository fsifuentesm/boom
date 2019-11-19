from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from datetime import datetime
import random
import re
import csv
import phonenumbers
from phonenumbers import geocoder
from django.http import JsonResponse

# Create your views here.

@csrf_exempt 
def locate_numbers(request):

    if request.method == "POST":
        data = request.FILES['numbers']

        file_data = data.read().decode("utf-8")

        lines = file_data.split("\n")

        dt = datetime.today()
        rdm = random.randint(1, 10000)
        name_file = str(dt.year) + str(dt.month) + str(dt.day) + str(rdm)

        with open("data/output_"+ name_file +".csv", mode='w') as number_file:
            number_writer = csv.writer(number_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            number_writer.writerow(["numbers", "valid", "location"])

            for line in lines:
                fields = line.split(",")
                data_dict = {}
                data_dict["numbers"] = fields[0]
                x = data_dict["numbers"]
                x = re.sub('[^A-Za-z0-9]+', '', x)

                try:
                    number_format = phonenumbers.format_number(phonenumbers.parse(x, "US"),phonenumbers.PhoneNumberFormat.NATIONAL)
                    number = phonenumbers.parse(x, "US")
                    location = geocoder.description_for_number(number, "en")

                    if location == '':
                        location = "n/a"

                    is_valid = phonenumbers.is_valid_number(number)
                    number_writer.writerow([number_format, is_valid, location])

                except Exception as e:
                    print(e)

            data_response = {"success":True}

    return JsonResponse(data_response, safe=False)
