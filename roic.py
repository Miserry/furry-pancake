import requests
import creds

# oi = int(input("Operating income: "))
# nta = int(input("Net tangible assets: "))

def get_roic(ebit, net_tangibles):
    roic = ebit/net_tangibles*100
    return f'{roic:.2f}%'
#print(get_roic(oi, nta))

"""
ar - Accounts Receivable
inv - Inventory
ocA - Other Current Assets
ap - Accounts Payable
def_rev = Deferred Revenue
ocL - Other Current Liabilities
"""

def calculate_nwc(ar, inv, ocA, ap, def_rev, ocL):
    nwc = ar + inv + ocA - ap - def_rev - ocL
    if nwc < 0:
        return 0
    else:
        return nwc

def get_nwc(ticker, years):
    balance_sheet = requests.get(
        f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit={years}&apikey={creds.api_key}"
    )
    ar = list(
        reversed(
            [balance_sheet[i]["netReceivables"] for i in range(len(balance_sheet))]
        )
    )
    inventory = list(
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
    return ar, inventory, ocA, ap, def_rev, ocL

print(get_nwc("AZO", 5))