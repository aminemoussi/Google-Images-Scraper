import requests


def download_img(url, full_path, i):
    try:
        response = requests.get(url, timeout = 10)            #you have 10 secs to download
        if response.status_code == 200:
            with open(full_path + str(i)+".jpg", "wb") as f:
                f.write(response.content)
            print("***%s DOWNLOADED***" % i)
        else:
            print(f"ERROR, {i} DOWNLOADED FAILED, HTTP Side Status Code: {response.status_code}")
            print("Request reached the sever, Responce by the server was received but wasn't successful.")

    except requests.exceptions.Timeout:
        print(f"ERROR, Download attempt for image {i} TIMED OUT.")

    except requests.exceptions.RequestException as e:
        print(f"ERROR, HTTP Request process wasn't successful for image {i}.")