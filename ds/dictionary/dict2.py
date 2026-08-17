movie = {
    "name": "Awarapan 2",
    'cast': ['Imraan Hashmi', 'Disha Patani'],
    "rating": 4.5,
    'genre': 'Action',
}

print(movie)
# movie.pop() # & TypeError: pop expected at least 1 argument, got 0
movie.pop('genre')
# movie.pop('genrew')  # & KeyError: 'genrew'
print(movie)

movie.popitem()  # & las tis deleted
print(movie)

#  delete single key
del movie['name']
print(movie)

# & delete completed dictionary -- removes from memory
# del movie
# print(movie)

for i in movie["cast"]:
    print(i)

li = ['name', 'age', 'marks']
ans = movie.fromkeys(li, 0)
print(ans)

movie.update({
    'cast':'Imraan Hashmi'
})

print(movie)

movie.clear()
print(movie)