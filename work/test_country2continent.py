import pycountry
import pycountry_convert as pc

def country_to_continent(country_name):
    """
    将国家名称转换为大洲名称
    :param country_name: 国家名称（字符串）
    :return: 大洲名称（字符串），如果无法匹配则返回 "Unknown"
    """
    try:
        # 将国家名称转换为 ISO 3166-1 alpha-2 国家代码（例如 "CN"）
        country_code = pc.country_name_to_country_alpha2(country_name)
        
        # 将国家代码转换为大洲代码（例如 "AS"）
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        
        # 将大洲代码转换为大洲名称（例如 "Asia"）
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        
        return continent_name
    except Exception as e:
        # 如果无法匹配，返回 "Unknown"
        return "Unknown"

# 示例测试
#countries = ["China", "Brazil", "Germany", "Kenya", "Australia", "Unknown Country"]

file = open("country2continent.erl", 'w')
file.write('-module(country2continent).\n-export([to/1]).\n')

countries = list(pycountry.countries)
for country in countries:
    file.write('to("%s") -> "%s";\n' % (country.name.lower(), country_to_continent(country.name).lower()))
    #print(f"{country.name.lower()} -> {country_to_continent(country.name).lower()}")
file.write("to(_) -> none.")
