import requests
import creds

"""
ar - Accounts Receivable
inv - Inventory
ocA - Other Current Assets
ap - Accounts Payable
def_rev = Deferred Revenue
ocL - Other Current Liabilities
"""

class Company:
    def __init__(self, ticker, years):
        self.ticker = ticker
        self.years = years
        #print(ticker)

#Done: Get ebit from API.
    def get_ebit(self):
        income_statement = requests.get(
            f"https://financialmodelingprep.com/api/v3/income-statement/{self.ticker}?limit={self.years}&apikey={creds.api_key}"
        )
        income_statement = income_statement.json()
        return list(
            reversed(
                [income_statement[i]["operatingIncome"] for i in range(len(income_statement))]
            )
        )

# x = Company("AZO")
# print(x.get_ebit())

#Done: Get receivables, inventory, ocAssets, payables, def revenue, ocLiabilities from the balance sheet.

    def get_nwc(self):
        balance_sheet = requests.get(
            f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{self.ticker}?limit={self.years}&apikey={creds.api_key}"
        )
        balance_sheet = balance_sheet.json()
        ar = list(
            reversed(
                [balance_sheet[i]["netReceivables"] for i in range(len(balance_sheet))]
            )
        )
        inv = list(
            reversed([balance_sheet[i]["inventory"] for i in range(len(balance_sheet))])
        )
        ocA = list(
            reversed(
                [balance_sheet[i]["otherCurrentAssets"] for i in range(len(balance_sheet))]
            )
        )
        ap = list(
            reversed(
                [balance_sheet[i]["accountPayables"] for i in range(len(balance_sheet))]
            )
        )
        def_rev = list(
            reversed(
                [balance_sheet[i]["deferredRevenue"] for i in range(len(balance_sheet))]
            )
        )
        ocL = list(
            reversed(
                [
                    balance_sheet[i]["otherCurrentLiabilities"]
                    for i in range(len(balance_sheet))
                ]
            )
        )


        nwc = []
        for j in range(self.years):
            if ar[j] + inv[j] + ocA[j] - ap[j] - def_rev[j] - ocL[j] < 0:
                nwc.append(0)
            else:
                nwc.append(ar[j] + inv[j] + ocA[j] - ap[j] - def_rev[j] - ocL[j])

        ppie = list(
            reversed(
                [
                    balance_sheet[i]["propertyPlantEquipmentNet"]
                    for i in range(len(balance_sheet))
                ]
            )
        )

        net_tang = []
        for i in range(self.years):
            net_tang.append(nwc[i] + ppie[i])
        return net_tang


    def get_roic(self):
        roic = []
        for i in range(self.years):
            roic.append((x.get_ebit()[i]/x.get_nwc()[i]*100))
        return ["{0:0.2f}%".format(i) for i in roic]

x = Company("AZO", 5)
print(x.get_ebit())
print(x.get_nwc())
print(x.get_roic())



#TODO calculate net working capital

#TODO calculate Return on net tangible assets.