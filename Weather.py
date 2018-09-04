try:
    import httplib
except:
    import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=50)
    try:
        conn.request("HEAD", "/")                            #Check The Internet Connectivity 
        conn.close()
        return True
    except:
        conn.close()
        print("No Internet Connection")
        
have_internet()
if True:
    
    import requests
    api_address="https://api.openweathermap.org/data/2.5/weather?appid=106d8ce723e3616ce4ad42f47078068d&q="
    City=input("Search :")                                
    url=api_address+City                                #api address
    json_data=requests.get(url).json()
    format_add=json_data['main']['temp']
    format_add1=json_data['weather'][0]['description']
    format_add2=json_data['wind']['speed']
    format_add3=json_data["main"]['humidity']
    format_add4=json_data["sys"]["country"]
    format_add5=json_data["main"]["temp_min"]
    format_add6=json_data["main"]["pressure"]
    print("Temperature :{}F".format(format_add)) 
    print("Weather : {}".format(format_add1))
    print("Wind Speed :{} m/s".format(format_add2))
    print("Pressure:{}".format(format_add6))
    print("Humidity :{}%".format(format_add3))
    print("Country :{}".format(format_add4))
    print("temp_min :{}F".format(format_add5))
else :
    print("Check The Internet Connection")
