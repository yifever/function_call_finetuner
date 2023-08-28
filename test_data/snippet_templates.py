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

if __name__ == "__main__":
    curr_path = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(curr_path, "test_function_snippets.jsonl")
    results = []
    for i, func_snip in enumerate([SNIPPET_TEST_1]):
        results.append({
            "func_id": f"test-{i}",
            "snippet":  func_snip,
        })
    write_jsonl(output_file, results)
