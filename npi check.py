import pandas as pd

# Assuming df and cld_file are already defined
# Example DataFrame
data = {'STATE': ['CT', 'MS', 'CA', 'NY', 'TX', 'CT'],
        'PROVIDER_ID_(NPI)': ['NPI 12345', 'NPI 67890', 'NPI 11223', 'NPI 44556', 'NPI 77889', 'NPI 99001']}
df = pd.DataFrame(data)

# Example cld_file (assuming it also has a 'STATE' column, or you're checking against a list)
cld_file_states = ['MS', 'CA', 'TX', 'CT']

# Create a list of states where the replacement should happen
states_to_modify = ['CT', 'MS', 'CA', 'TX']

# Use .isin() and boolean indexing to select rows and apply str.replace()
df.loc[df['STATE'].isin(states_to_modify), 'PROVIDER_ID_(NPI)'] = \
    df.loc[df['STATE'].isin(states_to_modify), 'PROVIDER_ID_(NPI)'].str.replace('NPI ', '')

# Print the modified DataFrame
print(df)
