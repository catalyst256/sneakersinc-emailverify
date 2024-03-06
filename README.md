##Email address checker (Python3)

####Installation:  
python3 -m pip install -r requirements.txt  

####To run server:  
python3 server.py

####Docker Container:  
docker build -t emailverify .  
docker run -d -p 5000:5000 emailverify  

####Example Usage:  
http://localhost:5000/api/v1/verify?q=bob@anon.com


