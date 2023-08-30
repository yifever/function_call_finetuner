import os
import textwrap

from util.json_utils import write_jsonl

SNIPPET_TEST_1 = \
'''
def order_airplane_tickets(
    num_tickets: int,
    destination: str,
    departure_date: str,
    passengers: List[Dict[str, str]],
) -> Dict[str, float]:
    """
    Orders airplane tickets and returns the total price.
    
    Parameters:
        num_tickets (int): The number of tickets to buy.
        destination (str): The destination city.
        departure_date (str): The departure date in YYYY-MM-DD format.
        passengers (List[Dict[str, str]]): A list of dictionaries containing passenger details.
                                          Each dictionary should have 'name' and 'age' keys.
                                          
    Returns:
        Dict[str, float]: A dictionary with 'total_price' as a key and the total price as a value.
    """
'''

BUSINESS_TASKS = [
    "send a client an invoice",
    "schedule a meeting",
    "generate a sales report",
    "perform an employee evaluation",
    "create an account for a new customer",
    "calculate payroll for someone",
    "calculate payroll for a team",
    "update inventory stock data",
    "track the status of a shipment",
    "assign a customer support ticket to an agent",
    "generate a unique discount code for a customer for maketing promotions",
    "enable a customer's subscription to various services",
    "disable a customer's subscription to various services",
    "modify a customer's subscription to various services",
    "renew contracts for services and subscriptions that are expiring",
    "perform a backup process of important business data",
    "check the validity of a software license for a given product",
    "onboard a new employee and do things like generate a new id, new email account, etc.",
    "allocate resources like meeting rooms, equipment, and personnel for a project or task force",
    "submit timesheets for employees, either for approval or archival",
    "calculate and distribute performance-based incentives or bonuses to employees",
    "generate employee shift schedules based on availability and workload",
    "create and approve budgets for different departments or projects"
]


if __name__ == "__main__":
    curr_path = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(curr_path, "test_function_snippets.jsonl")
    results = []
    for i, func_snip in enumerate(BUSINESS_TASKS):
        results.append({
            "function_id": f"business-{i}",
            "task":  func_snip,
        })
    write_jsonl(output_file, results)
