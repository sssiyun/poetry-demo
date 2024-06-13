import pandas as pd
import requests


def get_data(username):
    # example to get data from request
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()
    print(f"Get {username} github profile info successfully!\n")
    print(f"Details: {data}\n")
    print("-" * 50)
    return data


def parse_data(data):
    # example to parse data
    info_df = pd.DataFrame(data, index=[0])
    print(f"\nParse data to DataFrame successfully!\n")
    print("Info DataFrame:")
    print(info_df)
    print("-" * 50)
    return info_df


if __name__ == "__main__":
    print(">" * 10, "Demo", "<" * 10)

    user = "designlibro"

    # get profile info from github url
    info_data = get_data(user)

    # parse data to dataframe
    parse_data(info_data)
