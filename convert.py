import pandas as pd

def convert():
    print("Converting Excel files to CSV using pandas...")
    
    # 1. Convert current employee list
    df_employees = pd.read_excel('Employee-List.xlsx')
    df_employees.to_csv('employees_list.csv', index=False)
    print("Successfully created employees_list.csv")
    
    # 2. Convert previous year's assignments
    df_previous = pd.read_excel('Secret-Santa-Game-Result-2023.xlsx')
    df_previous.to_csv('secret_santa_game_result_2023.csv', index=False)
    print("Successfully created secret_santa_game_result_2023.csv")

if __name__ == '__main__':
    convert()
