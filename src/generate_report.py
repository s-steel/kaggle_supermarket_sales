import sqlite3
import pandas as pd

def generate_report(database_path: str, output_csv_path: str) -> None:
    try:
        conn = sqlite3.connect(database_path)
        print('Connected to database successfully.')

        # SQL query: Total sales by branch and product line
        query = """
        SELECT 
            c.city,
            c.customer_type,
            p.product_line,
            SUM(s.total) AS total_sales,
            RANK() OVER (PARTITION BY c.city ORDER BY SUM(s.total) DESC) AS rank
        FROM 
            sales s
        JOIN 
            customers c ON s.customer_id = c.customer_id
        JOIN 
            products p ON s.product_id = p.product_id
        GROUP BY 
            c.city, c.customer_type, p.product_line
        ORDER BY 
            c.city, rank;
        """

        report_df = pd.read_sql_query(query, conn)

        report_df.to_csv(output_csv_path, index=False)
        print(f'Report saved to {output_csv_path}')

    except FileNotFoundError as e:
        raise FileNotFoundError(f'Database not found at {database_path}. Ensure the path is correct.') from e
    except sqlite3.DatabaseError as e:
        raise sqlite3.DatabaseError('Error occurred while querying the SQLite database.') from e
    finally:
        if conn:
            conn.close()
