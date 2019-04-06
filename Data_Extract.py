import csv

DATE_ID = 0
TZ_ID = 1
PRESSURE_ID = 2


def readToList():

    # Open data file and read it
    with open('data.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # Store csv data as a list
        csvData = list(reader)
        # Check if format is valid
        dataCeck = ['Timestamp', 'TZ', 'Pressure (bar)']
        # Check if csv file is correct
        if not dataCeck == csvData[0]:
            print("ERROR has occured.")
            print("REASON: File format is either wrong or file is empty.")
            print("Please double check if provided csv file is correct.")
            exit(0)

    csvFile.close()
    # Return csv data as a list
    return csvData


def exportData(csvData, startTime, endTime):

    startIndex = 0
    endIndex = 0

    for data in csvData:
        if data[0].startswith(startTime):
            startIndex = csvData.index(data)
            print(startIndex)
            break

    for data in csvData:
        if data[0].startswith(endTime):
            endIndex = csvData.index(data)
            print(endIndex)
            break

    if not startIndex or not endIndex:
        print("ERROR: Time frame specified is incorrect.")
        print("Double check you specified start and end time correctly.")
        exit(0)

    tmpData = [['Timestamp', 'TZ', 'Pressure (bar)']]
    tmpData.extend(csvData[startIndex:endIndex])

    with open('tmpData.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(tmpData)



if __name__ == "__main__":

    running = 'y'

    while running in 'y':
        csvData = readToList()

        print("-----------------------------------------------")
        print("We found data from {} to {}".format(csvData[1][DATE_ID], csvData[-1][DATE_ID]))
        print("Specify time period you want data for.")
        print("You can enter just date in format 'YYYY/MM/DD' if you just want daily data")
        print("or you can enter more specific time in format 'YYYY/MM/DD HH:MM'")
        startTime = input("Enter start time: ")
        endTime = input("Enter end time: ")

        print("--------------------------")
        print("You selected time period from {} to {}".format(startTime, endTime))

        exportData(csvData, startTime, endTime)

        running = input("Press y to go again: ")

    exit(0)