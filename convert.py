import pandas as pd

def convert():
    print("Converting Employee-List.xlsx to employees.csv using pandas...")
    # Read the excel file
    df = pd.read_excel('Employee-List.xlsx')
    
    # Save it directly to CSV without the pandas index
    df.to_csv('employees.csv', index=False)
    print("Conversion complete!")

if __name__ == '__main__':
    convert()
