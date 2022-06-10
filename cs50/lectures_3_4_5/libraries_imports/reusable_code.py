from cmd import PROMPT

def main():
    a = get_int('What is "A"? ') # "A" variable is - CALLER
    print(f'"A" is {a}')


def get_int(prompt): # get_int FUNCTION is - CALL
    while True:
        try: # CALLEE
            return int(input(prompt)) 
        except ValueError:
            pass # PASS, ignores EXCEPTION. Program catches, but doesn't take action
           
main()
