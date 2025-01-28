import requests
from bs4 import BeautifulSoup



def amazon_scrapper(product_url,output_file):
    headers = {
    "User-Agent" : "Chrome/113.0.0.0",
    "Accept-Language" : "en-US,en;q=0.9",
    "Accept-Encoding" : "gzip, deflate, br",
    "Connection" : "keep-alive"
    }
    
    try:
        response = requests.get(product_url,headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text,'html.parser')
        
        #Extracting Title
        title = soup.find("span",id = 'productTitle')
        if title:
            title = title.get_text(strip=True) 
        else:
            title = "Title not Found"
        
        #Extracting Price
        price = soup.find("span", class_ = 'a-price-whole')
        if price:
            price = price.get_text(strip=True) 
        else:
            price = "Price not Found"

        with open(output_file, 'a') as file:
            file.write(f"Prooduct name: {title}\nProduct price: {price}\n{'-'*40}")

        print("Data added successfully!!")
    except Exception as e:
        print(f"Error occured: {e}")

product_url = 'https://www.amazon.com/SOMIC-Headset-Headphones-Retractable-Cancelling/dp/B09SKPLSHT/ref=pd_pss_dp_d_1_d_sccl_2_2/141-5572868-5132667'
output_file = 'headphones.txt'
amazon_scrapper(product_url,output_file)