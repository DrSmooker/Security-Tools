import re


class PwdChecker:

    def isCommon(pwd):
        with open('top10k', 'r', encoding='UTF-8') as file:
            for commonPwd in file:
                # Strip leading and trailing whitespace from the line
                commonPwd = commonPwd.strip()
                # Check if the string is in the line
                if pwd in commonPwd:
                    return True
            return False

    def upperCase(pwd):
        return re.search(r'[A-Z]', pwd)

    def lowerCase(pwd):
        return re.search(r'[a-z]', pwd)

    def numbers(pwd):
        return re.search(r'[0-9]', pwd)

    def specialChars(pwd):
        pattern = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        # Compile the regular expression pattern

        return pattern.search(pwd)

    def checker(pwd):
        if len(pwd) > 9:
            boole = True

            if not (PwdChecker.upperCase(pwd)):
                boole = False
                print("No upper case letters")
            if not (PwdChecker.lowerCase(pwd)):
                boole = False
                print("No lower case letters")
            if not (PwdChecker.numbers(pwd)):
                boole = False
                print("No numbers")
            if not PwdChecker.specialChars(pwd):
                boole = False
                print("Password doesn't contain special characters")
            if PwdChecker.isCommon(pwd):
                boole = False
                print("Password is common")

            if boole:
                print("Great password!")

        else:
            print("Password must include more than 10 characters")


if __name__ == '__main__':
    PwdChecker.checker("111111prof_root2.sql.txt:,")
