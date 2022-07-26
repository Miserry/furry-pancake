import requests
import creds

company = input("Give me your ticker: ").upper()
years = int(input("How many years: "))


"""
ar - Accounts Receivable
inv - Inventory
ocA - Other Current Assets
ap - Accounts Payable
def_rev = Deferred Revenue
ocL - Other Current Liabilities
"""

def get_nwc(ticker, years):
    balance_sheet = requests.get(
        f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit={years}&apikey={creds.api_key}"
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
    for j in range(years):
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
    for i in range(years):
        net_tang.append(nwc[i] + ppie[i])
    return net_tang

net_tangible_assets = get_nwc(company, years)


def get_ebit(ticker, years):
    income_statement = requests.get(
        f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit={years}&apikey={creds.api_key}"
    )
    income_statement = income_statement.json()
    return list(reversed([income_statement[i]["operatingIncome"] for i in range(len(income_statement))]))

ebit = get_ebit(company, years)

roic = []
for i in range(years):
    roic.append((ebit[i]/net_tangible_assets[i])*100)
roic = ['{:.2f}%'.format(elem) for elem in roic]
net_tangible_assets = ['{:,}'.format(elem) for elem in net_tangible_assets]
print(f'Return on invested capital: {roic}')
#print(ebit)
print(f'Net Tangible Assets: {net_tangible_assets}')


