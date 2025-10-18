import json
import pandas as pd
data = json.load(open("data/grant_opportunities.json"))

dff = pd.json_normalize(data)
print(dff.iloc[0])

# Convert to a pandas DataFrame
df = pd.DataFrame(data)

