highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

#print(highlighted_poems_list)

highlighted_poems_stripped = []

for p in highlighted_poems_list:  
  highlighted_poems_stripped.append(p.strip())
  
#print(highlighted_poems_stripped)

highlighted_poems_details = []

for p in highlighted_poems_stripped:
  highlighted_poems_details.append(p.split(':'))
  
titles = []
poets = []
dates = []

print(highlighted_poems_details[0])

for title, poet, date in highlighted_poems_details:
  titles.append(title)
  poets.append(poet)
  dates.append(date)

for index in range(0,len(highlighted_poems_details)):
  print("The poem {TITLE} was published by {POET} in {DATE}".format(TITLE=titles[index], POET=poets[index], DATE=dates[index]))


"""Finally, write a for loop that uses either f-strings or .format() to prints out the following string for each poem:"""
