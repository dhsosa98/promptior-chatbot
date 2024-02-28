from typing import List

# This is a function that have the purpose of refining the data from a text source file.
# It can be used to remove unwanted characters, split the text into a list of strings, etc.
# But for now, it just split the text into a list of strings.
def refine_text_data(data: str) -> List[str]:
    data.split('----')
    return data

    