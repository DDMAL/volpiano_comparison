from urllib.request import urlopen
from io import StringIO
from csv import DictReader

paris15181 = "https://cantus.uwaterloo.ca/sites/default/files/csv/123631.csv"

def obtain(csvSource=paris15181, maxLength=10000):
    """Get a list of volpiano strings.

    Fetch a csv from the cantus database, and extract
    the first maxLength volpiano strings from it."""
    contents = urlopen(csvSource).read().decode("utf8")
    # The DictReader only reads files (not strings)
    contentsF = StringIO(contents)
    csvDict = DictReader(contentsF)
    volpianos = []
    for row in csvDict:
        v = row["volpiano"]
        if v and len(v) <= maxLength:
            volpianos.append(v)
    return volpianos


def validate():
    pass


def compare():
    pass
