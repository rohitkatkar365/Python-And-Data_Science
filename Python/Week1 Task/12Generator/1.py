# ## Exercise: Generators

# 1. Print Square Sequence using yield
# ```
#     Create Generator method such that every time it will returns a next square number

# for exmaple : 1 4 9 16 ..     
# ```

def gen(n):
    for i in range(n):
        yield i * i

sq = gen(5)
for i in sq:
    print(i)