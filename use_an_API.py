#################################################
#
# Saul Contreras (Suulcoder)
#
#   This code only answers the questions 
#   of the Use an API SECTION
#################################################

import requests
import time

#how_many_employees_earn_more_than_300k
#   Type:           Int
#   Parameters:     None
#   Description:    Returns how many employees earn more than 300k
def how_many_employees_earn_more_than_300k():
    response = requests.get(
        'http://dummy.restapiexample.com/api/v1/employees', 
        headers={"User-Agent": "XY"}
        )
    if(response.status_code==200):
        count_to_return = 0
        for employee in response.json()["data"]:
            if int(employee["employee_salary"]) > 300000:
                count_to_return += 1
        return count_to_return
    else:
        raise Exception("Something went wrong with the API (status code: {})".format(response.status_code))

#create_a_record_with_your_name
#   Type:           String
#   Parameters:     name: String
#   Description:    Create a record with your name
def create_a_record_with_your_name(name):
    response = requests.post(
        'http://dummy.restapiexample.com/api/v1/employee/create', 
        headers={"User-Agent": "XY"},
        json={
                "employee_name" : name,
                "employee_salary" : 400000,
                "employee_age" : 23,
                "profile_image": ""
            }
        )
    if(response.status_code==200):
        return "Record created successfully", response.json()["data"]["id"]
    else:
        raise Exception("Something went wrong with the API (status code: {})".format(response.status_code))


#Answers:

# print("How many employees earn more than 300k?\n")
# print(how_many_employees_earn_more_than_300k())
# time.sleep(60)

print("Create a record with your name\n")
created_record = create_a_record_with_your_name("Saul Contreras")
print(created_record[0])

print("What’s your user id?")
print(created_record[1])

