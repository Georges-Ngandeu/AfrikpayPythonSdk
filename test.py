from afrikpay_pip_sdk import Ecommerce, Account, Airtime, Bill

#testing some ecommerce api

# ecommerce = Ecommerce(
#     'AFC6617',
#     '661671d0bd7bef499e7d80879c27d95e',
#     '7777',
#     'http://34.86.5.170:8086/api/ecommerce/collect/',
#     'http://34.86.5.170:8086/api/ecommerce/payout/',
#     'http://34.86.5.170:8086/api/ecommerce/deposit/',
#     'http://34.86.5.170:8086/api/ecommerce/changekey/',
#     'http://34.86.5.170:8086/api/ecommerce/transaction/status/')

# ecommerce payment with mtn
# response = ecommerce.collect(
#     'mtn_mobilemoney_cm',
#     '677777777',
#     4000,
#     '123456'
# )

# ecommerce payment with orange
# response = ecommerce.collect(
#     'orange_money_cm',
#     '699999999',
#     400,
#     0000
# )

# ecommerce withdrawal with orange
# response = ecommerce.payout(
#     'orange_money_cm',
#     '699999999',
#     400
# )

#response = ecommerce.deposit()
#print(response)

# change ecommerce apikey
#response = ecommerce.changeKey()

# get ecommerce transaction status
#response = ecommerce.transactionStatus('128_1622044090')
#print(response)

#testing account apis

# account = Account(
#     '3620724907638658',
#     '3620724907638658',
#     'e825e83873eafffff315fc3f22db2d59',
#     'http://34.86.5.170:8086/api/account/transaction/status/',
#     'http://34.86.5.170:8086/api/account/agent/balance/v2/',
#     'http://34.86.5.170:8086/api/account/developer/changekey/')

# response = account.balance()
# print(response)

#testing airtime apis

# airtime = Airtime(
#     '3620724907638658',
#     '3620724907638658',
#     'e825e83873eafffff315fc3f22db2d59',
#     'afrikpay',
#     'http://34.86.5.170:8086/api/airtime/v2/',
#     'http://34.86.5.170:8086/api/airtime/status/v2/')

# response = airtime.makeAirtime(
#     'mtn',
#     '677777777',
#     1000,
#     'cash',
#     '123456789'
# )
#print(response)

# response = airtime.airtimeStatus(
#     '123456789'
# )

# print(response)


#testing bill api

# bill = Bill(
#     '3620724907638658',
#     '3620724907638658',
#     'e825e83873eafffff315fc3f22db2d59',
#     'afrikpay',
#     'http://34.86.5.170:8086/api/bill/v2/',
#     'http://34.86.5.170:8086/api/bill/getamount/',
#     'http://34.86.5.170:8086/api/bill/status/v2/')

#camwater

# response = bill.payBill(
#     'camwater',
#     '111111111111111',
#     1000,
#     'cash',
#     '96543'
# )
# print(response)

# response = bill.getBillAmount(
#     'camwater',
#     '111111111111111',
# )
#print(response)

# response = bill.getBillStatus(
#     '96543',
# )
# print(response)

#eneoprepay

# response = bill.payBill(
#     'eneoprepay',
#     '014111111111',
#     1000,
#     'cash',
#     'qsde14'
# )
# print(response)

# response = bill.getBillAmount(
#     'eneoprepay',
#     '014111111111',
# )
# print(response)

# response = bill.getBillStatus(
#     'qsde14',
# )
# print(response)