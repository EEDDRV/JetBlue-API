# JetBlue-API
A small package that retrieves JetBlue prices.

# How to use
## Simple search
```py
from JetBlue import Get_Prices
Get_Prices(origin="JAX", destination="NYC", month="AUGUST 2021")
```
## Advanced search
```py
from JetBlue import Get_Prices
data = {
	"origin": "JFK",
	"destination": "DFW",
	"fareType": "POINTS", #or "LOWEST"
	"month": "AUGUST 2021",
	"tripType": "ONE_WAY",
	"adult": "1",
	"child": "0",
	"infant": "0",
}
Get_Prices(data=data)
```