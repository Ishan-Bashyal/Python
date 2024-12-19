'''
Accept any city from the user and display monument of that city.
City Monument
Delhi Red Fort
Agra Taj Mahal
Jaipur Jal Mahal
'''

city = input("Enter a city name(delhi,agra,jaipur): ")
city = city.lower()
if (city == 'delhi'):
    print("Delhi Monument is Red Fort")
elif (city == 'agra'):
    print("Agra Monument is Taj Mahal")
elif (city == 'jaipur'):
    print("Jaipur Monument is Jal Mahal")
else:
    print("Invalid")