import os

# change working directory
os.chdir("C:/Users/shafi/Documents/Python/py_simple_program/test-folder")

""" print(os.getcwd())
print(os.listdir()) """

for files in os.listdir():
  # Check for files only
  if os.path.isfile(files):
    f_name, f_ext = os.path.splitext(files)
    f_num, f_course, f_title = f_name.split('-')
    f_num = f_num.strip()[1:].zfill(2)
    f_course = f_course.strip()
    f_title = f_title.strip()
    new_name = f'{f_num}-{f_title}{f_ext}'
    os.rename(files,new_name)
    

  

