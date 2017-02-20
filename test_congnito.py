import boto3
import srp

#  setup App (client) without generating hash
COC_USER_POOL_CLIENT_ID = '53enhkpo0khlf6shc5ta1b0ssd'

AWS_ACCOUNT = '490378467565'
# user MarkWorkman
IDENTITY_POOL_ID = 'us-east-1:6aac05d7-6032-4745-bb07-4de447b7c220'

def sign_up():
    response = client.sign_up(
        ClientId = COC_USER_POOL_CLIENT_ID,
        #SecretHash = secret_hash,
        Username = 'ChristinaMarieWorkman',
        Password = 'Hyenas!12',
        UserAttributes = [
            {'Name': 'given_name',
             'Value': 'Christina'},
            {'Name': 'middle_name',
             'Value': 'Marie'},
            {'Name': 'family_name',
             'Value': 'Workman'},
            {'Name': 'email',
             'Value': 'mworkman12@gmail.com'}
        ]
    )
    print('sign up response = %s' % response)

def confirm_sign_up():
    response = client.confirm_sign_up(
        ClientId = COC_USER_POOL_CLIENT_ID,
        Username = 'ChristinaMarieWorkman',
        ConfirmationCode = '155514',
     )
    print('confirm sign up response: %s' % response)

def alt_get_credentials():
    bytes_to_hex = lambda x: "".join("{:02x}".format(ord(c)) for c in x)

    cognito = boto3.client('cognito-idp', region_name="us-east-1",
                           aws_access_key_id='AKIAJ63U4XITMUGOU23A',
                           aws_secret_access_key='uAPGsapSXzm1ra3mHKPgO4FXDbBRFgA+rg0vfP2'
                           )

    username = "MarkWorkman"
    password = "Hyenas12"

    user_pool_id = u"us-east-1:6aac05d7-6032-4745-bb07-4de447b7c220"
    client_id = u"53enhkpo0khlf6shc5ta1b0ssd"

    srp_user = srp.User(username, password)
    _, srp_a_bytes = srp_user.start_authentication()

    srp_a_hex = bytes_to_hex(srp_a_bytes)

    response = cognito.initiate_auth(
        AuthFlow='USER_SRP_AUTH',
        AuthParameters={'USERNAME': username, 'SRP_A': srp_a_hex},
        ClientId=client_id,
        ClientMetadata={'UserPoolId': user_pool_id})
    print(response)

def get_credentials():
    #boto3.setup_default_session(region_name='us-east-1')

    identity_client = boto3.client('cognito-identity',
                          region_name='us-east-1',
                          aws_access_key_id='AKIAJ63U4XITMUGOU23A',
                          aws_secret_access_key='uAPGsapSXzm1ra3mHKPgO4FXDbBRFgA+rg0vfP2')



    response = identity_client.get_id(
        AccountId=AWS_ACCOUNT,
        IdentityPoolId=IDENTITY_POOL_ID,
        Logins={  }
    )
    identity_id = response['IdentityId']
    print ("Identity ID: %s" % identity_id)

    response = identity_client.get_open_id_token(IdentityId=identity_id)
    token = response['Token']
    print ("\nToken: %s" % (token))

    resp = identity_client.get_credentials_for_identity(IdentityId=identity_id)
    secretKey = resp['Credentials']['SecretKey']
    accessKey = resp['Credentials']['AccessKeyId']

    print ("\nSecret Key: %s" % (secretKey))
    print ("\nAccess Key %s" % (accessKey))
def forgot_password():
    #boto3.setup_default_session(region_name='us-east-1')


    response = client.forgot_password(
        ClientId=COC_USER_POOL_CLIENT_ID,
        Username='MarkWorkman'
    )
    print(response)
def confirm_forgot_password():
    #boto3.setup_default_session(region_name='us-east-1')


    response = client.confirm_forgot_password(
        ClientId=COC_USER_POOL_CLIENT_ID,
        Username='MarkWorkman',
        ConfirmationCode='395778',
        Password='Hyenas!5601adfasdfasdf'
    )
    print(response)
def main():
    global client
    #boto3.setup_default_session(region_name='us-east-1')

    client = boto3.client('cognito-idp',
                          region_name='us-east-1',
                          aws_access_key_id='AKIAJ63U4XITMUGOU23A',
                          aws_secret_access_key='uAPGsapSXzm1ra3mHKPgO4FXDbBRFgA+rg0vfP2')
    #sign_up()
    #confirm_sign_up()
    #forgot_password()
    #confirm_forgot_password()
    alt_get_credentials()


# Start program
if __name__ == "__main__":
   main()
