#Nested Data Structure
data = {
  "user" :{
    "name" : "Hijbullah",
    "id" : 123,
    "contact" : {
      "email" : "hijbullah119445@gmail.com",
      "phone" : "01748470965",
  }
  },
  "items" : [
    {"name": "Laptop", "price" : 1200},
    {"name": "keyboard", "price": 75}
  ]
}

print("User Name: ", data["user"]["name"])
print("First Item Price: ", data["items"][0]["price"])
print("User Email: ", data["user"]["contact"]["email"])

