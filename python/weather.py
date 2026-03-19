import requests

print("hello")

def get_weather(city):
    """
    获取指定城市的当前天气信息
    
    参数:
        city (str): 城市名称
        
    返回:
        str: 包含当前气温的天气信息，或错误信息
    """
    try:
        # 使用Open-Meteo API获取天气数据（无需API密钥）
        # 首先获取城市的经纬度坐标
        geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=zh&format=json"
        geo_response = requests.get(geocoding_url, timeout=10)
        geo_data = geo_response.json()
        
        if not geo_data.get("results"):
            return f"未找到城市: {city}"
        
        # 获取第一个匹配城市的坐标
        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        
        # 使用坐标获取天气数据
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&timezone=auto"
        weather_response = requests.get(weather_url, timeout=10)
        weather_data = weather_response.json()
        
        # 提取当前气温
        current_temp = weather_data["current"]["temperature_2m"]
        temp_unit = weather_data["current_units"]["temperature_2m"]
        
        return f"{city}的当前气温为: {current_temp}{temp_unit}"
        
    except requests.RequestException as e:
        return f"获取天气信息时发生网络错误: {str(e)}"
    except (KeyError, ValueError) as e:
        return f"解析天气数据时发生错误: {str(e)}"
    except Exception as e:
        return f"获取天气信息时发生未知错误: {str(e)}"

# 获取当前时间，格式类似：2026-03-19 15:30:00
# 函数名：get_current_time
def get_current_time():
    """
    获取当前时间，格式为YYYY-MM-DD HH:MM:SS
    
    返回:
        str: 当前时间字符串
    """
    import datetime
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time

if __name__ == "__main__":
    print(get_current_time())
    city = "北京"
    weather = get_weather(city)
    print(weather)