
#For variables (pantry limit, cooldown etc)
with open('text_files/misc_text_files/updateLog.txt') as my_file:
    updateLog = my_file.read()
with open('text_files/misc_text_files/help.txt') as my_file:
    helpContent = my_file.read()
with open('text_files/misc_text_files/faq.txt') as my_file:
    faqContent = my_file.read()
    
with open('text_files/bread_data/common_bread.txt') as my_file:
  common_bread = my_file.readlines()
  for i in range(0,len(common_bread)):
    common_bread[i] = common_bread[i].strip()

with open('text_files/bread_data/rare_bread.txt') as my_file:
  rare_bread = my_file.readlines()
  for i in range(0,len(rare_bread)):
    rare_bread[i] = rare_bread[i].strip()

with open('text_files/bread_data/mythical_bread.txt') as my_file:
  mythical_bread = my_file.readlines()
  for i in range(0,len(mythical_bread)):
    mythical_bread[i] = mythical_bread[i].strip()

with open('text_files/bread_data/legendary_bread.txt') as my_file:
  legendary_bread = my_file.readlines()
  for i in range(0,len(legendary_bread)):
    legendary_bread[i] = legendary_bread[i].strip()
pantry_limit = 1000
