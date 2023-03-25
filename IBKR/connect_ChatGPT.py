# Import necessary libraries
import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import pandas as pd

# Define the EWrapper class to handle incoming messages
class IBWrapper(EWrapper):
    def __init__(self):
        self.data = []  # Initialize an empty list to store historical data

    def historicalData(self, reqId, bar):
        self.data.append([bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume])

# Define the EClient class to connect to the API
class IBClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

# Connect to the IBKR API
host = "127.0.0.1"
port = 7497
client_id = 0
wrapper = IBWrapper()
client = IBClient(wrapper)
client.connect(host, port, client_id)

# Define the contract for the data you want to request
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"

# Request historical market data using the reqHistoricalData() function
end_time = ""  # leave empty to get data up to the current time
duration = "1 Y"  # request data for the past year
bar_size = "1 day"  # request daily bars
client.reqHistoricalData(1, contract, end_time, duration, bar_size, "TRADES", 0, 1, False, [])

# Wait for the data to be returned
client.run()

# Convert the raw data to a Pandas DataFrame and print the first few rows
df = pd.DataFrame(wrapper.data, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
print(df.head())