names = []
sugest_name = ""

while True:
    sugest_name = input("введіть імя людини (end щоб закінчити): ")
    if sugest_name == "end":
        break
    else:
        names.append(sugest_name)

def like(names):
    
    count = 0
    for _ in names:
        count += 1

    
    if count == 0:
        return "ніхто не поставив вподобайку"
    elif count == 1:
        return f"{names[0]} поставив вподобайку"
    elif count == 2:
        return f"{names[0]} і {names[1]} поставили вподобайку"
    elif count == 3:
        return f"{names[0]}, {names[1]} і {names[2]} поставили вподобайку"
    else:
        return f"{names[0]}, {names[1]} і {count - 2} поставли вподобайку"

print(like(names))