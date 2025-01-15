thename = input('what \'s your name:').strip().capitalize
theemail = input('what \'s your email:').strip().capitalize
usename = theemail[:theemail.index("@"+1)]
web =  theemail[theemail.index("@"):]
print(f"your name is {thename} and your email is {theemail}")
print(f'you usename is {usename} \n your web sit is {web}')