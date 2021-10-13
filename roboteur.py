import click
import requests
import json
import os


@click.group()
def roboteur():
    pass


@roboteur.command('sign-in')
@click.option('--email', prompt='Your Roboteur email please')
@click.option('--password', prompt=True, hide_input=True)
def signIn(email, password):
    '''Sign-in to Roboteur'''
    print('roboteur cli sign-in', email)
    try:
        r = requests.post('https://uat.roboteur.co.uk/api/authentication', data={
            'strategy': 'local',
            'email': email,
            'password': password
        }, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        auth = r.json()
        print('sign-in auth code', r.status_code)
        # print('sign-in auth response', auth)
        if (r.status_code == 201):
            print('sign-in success', auth['user']['username'])
            with open('_auth.json', 'w') as outfile:
                json.dump(auth, outfile)
        else:
            print('sign-in failed', auth)
    except Exception as ex:
        print('Sign-in error', ex)


@roboteur.command('sign-out')
def signOut():
    '''Sign-out of Roboteur'''
    os.remove('_auth.json')
    print('roboteur cli sign-out complete')


@roboteur.command('services')
def services():
    '''List available services'''
    click.echo('roboteur cli services')
    with open('_auth.json') as json_file:
        data = json.load(json_file)
    print('AUTH DATA', data['accessToken'])


@roboteur.command('reaction')
def reaction():
    '''Create a reaction'''
    click.echo('roboteur cli reaction')


if __name__ == '__main__':
    roboteur()
