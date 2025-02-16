import requests
import os
import datetime
from dotenv import load_dotenv
def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = current_directory + r"\.env"
    print(env_path)
    load_dotenv(env_path)
    today =  datetime.datetime.now()
    formatted_date = today.strftime("%Y%m%d")
    print(formatted_date)
    pixela_username = "fumy"
    graph_id = "graph1"
    pixela_headers = {
        "X-USER-TOKEN": os.getenv("PIXELA_TOKEN"),
    }
    pixela_parameters = {
        "quantity": input("How many minutes did you spend programming?: "),
    }
    
    # pixela_graph_create= requests.post(url= f"https://pixe.la/v1/users/{pixela_username}/graphs", json = pixela_parameters, headers = pixela_headers)
    # pixela_graph_create.raise_for_status()
    # print(pixela_graph_create)
    
    # update_pixela_graph = requests.post(url = f"https://pixe.la/v1/users/{pixela_username}/graphs/{graph_id}",headers = pixela_headers,json = pixela_parameters)
    # update_pixela_graph.raise_for_status()
    # print(update_pixela_graph)
    
    update_pixela_data = requests.put(url = f"https://pixe.la/v1/users/{pixela_username}/graphs/{graph_id}/{formatted_date}",headers = pixela_headers,json = pixela_parameters)
    update_pixela_data.raise_for_status()
    print(update_pixela_data)
if __name__ == "__main__":
    main()