import requests, hashlib

class Ecommerce:
    def __init__(
        self,
        store,
        apiKey,
        secretCode = '',
        collectUrl = 'http://35.204.26.22:8086/api/ecommerce/collect/',
        payoutUrl = 'http://35.204.26.22:8086/api/ecommerce/payout/',
        depositUrl = 'http://35.204.26.22:8086/api/ecommerce/deposit/',
        changeKeyUrl = 'http://35.204.26.22:8086/api/ecommerce/changekey/',
        transactionStatusUrl = 'http://35.204.26.22:8086/api/ecommerce/transaction/status/',
        acceptUrl = '',
        cancelUrl = '',
        declineUrl = '',
        notifyUrl = ''):

        self.store = store
        self.apiKey = apiKey
        self.secretCode = secretCode
        self.collectUrl = collectUrl
        self.payoutUrl = payoutUrl
        self.depositUrl = depositUrl
        self.changeKeyUrl = changeKeyUrl
        self.transactionStatusUrl = transactionStatusUrl
        self.acceptUrl = acceptUrl
        self.cancelUrl = cancelUrl
        self.declineUrl = declineUrl
        self.notifyUrl = notifyUrl

    def collect(
        self,
        provider,
        reference,
        amount,
        code = '',
        purchaseRef = '',
        description = ''):

        if provider == 'mtn_mobilemoney_cm':
            return self.makePayment(
                provider,
                reference,
                amount,
                code,
                purchaseRef,
                description)
        elif provider == 'orange_money_cm':
            return self.makePayment(
                provider,
                reference,
                amount,
                code,
                purchaseRef,
                description)
        elif provider == 'express_union_mobilemoney':
            return self.makePayment(
                provider,
                '237' + reference,
                amount,
                code,
                purchaseRef,
                description)
        elif provider == 'afrikpay':
            return self.makePayment(
                provider,
                '237' + reference,
                amount,
                code,
                purchaseRef,
                description)
        else:
            print('Invalid provider')
        

    def deposit():
        pass

    def payout():
        pass

    def changeKey():
        pass

    def transactionStatus():
        pass

    def makePayment(
        self,
        provider,
        reference,
        amount,
        code = '',
        purchaseRef = '',
        description = ''):

        hash = hashlib.md5((str(provider) + str(reference) + str(amount) + str(self.apiKey)).encode()).hexdigest()

        params = {
            'provider': provider,
            'reference': reference,
            'amount': amount,
            'description': description,
            'purchaseref': purchaseRef,
            'store': self.store,
            'hash': hash,
            'code': code,
            'notifurl': self.notifyUrl,
            'accepturl': self.acceptUrl,
            'cancelurl': self.cancelUrl,
            'declineurl': self.declineUrl
        }

        response = requests.post(url = self.collectUrl, params = params)
        return response.json()

    def makePayout():
        pass

    def __repr__(self):
        return str(self.store + " - " + self.apiKey)

