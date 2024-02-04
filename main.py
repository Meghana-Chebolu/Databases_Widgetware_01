import pandas as pd

def generate_create_table_query(df, table_name, primary_keys):
    columns = []
    for column, dtype in zip(df.columns, df.dtypes):
        sql_dtype = dtype.name
        if 'int' in sql_dtype:
            sql_dtype = 'INT'
        elif 'float' in sql_dtype:
            sql_dtype = 'FLOAT'
        elif 'bool' in sql_dtype:
            sql_dtype = 'BOOLEAN'
        elif 'object' in sql_dtype:
            sql_dtype = 'TEXT'
        columns.append(f"{column} {sql_dtype}")
    primary_key_str = ", ".join(primary_keys)
    columns.append(f"PRIMARY KEY ({primary_key_str})")
    query = f"CREATE TABLE {table_name} (\n"
    query += ",\n".join(columns)
    query += "\n);"
    return query

def generate_copy_query(table_name, column_names, file_path, with_header=True):
    header_option = "HEADER = TRUE" if with_header else "HEADER = FALSE"
    column_names_str = ", ".join(column_names)
    query = f"COPY {table_name} ({column_names_str}) "
    query += f"FROM '{file_path}' "
    query += f"WITH DELIMITER=',' AND {header_option} AND NULL='NA';"
    return query

if __name__ == "__main__":
    # Read CSV file into DataFrame
    file_path = 'sales_data.csv'
    df = pd.read_csv(file_path)

    # Determine primary key columns
    primary_key_columns = []
    for column in df.columns:
        if df[column].nunique() == len(df):
            primary_key_columns.append(column)
            break

    if not primary_key_columns:
        primary_key_columns = df.columns[:2]

    # Get keyspace and table names from user input
    keyspace_name = input("Enter your keyspace name: ")
    table_name = input("Enter table name: ")

    # Combine keyspace and table names
    final_table_name = f"{keyspace_name}.{table_name}"

    # Generate CREATE TABLE query
    create_table_query = generate_create_table_query(df, final_table_name, primary_key_columns)

    # Print the generated CREATE TABLE query
    print("Generated CREATE TABLE query:")
    print(create_table_query)

    # Generate COPY query
    copy_query = generate_copy_query(final_table_name, df.columns, file_path)

    # Print the generated COPY query
    print("\nGenerated COPY query:")
    print(copy_query)
