
DELIMITER = ";"

def TIMESTAMP():
    timestamp = {}
    return timestamp

def readTimestamps(filepath, timestamps):
    filehandler = open(filepath, "r")
    filehandler.readline()

    for line in filehandler:
        line = line.rstrip("\n")
        if line != "":
            columns = line.split(DELIMITER)
            timestamp = TIMESTAMP()
            timestamp["weekday"] = columns[0]
            timestamp["hour"] = int(columns[1])
            timestamp["consumption"] = float(columns[2])
            timestamp["price"] = float(columns[3])
            timestamps.append(timestamp)

    filehandler.close()

def displayTimestamps(timestamps):
    print("Electricity usage:")
    for line in timestamps:
        total = line["price"] * line["consumption"]
        print(f'- {line["weekday"]} {line["hour"]:02d}:00, price {line["price"]:.2f} €, consumption {line["consumption"]:.2f} kWh, total {total:.2f} €')

def main():
    print("Program starting.")
    timestamps = []
    filepath = input("Insert filename:")
    print(f'Reading file "{filepath}".')
    readTimestamps(filepath, timestamps)
    displayTimestamps(timestamps)
    print("Program ending.")

if __name__ == "__main__":
    main()
