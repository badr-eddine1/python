user ={
    "id":12,
    "name":"sara",
    "interests":["AI","data science","cyber security"],
    "experience" : 2
}
user["email"]="badr@gmail.com"
email = user.get("email")
if email:
    print("email ", email)
else :
    print("email not found")



