import sys
import traceback as tb

try:
    dividend=int(input("enter dividend: "))
    divisor=int(input("enter divisor: "))
    result=dividend/divisor
    print(result)

except ZeroDivisionError as err:
    print(f"{err} : divisor cannot be zero")
    e_type,e_cause,tb=sys.exc_info()
    print(f"{e_type},{e_cause}")
except ValueError as err:
    print(err)
    tb.print_exc()
else:
    print("contINUE")
finally:
    print("fInAlLy ExEcUtEs SuCcEsSfUlLy")
