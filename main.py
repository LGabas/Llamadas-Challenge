from call import Call
from bill import Bill

bill_one = Bill(monthly_payment=20)
bill_one.add_call(Call(duration_of_call=10, type_of_call="local"))
bill_one.add_call(Call(duration_of_call=10, type_of_call="international"))
bill_one.add_call(Call(duration_of_call=5, type_of_call="national"))
print(bill_one.generate_bill())

