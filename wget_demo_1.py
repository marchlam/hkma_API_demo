import wget
url = 'https://api.hkma.gov.hk/public/market-data-and-statistics/monthly-statistical-bulletin/er-ir/er-eeri-daily'
filename = 'exchange_rate.json'
action_download = wget.download(url , filename )
