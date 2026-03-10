def get_full_name(first_name:str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    print(full_name)


get_full_name("AQUIB", "ahmed")


def get_name_with_age(name: str, age:int):
    ans = name + " is this year old: " + str(age)
    print(ans)

get_name_with_age("aquib",25)

def some_function(data:any):
    print(data)

some_function("hey")

def process_items(items: list[str]): #str here inside square brackets is type parameter., rest above are all types;
    for i in items:
        print(i.capitalize())

process_items(["ajay", "ram", "parakash"])

#with tuple and set
def process_tiems(items_t:tuple[int,int,str], items_s:set[bytes]):
    print(items_t, items_s)

process_tiems([1,2,3], [1,3]) #just type hints and not enforced at run time used for helping humans 

#with Dict
def process_dict(prices:dict[str, float]):
    for i,j in prices.items():
        print(i,j)

process_dict({
    "curd":19.5,
    "milk":25,
    "rice":50
    })

#union
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

def process_item(item: int | str):
    print(item)