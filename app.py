
def add_record(records):
    key = input("Enter name: ").strip()

    if key in records:
        print("Record already exists!")
    else:
        value = input("Enter details: ").strip()
        records[key] = value
        print("Record added successfully!")


def update_record(records):
    key = input("Enter name to update: ").strip()

    if key in records:
        records[key] = input("Enter new details: ").strip()
        print("Record updated successfully!")
    else:
        print("Record not found!")


def search_record(records):
    key = input("Enter name to search: ").strip()

    if key in records:
        print(f"{key}: {records[key]}")
    else:
        print("Record not found!")


def delete_record(records):
    key = input("Enter name to delete: ").strip()

    if key in records:
        del records[key]
        print("Record deleted successfully!")
    else:
        print("Record not found!")


def display_records(records):
    if not records:
        print("No records available.")
    else:
        print("\n--- All Records ---")

        for key, value in records.items():
            print(f"{key}: {value}")


def main():
    records = {}

    while True:
        print("\n===== Python Dictionary Application =====")
        print("1. Add Record")
        print("2. Update Record")
        print("3. Search Record")
        print("4. Delete Record")
        print("5. Display All Records")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_record(records)

        elif choice == "2":
            update_record(records)

        elif choice == "3":
            search_record(records)

        elif choice == "4":
            delete_record(records)

        elif choice == "5":
            display_records(records)

        elif choice == "6":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
