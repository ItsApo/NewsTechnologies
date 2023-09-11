import random

def main_menu():
    print("--------------------------------")
    print("********** MAIN MENU ***********")
    print("--------------------------------")
    print("\n Choose an option:")
    print("1 - Sign Up")
    print("2 - Log In")
    print("0 - Exit")
    
def sign_up():
    print("------------------------------")
    print("********** SIGN UP ***********")
    print("------------------------------")
    user_name = input("Enter your name: ")
    user_email = input("Enter your email: ")
    user_phone = input("Enter your phone number: ")
    user_password = input("Enter your password: ")
    return user_name, user_email, user_phone, user_password

def log_in():
    print("------------------------------")
    print("*********** LOGIN ************")
    print("------------------------------")
    captcha = 25
    user_name, user_email, user_phone, user_password = sign_up()
    
    while True:
        user_validation = input("Enter email or phone number: ")
        password_validation = input("Enter password: ")
        captcha_validation = input("CAPTCHA - Solve the following equation: 5*5 = ? ")
        
        if user_email == user_validation or user_phone == user_validation:
            if password_validation == user_password:
                if int(captcha_validation) == captcha:
                    print("Welcome", user_name)
                    user_menu()
                    break
                else:
                    print("Incorrect CAPTCHA")
            else:
                print("Invalid password")
        else:
            print("Invalid email or phone number")

def user_menu():
    login = True
    while login:
        print("--------------------------------")
        print("********** USER MENU ***********")
        print("--------------------------------")
        print("\n Choose an option:")
        print("1 - Game")
        print("2 - Credit Card")
        print("0 - Log Out")

        menu_option = input("Select an option: ")

        if menu_option == "1":
            live_game()
        elif menu_option == "2":
            purchase()
        elif menu_option == "0":
            login = False

def live_game():
    print("--------------------------------")
    print("********** LIVE GAME ***********")
    print("--------------------------------")
    vidas = 3
    puntos = 0

    while vidas > 0:
        num = random.randint(0, 9)
        if num == 0:
            vidas -= 1
            print("Lives:", vidas)
        else:
            puntos += 1
            print("Points:", puntos)

def purchase():
    print("------------------------------")
    print("********* PURCHASE ***********")
    print("------------------------------")
    compra = int(input("Enter Purchase Amount: "))
    cuotas = int(input("Enter Number of Installments: "))
    pagar = input("Start payments? Enter 1 for YES / 2 for NO: ")

    montoCuota = compra / cuotas

    print("------------------------------")
    print("********* PAYMENT ***********")
    print("------------------------------")

    while pagar != "2":
        if cuotas == 0:
            print("Your purchase has already been paid!")
            break
        else:
            cuotas -= 1
            compra -= montoCuota
            print("Remaining installments:", cuotas)
            print("Remaining amount:", compra)

    print("THANK YOU!")

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Select an option: ")
        
        if choice == "1":
            sign_up()
        elif choice == "2":
            log_in()
        elif choice == "0":
            print("THANK YOU!")
            break
