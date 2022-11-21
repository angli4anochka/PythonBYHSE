postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"

}

postcards.update({
    "Peter": "Paris",
    "Ivan": "Moscow"
})

postcards["Oleg"] = "Sydney"

res = list(set(val for dic in postcards for val in postcards.values()))


print(postcards)
print(len(res))


