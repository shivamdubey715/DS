import requests

url = "http://127.0.0.1:5000/"

def add(num1,num2):
    endpoint = url + "add"
    data = {"num1" : num1, "num2": num2}
    response = requests.post(endpoint, json=data)
    result = response.json()["result"]
    return result

def multiply(num1, num2):
    endpoint = url + "multiply"
    data = {"num1" : num1, "num2" : num2}
    response = requests.post(endpoint, json=data)
    result = response.json()["result"]
    return result

state = True
while state:
    print("Enter the first number:")
    try:
        num1 = int(input())
        print("Enter the second number:")
        num2 = int(input())
        print("Do you want to:\n1. Add\n2. Multiply\n3. Exit")
        choice = int(input())
        if choice == 1:
            print("Result:", add(num1,num2))
        elif choice == 2:
            print("Result:", multiply(num1,num2))
        elif choice == 3:
            print("Thank you for using the service")
            state = False
    except Exception as e:
        print("Encountered Error:", e)
        print("Restarting interface")
