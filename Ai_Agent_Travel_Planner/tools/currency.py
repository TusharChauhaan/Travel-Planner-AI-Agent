import requests
from langchain_core.tools import tool
import requests
from langchain_core.tools import tool
class CurrencyTool:
        @tool
        @staticmethod
        def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
            """
            Convert an amount from one currency to another using exchangerate.host API.

            Args:
                amount (float): Amount to convert.
                from_currency (str): ISO code to convert from (e.g., "INR").
                to_currency (str): ISO code to convert to (e.g., "USD").

            Returns:
                str: Converted result string, or error message if failed.
            """
            access_key = ""  # ← Replace with your key
            url = (
                "https://api.exchangerate.host/convert"
                f"?access_key={access_key}"
                f"&from={from_currency.upper()}"
                f"&to={to_currency.upper()}"
                f"&amount={amount}"
            )
            try:
                res = requests.get(url, timeout=10).json()
                if not res.get("success") or "result" not in res:
                    return f"Conversion failed. Response: {res}"
                return f"{amount} {from_currency.upper()} = {res['result']} {to_currency.upper()}"
            except Exception as e:
                return f"Error during currency conversion: {str(e)}"
