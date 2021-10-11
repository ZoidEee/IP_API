# Ip_API

Ip_API is a Python library for implementation of the "IP-API" API found at https://ip-api.com. This is for the free plan they offer that has 45 request/ minute. 

## Installation

Work in progress 


## Usage
Changing the number between 1 - 3 after the IP address allows for more detailed information to be displayed. 

1:  status, message, continent, country, countryCode, regionName, city, zip, timezone, currency, query


2: status, message, continent, continentCode, country, countryCode, region, regionName, city, district, zip, lat, lon, timezone, currency, isp, query

3: status, message, continent, continentCode, country, countryCode, region, regionName, city, district, zip, lat, lon, timezone, currency, isp, org, as, asname, reverse, mobile, proxy, hosting, query

```python
from ip_api import IpApi

core = IpApi("123.345.67.89",1)

print(core.locate())

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)
