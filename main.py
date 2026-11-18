
from dataclasses import dataclass

DELIMITER = ";"

@dataclass
class TIMESTAMP:
    weekday: str
    hour: int
    consumption: float
    price: float

def readTimestamps():
    timestamps = []
    file = input("Insert filename:")
    print(f'Reading file "{file}".')
    filehandler = open(file, "r")
    filehandler.readline()

    for line in filehandler:
        line = line.rstrip("\n")
        if line != "":
            columns = line.split(DELIMITER)
            timestamp = TIMESTAMP(
                columns[0],
                int(columns[1]),
                float(columns[2]),
                float(columns[3])
            )
            timestamps.append(timestamp)

    filehandler.close()
    return timestamps

def displayTimestamps(timestamps):
    print("Electricity usage:")
    for line in timestamps:
        total = line.price * line.consumption
        print(f"- {line.weekday} {line.hour:02d}:00, price {line.price:.2f} €, consumption {line.consumption:.2f} kWh, total {total:.2f} €")

def main():
    print("Program starting.")
    timestamps = readTimestamps()
    displayTimestamps(timestamps)
    print("Program ending.")

if __name__ == "__main__":
    main()
