
DELIMITER = ";"

def insert():
    timestamps = []
    file = input("Insert filename:")
    filehandler = open(file, "r")
    print(f'Reading file "{file}".')
    filehandler.readline()

    for line in filehandler:
        line = line.rstrip("\n")
        if line != "":
            columns = line.split(DELIMITER)
            timestamp = {}
            timestamp["weekday"] = columns[0]
            timestamp["hour"] = int(columns[1])
            timestamp["consumption"] = float(columns[2])
            timestamp["price"] = float(columns[3])
            timestamps.append(timestamp)

    filehandler.close()
    return timestamps

def display(timestamps):
    print("Electricity usage:")
    for line in timestamps:
        total = line["price"] * line["consumption"]
        print(f'- {line["weekday"]} {line["hour"]:02d}:00, price {line["price"]:.2f} €, consumption {line["consumption"]:.2f} kWh, total {total:.2f} €')

def main():
    print("Program starting.")
    file = insert()
    display(file)
    print("Program ending.")

if __name__ == "__main__":
    main()
