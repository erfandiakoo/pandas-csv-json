import pandas as pd
import re
import unicodedata

def remove_unicode_and_invisible(text):
    if isinstance(text, str):
        cleaned_text = ''.join(char for char in text if unicodedata.category(char)[0] != 'C')
        cleaned_text = re.sub(r'[\s\?]+', ' ', cleaned_text)
        return cleaned_text.strip()
    else:
        return str(text)

df = pd.read_csv('yourfile.csv', encoding='UTF-8')

df = df.applymap(remove_unicode_and_invisible)

table_name = 'table_name'

sql_statements = []

for index, row in df.iterrows():
    columns = ', '.join(row.index)
    values = ', '.join([f"'{str(value).replace('\'', '\'\'')}'" if isinstance(value, str) else str(value) for value in row.values])
    sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    sql_statements.append(sql_statement)

with open('output.sql', 'w') as f:
    for statement in sql_statements:
        f.write(statement + '\n')

print("SQL statements have been written to 'output.sql'")
