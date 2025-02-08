def beautiful_year(year):
    str_year = str(year)
    return len(set(str_year)) == len(str_year)

def find_beautiful_year(y):
    y+=1
    while not beautiful_year(y):
        y+=1
    return y

if __name__ == "__main__":
    y = int(input())
    print(find_beautiful_year(y))