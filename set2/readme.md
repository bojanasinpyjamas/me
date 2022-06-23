# TODO: Reflect on what you learned this week and what is still unclear.

## In-class notes
* Why are there empty brackets for upper ?
* Empty () will be filled with the definition?
```
Concatenate new word
a string + !
join?
append?

a string.upper()

The word/sentence will be in uppercase 
```
### 20220615 10.25 forgot to push reading notes so will rewrite.

## Notes from code:
## exercise 0:
```
shout with a number:
    the_answer = f"{shout(a_string)}{a_number}"
```

## exercise 3:

### def is_odd
```
    if (a_number % 2) == 0: return(False); else: return(True) nope
```

### def fix_it
```
if moves=True and should_move=True: return "No Problem"
if moves=True and should_move=False: return "Duct Tape"
if moves=False and should_move=False: return "No Problem"
if moves=False and should_move=True: return "WD-40"
```

### def loop_4
```
    numberfield = []
    numbers = list(range(10))
for i in range(10):
    numberfield.append(str(numbers))
return numberfield
```

### def loop_7
```
    christmastree = []
height = 5
stars = 1
stars += 2
for i in range(height):
    christmastree.append((' ' * (height - i)) + ('*' * stars))
return christmastree
    
christmastree = []
    for i in range(8):
       row = []
    for j in range(i+1):
        row.append(" " + "*")
    christmastree.append(row)
k=0
for element in christmastree:
    if k % 2 == 0:
        pass
    else:
        christmastree.remove(element)
    k = k + 1
return christmastree
```

## Readings 
    Automate the Boring Stuff with Python
    Introduction:
    Consider a computer as a versatile tool that 'you can configure for countless tasks'

    Name is based on Monty Python, no the snake. Rewatch Flying Circus

    Simple mathematics for complex problem solving e.g. a large Sudoku puzzle
    Programming is a creative activity, endless possibilities

    What to expect:
    Chapter 1:
    2
    3
    4
    5

    Chapter 1:
    