import random
import string
from datetime import datetime, timedelta

output_file_path = "account_info.txt"  # 指定要保存檔案的路徑和檔名

first_names = [
    "Alanna", "Alberto", "Galilea", "Cameron", "Madilynn",
    "Janiyah", "Maximo", "Dakari", "Emerald", "Ramona",
    "Emerie", "Johanna", "Izaiah", "Mohamed", "Malayah",
    "Kamilah", "Amoura", "Gustavo", "Sierra", "Adalee",
    "Marcelo", "Lilian", "Caspian", "Jadiel", "Madalyn",
    "Dayana", "Rodrigo", "Alondra", "Malaya", "Kennedi",
    "Jericho", "Valentin", "Paulina", "Gloria", "Vincenzo",
    "Anakin", "Amaris", "Mohammed", "Orlando", "Lakelyn",
    "Jianna", "Callahan", "Malaysia", "Johnathan", "Miranda",
    "Christina", "Guinevere", "Loretta", "Nikolas", "Meredith",
    "Sariah", "Ivanna", "Arturo", "Roselyn", "Sarahi",
    "Milana", "Azriel", "Zendaya", "Teresa", "Yareli",
    "Mikaela", "Alfredo", "Jaliyah", "Benedict", "Cartier",
    "Elliot", "Gerardo", "Kenia", "Eliel", "Alia",
    "Anahi", "Aliza", "Noemi", "Paola", "Ariya",
    "Ariel", "Eliam", "Elina", "Amani", "Aliya",
    "Uriah", "Inaya", "Graeme", "Gregory", "Greg",
    "Anselm", "Anthony", "Antony", "Angus", "Archibald",
    "Archie", "Arnold", "Arthur", "Augustin", "Augustus",
    "Auberon", "Aubrey", "Baldwin", "Bertran", "Bryan",
    "Barnaby", "Barry", "Bartholomew", "Basil", "Ben",
    "Benjamin", "Bernard", "Bernie", "Bert", "Bill",
    "Billy", "Bob", "Bobby", "Boris", "Bradford",
    "Brad", "Brandon", "Brendan", "Brian", "Bruce",
    "Bud", "Burt", "Caesar", "Calvin", "Carlton",
    "Cary", "Christian", "Carl", "Cecil", "Cedric",
    "Charles", "Charlie", "Chuck", "Christopher", "Chris",
    "Clarence", "Clark", "Claude", "Clement", "Clare",
    "Constant", "Curtis", "Clifford", "Cliff", "Clint",
    "Clive", "Clyde", "Colin", "Craig", "Curt",
    "Cyril", "Cuthbert", "Dexter", "Derby", "Dale",
    "Daniel", "Dan", "Danny", "Darrell", "Darren",
    "David", "Dave", "Dean", "Dennis", "Derek",
    "Dermot", "Desmond", "Des", "Dick", "Dirk",
    "Dominic", "Donald", "Don", "Douglas", "Doug",
    "Duane", "Dudley", "Dud", "Duncan", "Dustin",
    "Dwight", "Duke", "Earl", "Ebenezer", "Eamonn",
    "Ed", "Edgar", "Edmund", "Edward", "Edwin",
    "Eliot", "Elmer", "Elroy", "Emlyn", "Enoch",
    "Eric", "Ernest", "Errol", "Eugene", "Eli",
    "Enos", "Freddie", "Felix", "Ferdinand", "Fergus",
    "Floyd", "Francis", "Frank", "Frankie", "Frederick",
    "Fred", "Gaston", "Gabriel", "Gareth", "Gary",
    "Gavin", "Gene", "Geoffrey", "Geoff", "George",
    "Geraint", "Gerald", "Gerry", "Gerard", "Gilbert",
    "Giles", "Glen", "Godfrey", "Gordon", "Graham",
    "Graeme", "Gregory", "Greg", "Guy", "Gideon",    
]  # 美國的名
# 台灣的姓
last_names = [
    "Chen", "Huang", "Chung", "Hsu", "Lin",
    "Wang", "Li", "Wu", "Liu", "Yang",
    "Zhang", "Zhao", "Wei", "Zhu", "Yu",
    "Xu", "Sun", "Ma", "Lu", "Zhou"
]

def generate_random_name():
    # Randomly choose a first name and a last name
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def generate_random_account_info_lowercase(n=200):
    accounts = []
    for _ in range(n):
        # Generate random name
        name = generate_random_name()
        
        # Generate username with lowercase letters
        username = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@outlook.com"

        # Generate password
        # 生成一個長度為10的密碼，包括大小寫字母和數字
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        # 生成一個長度為12的chatgptpassword，包括大小寫字母和數字
        chatgptpassword = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        # Generate birth date
        start_date = datetime(1975, 1, 1)
        end_date = datetime(2000, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        birth_date = start_date + timedelta(days=random_number_of_days)
        birth_date_str = birth_date.strftime("%Y/%m/%d")

        accounts.append((name, username, password, birth_date_str, chatgptpassword))

    return accounts

# Generate 200 account information sets with lowercase usernames
account_info_lowercase = generate_random_account_info_lowercase()

# Writing the account information to a file with indices
with open(output_file_path, 'w') as file:
    for index, account in enumerate(account_info_lowercase, start=1):
        # file.write(f"{index}. Name: {account[0]}, Username: {account[1]}, Password: {account[2]}, Birth Date: {account[3]}\n")
        file.write(f"{index}.\tName: {account[0]},\tUsername: {account[1]},\tPassword: {account[2]},\tBirth Date: {account[3]},\tChatGPT Password: {account[4]}\n")
