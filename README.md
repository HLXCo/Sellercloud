# Sellercloud
Python 3.x wrapper to interact with Sellercloud SOAP web services.  This wrapper makes integration simple.  ~250 of ~1000 API calls have been implemented.

# To collect the package:

pip install Sellercloud

# Basic functionality:

from Sellercloud import Sellercloud
Credentials = {"WSDL":"http://ws.sellercloud.com/scservice.asmx?WSDL" # Replace this with your WSDL
	,"UserName":"developer@yourdomain.com"
	,"Password":"your_password"}

sc = Sellercloud(Credentials)
print(sc.GetClientID())
  
