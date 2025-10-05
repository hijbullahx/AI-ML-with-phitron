#Loop and else-if condition

samples = [0,1,"","text",[],[1],{},{"k": 1}, None]
for item in samples:
  if item:
    print(repr(item), "-> Truthy")
  else:
    print(repr(item), "-> Falsy")

#f_strings
name = "Hijbullah"
score = 99
print(f"{name} scored {score}% (next: {score+1}%)")