# * * * NOTE - 09/10/2018

It has been brought to my attention that Sellecloud changed the existing API as opposed to rolling out a new version.  As a result a software update along the way would have broken this software.  I do intend to update the wrapper, but for the time being, this codebase is good for learning material but many of the API calls would no longer work.


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
  
