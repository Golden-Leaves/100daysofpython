import pandas
def main():
    data = pandas.read_csv(r"100daysofpython/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
    cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

    necessary_info = {
        "Fur Color": ["Black","Cinnamon","Gray"],
        "Squirrel Count": [black_squirrels_count, cinnamon_squirrels_count,gray_squirrels_count],
    }
    necessary_info_dataframe = pandas.DataFrame(data = necessary_info)
    necessary_info_dataframe.to_csv("Squirrels color count.csv")
        
    #fur_color = data[(data["Primary Fur Color"] == "Gray") | (data["Primary Fur Color"] == "Cinnamon")]# Needs to get wrapped in parenthesis due to "==" having a higher order than "|"


 

    




    
    
   

    



if __name__ == "__main__":
    main()