# Sellercloud
Python 3.x wrapper to interact with Sellercloud SOAP web services.  This wrapper makes integration simple.  ~250 of ~1000 API calls have been implemented.

# To collect the package:

From the Pypi package manager:
pip install Sellercloud

From git version control:
git clone https://github.com/HLXCo/Sellercloud.git

# Basic functionality:

```python
# * -	Import our Sellercloud library
from Sellercloud import Sellercloud

# * -	Declare your credentials (name, password & host)
Credentials = {"WSDL":"http://ws.sellercloud.com/scservice.asmx?WSDL" # Replace this with your WSDL
	,"UserName":"developer@yourdomain.com"
	,"Password":"your_password"}

# * -	Instantiate the object
sc = Sellercloud(Credentials)

# * -	Call one of any of the documented methods & print the result
print(sc.GetClientID())
```
  
