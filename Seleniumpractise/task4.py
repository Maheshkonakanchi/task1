
table = []
elements = flight_name=driver.find_element_by_xpath("//*[@id='flightForm']/section[2]/div[4]/div/nav/ul/li/table/tbody[2]/tr[1]/th[1]/span/img")

for element in elements:
   table.append(element.get_attribute('title')) # takes over 60 seconds (2000 elements)

print(table)