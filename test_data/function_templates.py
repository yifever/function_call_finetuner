# template for functions that we use
import os
import textwrap
from util.json_utils import write_jsonl


FUNCTION_TEST_1 = (
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
)


_DATABASE_SCHEMA_STRING = """
Table: albums
Columns: AlbumId, Title, ArtistId
Table: sqlite_sequence
Columns: name, seq
Table: artists
Columns: ArtistId, Name
Table: customers
Columns: CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId
Table: employees
Columns: EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax, Email
Table: genres
Columns: GenreId, Name
Table: invoices
Columns: InvoiceId, CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingState, BillingCountry, BillingPostalCode, Total
Table: invoice_items
Columns: InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity
Table: media_types
Columns: MediaTypeId, Name
Table: playlists
Columns: PlaylistId, Name
Table: playlist_track
Columns: PlaylistId, TrackId
Table: tracks
Columns: TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice
Table: sqlite_stat1
Columns: tbl, idx, stat
"""

_FUNCTION_2_DESCRIPTION = textwrap.dedent(
f"""
SQL query extracting info to answer the user's question.
SQL should be written using this database schema:
{_DATABASE_SCHEMA_STRING}
The query should be returned in plain text, not in JSON.
"""
)

FUNCTION_TEST_2 = (
    {
        "name": "ask_database",
        "description": "Use this function to answer user questions about music. Input should be a fully formed SQL query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": _FUNCTION_2_DESCRIPTION,
                }
            },
            "required": ["query"],
        },
    }
)

if __name__ == "__main__":
    curr_path = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(curr_path, "test_function_descriptions.jsonl")
    results = []
    for i, func_desc in enumerate([FUNCTION_TEST_1, FUNCTION_TEST_2]):
        results.append({
            "func_id": f"test-{i}",
            "description":  func_desc,
        })
    write_jsonl(output_file, results)
