from datetime import datetime as dt
from prettytable import PrettyTable
import random

MIN_HOUR = 8
MAX_HOUR = 20
MIN_DAY = 0
MAX_DAY = 4
CURRENTLY_HOUR = dt.now().hour
CURRENTLY_DAY = dt.now().weekday()
CURRENTLY_MONTH = dt.now().strftime('%B').title()


class Bill:
    def __init__(self, monthly_payment):
        self.monthly_payment = monthly_payment
        self.call = []
        self.local_call_cost = 0
        self.national_call_cost = 0
        self.international_call_cost = 0

    def __str__(self):
        return f"Monthly payment: {self.monthly_payment}, Local Call Cost: {self.local_call_cost}," \
               f"National Call Cost: {self.national_call_cost}, International Call Cost: {self.international_call_cost}"

    def add_call(self, call):
        """Gets an object and raise an error if the call type is other than local, national, international.
        Otherwise, add the call to the list"""
        if call.type_of_call.lower() not in ["local", "national", "international"]:
            raise ValueError("ERROR ---> Invalid type of call. Must be 'local', 'national', or 'international'")
        else:
            self.call.append(call)

    def calculate_call_cost(self):
        """Calculates the values of the calls, according to their type."""
        for call in self.call:
            if call.type_of_call == "local":
                if MIN_HOUR < CURRENTLY_HOUR < MAX_HOUR and MIN_DAY <= CURRENTLY_DAY <= MAX_DAY:
                    self.local_call_cost += call.duration_of_call * 0.20
                else:
                    self.local_call_cost += call.duration_of_call * 0.10
            elif call.type_of_call == "national":
                self.national_call_cost += call.duration_of_call * random.uniform(0.25, 1.0)
            else:
                self.international_call_cost += call.duration_of_call * random.uniform(1.0, 3.0)

    def calculate_total_cost(self) -> float:
        """Calculate the total value of the bill"""
        return round(self.monthly_payment + self.local_call_cost + self.national_call_cost +
                     self.international_call_cost, 2)

    def generate_bill(self) -> PrettyTable:
        """Generates a table format object specifying the bill"""
        self.calculate_call_cost()
        total_cost = self.calculate_total_cost()
        bill = PrettyTable(["Billing month", "Monthly Payment", "Local Call Cost",
                            "National Call Cost", "International Call Cost", "Total Cost"])
        bill.add_row([f"{CURRENTLY_MONTH}", f"${self.monthly_payment}", f"${self.local_call_cost}",
                      f"${round(self.national_call_cost, 2)}", f"${round(self.international_call_cost, 2)}",
                      f"${total_cost}"])

        return bill











