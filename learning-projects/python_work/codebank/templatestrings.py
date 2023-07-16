from string import Template

def main():

    # create template with placeholders:
    templ = Template("I'm eating ${food} and drinking ${drink} tonight")
    
    # 1. substitute with keyword arguments
    str1 = templ.substitute(food="pizza", drink="tango")
    print(str1)
    
    # 2. substitute with a dictionary
    data = {
        "food" : "Pizza",
        "drink" : "Tango"
    }
    str2 = templ.substitute(data)
    print(str2)

if __name__ == "__main__":
    main()

# Template method useful for inputting data that you don't have control over/own. Using standard format method has security issues due to power.