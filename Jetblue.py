import requests as r;
def Get_Prices(origin="JAX", destination="NYC", month="AUGUST 2021", data=None):
	url = "https://jbrest.jetblue.com/bff/bff-service/bestFares"
	headers ={
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"Referer": "https://www.jetblue.com/best-fare-finder",
		"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	}
	if data == None:
		data = {
			"origin": origin,
			"destination": destination,
			"fareType": "LOWEST",
			"month": month,
			"tripType": "ONE_WAY",
			"adult": "1",
			"child": "0",
			"infant": "0",
		}
	res = r.post(url=url, json=data, headers=headers)
	return res.json()

if __name__ == '__main__':
	data = {
			"origin": "JFK",
			"destination": "DFW",
			"fareType": "POINTS",
			"month": "AUGUST 2021",
			"tripType": "ONE_WAY",
			"adult": "1",
			"child": "0",
			"infant": "0",
		}
	r = Get_Prices(data=data)
	print(r)