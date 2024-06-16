import csv

def generate_sql_create_table(file_path, table_name):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)

        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"

        for column_name in header:
            column_definition = f"{column_name} VARCHAR,"
            create_table_sql += column_definition + "\n"

        create_table_sql = create_table_sql.rstrip(",\n") + "\n);"

        return create_table_sql

if __name__ == "__main__":
    file_path = './yourfile.csv'  # Replace with the path to your CSV file
    table_name = 'table_name'      # Replace with the name of your database table

    sql_create_table = generate_sql_create_table(file_path, table_name)

    print(sql_create_table)
