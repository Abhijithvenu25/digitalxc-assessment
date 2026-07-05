import argparse
import sys
import logging
from secret_santa.io_handlers import CSVHandler
from secret_santa.assigner import SecretSantaAssigner
from secret_santa.exceptions import SecretSantaError

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Acme Secret Santa Assignment System")
    parser.add_argument("input_file", help="Path to the input CSV file containing employees")
    parser.add_argument("output_file", help="Path to save the generated assignments CSV file")
    parser.add_argument("--previous", help="Path to the previous year assignments CSV file", default=None)
    
    args = parser.parse_args()
    
    try:
        # Utilize the CSVHandler object instance
        io = CSVHandler(args.input_file, args.output_file, args.previous)
        
        employees = io.read_employees()
        logging.info(f"Loaded {len(employees)} employees.")
        
        previous = io.read_previous_assignments()
        if previous:
            logging.info(f"Loaded {len(previous)} previous assignments.")
            
        # Utilize the SecretSantaAssigner object instance
        assigner = SecretSantaAssigner(employees, previous)
        assignments = assigner.generate_assignments()
        
        io.write_assignments(assignments)
        logging.info(f"Successfully generated assignments in {args.output_file}!")
        
    except SecretSantaError as e:
        logging.error(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
