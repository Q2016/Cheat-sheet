# map
map({a: i+1 for i, a in enumerate(sorted(set(A)))}.get, A)



In Python 3, map returns an iterator, not a list. You still have to iterate over it, either by calling list on it explicitly, or by putting it in 
a for loop. But you shouldn't use map this way anyway. map is really for collecting return values into an iterable or sequence. Since neither 
print nor set.update returns a value, using map in this case isn't idiomatic.

Your goal is to put all the keys in all the counters in counters into a single set. One way to do that is to use a nested generator expression:

s = set(key for counter in counters.values() for key in counter)
There's also the lovely dict comprehension syntax, which is available in Python 2.7 and higher (thanks Lattyware!) and can generate sets as well 
as dictionaries:

s = {key for counter in counters.values() for key in counter}
These are both roughly equivalent to the following:

s = set()
for counter in counters.values():
    for key in counter:
        s.add(key)
