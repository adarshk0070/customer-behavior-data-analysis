import pandas as pd
from sqlalchemy import create_engine, text
import re
import os

def main():
    print("Step 1: Loading Data...")
    if not os.path.exists('customer_shopping_behavior.csv'):
        print("Error: customer_shopping_behavior.csv not found.")
        return

    df = pd.read_csv('customer_shopping_behavior.csv')
    print(f"Loaded {len(df)} rows.")

    print("Step 2: Data Cleaning...")
    # Imputing missing values in Review Rating
    if 'Review Rating' in df.columns:
        df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

    # Renaming columns
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ','_')
    df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

    # Create age_group
    labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
    df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
    
    # Drop promo_code_used
    if 'promo_code_used' in df.columns:
        df = df.drop('promo_code_used', axis=1)

    print("Step 3: Loading into Database (SQLite)...")
    # Using SQLite for guaranteed execution
    db_path = 'customer_behavior.db'
    engine = create_engine(f'sqlite:///{db_path}')
    
    # Store 'age_group' as string because SQLite doesn't support categorical types well via to_sql sometimes
    df['age_group'] = df['age_group'].astype(str)
    
    df.to_sql('customer', engine, if_exists='replace', index=False)
    print(f"Data loaded into 'customer' table in {db_path}")

    print("Step 4: Executing SQL Analysis...")
    if not os.path.exists('customer_behavior_sql_queries.sql'):
        print("Error: customer_behavior_sql_queries.sql not found.")
        return

    with open('customer_behavior_sql_queries.sql', 'r') as f:
        sql_content = f.read()

    # Clean SQL for SQLite
    # Remove ::numeric for SQLite compatibility
    sql_content = sql_content.replace('::numeric', '')
    
    # Extract queries and comments
    # We want to separate queries but maybe keep context?
    # Simple approach: Split by ; and run non-empty strings
    
    # First, let's remove comments to avoid issues with split
    # Be careful not to remove comments inside strings (unlikely here)
    # Using regex to remove -- comments
    lines = sql_content.split('\n')
    clean_lines = []
    for line in lines:
        # Remove comment part
        line_code = line.split('--')[0]
        clean_lines.append(line_code)
    
    clean_sql = '\n'.join(clean_lines)
    
    queries = [q.strip() for q in clean_sql.split(';') if q.strip()]
    
    with engine.connect() as conn:
        for i, query in enumerate(queries, 1):
            print(f"\n--- Running Query {i} ---")
            print(f"SQL: {query[:100].replace(chr(10), ' ')}...")
            
            try:
                result = pd.read_sql_query(text(query), conn)
                print(result)
            except Exception as e:
                print(f"Error running query: {e}")

    print("\nProject run completed successfully.")

if __name__ == "__main__":
    main()
