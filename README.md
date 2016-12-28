##Email address checker

####Installation:
pip install -r requirements.txt  

####To run server:
python server.py

####Docker Container (without Tor support):
docker build -t emailverify .  
docker run -d -p 8080:8080 emailverify

####Example Usage:
http://localhost:8080/api/v1/verify/?q=bob@anon.com


