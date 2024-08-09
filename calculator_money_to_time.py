
def printStatus(total, gave, took, age):
    """
    Prints the status of the retirement calculation for a given age.

    Args:
        total (float): The total amount of money at the given age.
        gave (float): The amount of money added at the given age.
        took (float): The amount of money subtracted at the given age.
        age (int): The age at which the calculation is performed.
    """
    print(f"{round(age):<2} years  |    +{round(gave):<5}€     |    -{round(took):<5}€       | {round(total):<8}€  ")


def check_bankrupt(total, year, month):
    """
    Checks if the total amount of money is negative, indicating bankruptcy.

    Args:
        total (float): The total amount of money.
        year (int): The current year.
        month (int): The current month.

    Returns:
        bool: True if bankrupt, False otherwise.
    """
    if total < 0:
        print(f"Ran out of money in year: {year} and month: {month}")
        return True
    return False


class OneTimeInvestment:
    """
    Represents a one-time investment with a specific year and amount of money.

    Attributes:
        year (int): The year of the investment.
        amount (float): The amount of money invested.
    """

    def __init__(self, year, amount):
        self.year = year
        self.amount = amount

    def __str__(self):
        return f"Year: {self.year}, Amount: {self.amount}"


class InvestmentParameters:
    """
    Represents the parameters for retirement investment.

    Attributes:
        total (float): The initial total amount of money.
        start (int): The age of retirement, when no new deposits are made.
        rate_addition (float): The monthly rate of money addition.
        rate_takeout (float): The monthly rate of money subtraction.
        inflation_rate (float): The rate of inflation (e.g. 1.02 for 2 Percent).
        interest_rate (float): The rate of interest (e.g. 1.05 for 5 Percent).
    """

    def __init__(self, total, start, rate_addition, rate_takeout, inflation_rate, interest_rate):
        self.total = total
        self.start = start
        self.rate_addition = rate_addition
        self.rate_takeout = rate_takeout
        self.inflation_rate = inflation_rate
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Total: {self.total}, Start: {self.start}, Rate addition: {self.rate_addition}, Rate takeout: {self.rate_takeout}, Inflation rate: {self.inflation_rate}, Interest rate: {self.interest_rate}"


def howLongToBankrupt(investment_parameters, one_time_investments=[]):
    """
    Calculates the number of months until bankruptcy based on the investment parameters.

    Args:
        investment_parameters (InvestmentParameters): The parameters for retirement investment.
        one_time_investments (list, optional): A list of OneTimeInvestment objects representing one-time investments. Defaults to an empty list.

    Returns:
        int: The number of months until bankruptcy.
    """
    total = investment_parameters.total
    start = investment_parameters.start
    rate_addition = investment_parameters.rate_addition
    rate_takeout = investment_parameters.rate_takeout
    inflation_rate = investment_parameters.inflation_rate
    interest_rate = investment_parameters.interest_rate

    bankrupt = False
    current_month = 0
    current_year = 0

    print("\n====== ====== Starting simulation ====== ====== ")
    print(f"Age:       Add (monthly):    Sub (monthly):    Total:  ")

    # through the years
    for i in range(CURRENT_AGE, AGE_LIMIT):
        if bankrupt:
            break

        # check if there is a one-time investment in the current year
        for investment in one_time_investments:
            if investment.year == i:
                total += investment.amount
                print(f"Added one-time investment of {investment.amount} in year {investment.year}")

        current_year += 1
        # through the months
        for j in range(0, 12):
            current_month = j
            if bankrupt:
                break

            subtraction, addition = 0, 0

            if i <= start:
                addition = (rate_addition * (inflation_rate ** current_year))
                total += addition

            if i > start:
                subtraction = (rate_takeout * (inflation_rate ** current_year))

                total -= subtraction

            if check_bankrupt(total, i, j):
                bankrupt = True

            if MONTHLY_STATEMENTS:
                printStatus(total, addition, subtraction, i)

        if YEARLY_STATEMENTS:
            printStatus(total, addition, subtraction, i)

        total = total * interest_rate

    return current_year * 12 + current_month


def howMuchEarlier(investment_params, year, amount):
    """
    Calculates the difference in months until bankruptcy between regular and boosted investments.

    Args:
        investment_params (InvestmentParameters): The parameters for retirement investment.
        year (int): The year of the one-time investment (boost).
        amount (float): The amount of money for the one-time investment (boost).

    Returns:
        int: The difference in months until bankruptcy.
    """
    regular = howLongToBankrupt(investment_params, [OneTimeInvestment(year, 0)])
    boosted = howLongToBankrupt(investment_params, [OneTimeInvestment(year, amount)])
    print(f"Regular: {regular} months, Boosted: {boosted} months")
    print(f"Boosted is {regular - boosted} months earlier\n")
    return regular - boosted


def calculateMinimalInvestment(investment_params, last_for_target):
    """
    Calculates the minimal investment rate required to last for a target number of years.

    Args:
        investment_params (InvestmentParameters): The parameters for retirement investment.
        last_for_target (int): The target number of years.

    Returns:
        None
    """
    total = investment_params.total
    start = investment_params.start
    rate_takeout = investment_params.rate_takeout
    inflation_rate = investment_params.inflation_rate
    interest_rate = investment_params.interest_rate

    addition_rate = 0
    lasts_for = 0

    # convert desired years to months
    last_for_target = last_for_target * 12

    while lasts_for < last_for_target:
        modified_params = InvestmentParameters(total, start, addition_rate, rate_takeout, inflation_rate, interest_rate)
        lasts_for = howLongToBankrupt(modified_params)
        addition_rate += 10

    print(f"Minimal investment rate is {addition_rate - 10}€.")
    print(f"It will last for {lasts_for} months, which is {round(lasts_for / 12, 2)} years\n")


MONTHLY_STATEMENTS = False
YEARLY_STATEMENTS = True
CURRENT_AGE = 23 # the assumed age of starting the investment
AGE_LIMIT = 86 # the assumed year of death (no further money is taken out)
params = InvestmentParameters(0, 55, 1000, 2500, 1.02, 1.05)

calculateMinimalInvestment(params, 60)
    



    
    