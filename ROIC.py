import requests
api_key = '852ec16f7c9b072271357af378674bb6'
company = 'CPRT'
years = 5

oi = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}')
balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit={years}&apikey={api_key}')
balance_sheet = balance_sheet.json()
oi = oi.json()

ebit = list(reversed([oi[i]['operatingIncome'] for i in range(len(oi))]))
ar = list(reversed([balance_sheet[i]['netReceivables'] for i in range(len(balance_sheet))]))
inventory = list(reversed([balance_sheet[i]['inventory'] for i in range(len(balance_sheet))]))
ocA = list(reversed([balance_sheet[i]['otherCurrentAssets'] for i in range(len(balance_sheet))]))
ppie = list(reversed([balance_sheet[i]['propertyPlantEquipmentNet'] for i in range(len(balance_sheet))]))
ap = list(reversed([balance_sheet[i]['accountPayables'] for i in range(len(balance_sheet))]))
def_rev = list(reversed([balance_sheet[i]['deferredRevenue'] for i in range(len(balance_sheet))]))
ocL = list(reversed([balance_sheet[i]['otherCurrentLiabilities'] for i in range(len(balance_sheet))]))

nta = []   #Net Tangible assets
rotce = []

for j in range(5):
    if ar[j] + inventory[j] + ocA[j] - ap[j] - def_rev[j] - ocL[j] < 0:
        nta.append(ppie[j])
    else:
        nta.append(ar[j] + inventory[j] + ocA[j] - ap[j] - def_rev[j] - ocL[j])
    rotce.append((ebit[j] / (ppie[j] + nta[j]))*100)


year = 2017
print(f"{company}'s Return on net tangible assets")
for k in rotce:
    if k > 1000:
        k = 1000
    print(f'{year}: {k:.1f}%')
    year += 1