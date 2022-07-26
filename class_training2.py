import requests
import creds

class Statement:
    def __init__(self, ticker, income, bs, cf):
        self.ticker = ticker
        self.income = income
        self.bs = bs
        self.cf = cf

    def get_data(self):
        self.income = requests.get(
            f"https://financialmodelingprep.com/api/v3/income-statement/{self.ticker}?limit=5&apikey={creds.api_key}"
        )
        self.income = self.income.json()

        self.bs = requests.get(
            f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{self.ticker}?limit=5&apikey={creds.api_key}"
        )
        self.bs = self.bs.json()

        self.cf = requests.get(
            f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{self.ticker}?limit=5&apikey={creds.api_key}"
        )
        self.cf = self.cf.json()

    def net_working_capital(self):
        items = [
            "netReceivables",
            "inventory",
            "otherCurrentAssets",
            "accountPayables",
            "deferredRevenue",
            "otherCurrentLiabilities"
         ]
        nwc = []

        for i in range(len(items)+1):
            tot = 0
            for j in range(5):
                if j < 3:
                    tot += self.bs[items[j][i]]
                else:
                    tot -= self.bs[items[j][i]]
            nwc.append(tot)
        return nwc
