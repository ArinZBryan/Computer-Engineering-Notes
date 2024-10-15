# Complete the definition for copy_doves
def copy_doves(src: list[str], dst: list[str]) -> None:
    for i in range(len(src)):
        bird = src[i]
        if bird.endswith("Dove"):
            dst.append(bird)

# Complete the definition of function extract_doves_and_pigeons
def extract_doves_and_pigeons(src : list[str]) -> list[str]: 
    return [ i for i in src if (i.endswith("Dove") == True or i.endswith("Pigeon") == True)]


columbid_species = ["Rock Dove", "Stock Dove", "Wood Pigeon", "Turtle Dove", "Collared Dove"]
dove_species = []
copy_doves(columbid_species, dove_species)
print(dove_species)
assert dove_species == ["Rock Dove", "Stock Dove", "Turtle Dove", "Collared Dove"]