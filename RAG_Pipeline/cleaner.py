import re

def clean_text(document):

    """
    Clean text by removing tabs, extra spaces.
    """

    # Replace tabs with a space
    document['text'] = re.sub(r"\t+"," ",document['text'])

    # Remove extra blank lines
    document['text'] = re.sub(r"\n\s*\n+","\n\n",document['text'])

    # Remove spaces at the beginning and end
    document['text'] = document['text'].strip()

    return document















