import textwrap

# we might have multiple templates to test, some might be better than others
MESSAGE_TEMPLATE_1 = textwrap.dedent(
    """
    ###
    Below is the description of a function:
        "function_description":
        {FUNCTION_DESCRIPTION}    

    ### 
    Write a user prompt that would call this function, and the function call.
    Return the output as this example:
        {{
            "function_description": 
            {FUNCTION_EXAMPLE},
            "user_prompt": {PROMPT_EXAMPLE},
            "function_call": {CALL_EXAMPLE}
        }}
    """
)

PROMPT_EXAMPLE = textwrap.dedent(
    """
    "what is the weather going to be like in Glasgow, Scotland over the next 7 days"
    """
)

FUNCTION_EXAMPLE = textwrap.dedent(
    """
    {
        "name": "get_n_day_weather_forecast",
        "description": "Get an N-day weather forecast",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "format": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "The temperature unit to use. Infer this from the users location.",
                },
                "num_days": {
                    "type": "integer",
                    "description": "The number of days to forecast",
                }
            },
            "required": ["location", "format", "num_days"]
        },
    }
    """
)

CALL_EXAMPLE = textwrap.dedent(
    """
    {
        "name": "get_n_day_weather_forecast",
        "arguments": "{\n  "location": "Glasgow, Scotland",\n  "format": "celsius",\n  "num_days": 5\n}"
    }
    """
)
