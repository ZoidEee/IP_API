from requests import get


class IpApi:
    def __init__(self, ip_address, ip_detailed=int()):
        self.ip_address = ip_address
        self.ip_detailed = ip_detailed

    def locate(self):
        str(self.ip_address)
        if self.ip_detailed == 1:
            basic_info = get(
                f"http://ip-api.com/csv/{self.ip_address}?fields=status,message,continent,country,countryCode,"
                f"regionName,city,zip,timezone,currency,query").text.strip("\n").split(",")
            return basic_info
        elif self.ip_detailed == 2:
            inter_info = get(f"http://ip-api.com/csv/{self.ip_address}?fields=status,message,continent,continentCode,"
                             f"country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,"
                             f"query").text.strip("\n").split(",")
            return inter_info
        elif self.ip_detailed == 3:
            adv_info = get(f"http://ip-api.com/csv/{self.ip_address}?fields=status,message,continent,continentCode,"
                           f"country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,"
                           f"org,as,asname,reverse,mobile,proxy,hosting,query").text.strip("\n").split(",")
            return adv_info
