from afrikpay_pip_sdk import Ecommerce

ecommerce = Ecommerce(
    'AFC5308',
    'b2b0c952269cd5c38903433759369ac7',
    '',
    'http://34.86.5.170:8086/api/ecommerce/collect/')

response = ecommerce.collect(
    'mtn_mobilemoney_cm',
    '677777777',
    450
)

print(response)