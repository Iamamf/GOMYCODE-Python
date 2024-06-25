{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4d775de8-8621-4a9f-96d4-7c8a02505c21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current balance: 100020500.0\n",
      "Current balance after withdrawal: 100020200.0\n"
     ]
    }
   ],
   "source": [
    "# Create a class called \"Account\"\n",
    "class Account:\n",
    "    def __init__(self, account_number, account_balance, account_holder):\n",
    "        self.account_number = account_number\n",
    "        self.account_balance = account_balance\n",
    "        self.account_holder = account_holder\n",
    "\n",
    "    def deposit(self, amount):\n",
    "        self.account_balance += amount\n",
    "\n",
    "    def withdraw(self, amount):\n",
    "        if self.account_balance >= amount:\n",
    "            self.account_balance -= amount\n",
    "        else:\n",
    "            print(\"Insufficient funds. Withdrawal not possible.\")\n",
    "\n",
    "    def check_balance(self):\n",
    "        return self.account_balance\n",
    "\n",
    "# Create an instance of the Account class\n",
    "my_account = Account(account_number=\"1774284044\", account_balance=100000000.0, account_holder=\"Folarin\")\n",
    "\n",
    "# Deposit $500 into the account\n",
    "my_account.deposit(20500.0)\n",
    "\n",
    "# Check the current balance\n",
    "print(\"Current balance:\", my_account.check_balance())\n",
    "\n",
    "# Withdraw $300 from the account\n",
    "my_account.withdraw(300.0)\n",
    "\n",
    "# Check the current balance after withdrawal\n",
    "print(\"Current balance after withdrawal:\", my_account.check_balance())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "334183fe-e70a-4d57-99ac-427864deed36",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
