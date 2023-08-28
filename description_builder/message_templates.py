import textwrap

# we might have multiple templates to test, some might be better than others
MESSAGE_TEMPLATE_1 = textwrap.dedent(
    """
    ###
    Below is a snippet of a python function in natural language:
        {FUNCTION_SNIPPET}    

    ### 
    Write a description of this function.
    Return the output as this example:
        {{
            "function_snippet": 
            {SNIPPET_EXAMPLE},
            "function_description": {DESCRIPTION_EXAMPLE}
        }}
    """
)

SNIPPET_EXAMPLE_1 = textwrap.dedent(
    """
    def get_current_weather(
        location: str,
        unit: str="fahrenheit"
    ) -> str:
        \"\"\"
        Get the current weather in a given location
        \"\"\"
        <function implementation...>
    """
)

DESCRIPTION_EXAMPLE_1 = textwrap.dedent(
    """
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
    """
)
