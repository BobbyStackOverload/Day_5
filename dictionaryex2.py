ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print(ramit["email"])
print(ramit["interests"][0])
#print(ramit)["friends"][0]["email"]

bothfriends = ramit["friends"]

for index in range(len(bothfriends)):
    if bothfriends[index]["name"] == "Jasmine":
        print(bothfriends[index]["email"])

for index in range(len(bothfriends)):
    if bothfriends[index]["name"] == "Jan":
        print(bothfriends[index]["interests"][1])

