from TorManager.TorManager import TorManager
from dotenv import load_dotenv
import os

load_dotenv()
tor_password = os.getenv('TOR_PASSWORD') 

tor_manager = TorManager(tor_password=tor_password)
headers = {
    'Content-Type' : 'application/json'
}
json_data = {
    'name' : ''
}

tor_manager.make_tor_request('https://api.kanye.rest/', 'GET')