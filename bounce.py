git remote add origin https://github.com/korolm07/Python-exercices---Beazley.git
git branch -M main
git push -u origin main
bounce = 3/5
height_start = 100
height = height_start*bounce
number = 1
while number < 11:
  print(number,round(height,4))
  number = number + 1
  height = height * bounce
