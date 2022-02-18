import pandas as pd

FILEPATH = "description.csv"

data       = pd.read_csv(FILEPATH)

#dropping the unwanted columns
data.drop("Title", inplace=True, axis=1)

updated_data = data.to_csv("updated.csv", index = False)

def startpy():

    file = open("updated.csv", "r")
    
    # read the file as a list
    data = file.readlines()

    # close the file
    file.close()

    new_data =[]

    for index, item in enumerate(data):
        item = item.replace('\n', ' ')

        if(index % 6 == 0):

            item = str(item) + 'sdi3739djysy'

        new_data.append(item)

    textfile = open("description.txt", "w")
    
    for element in new_data:
         textfile.write(element + "\n ----------------------------------------------------------------------- \n")
    textfile.close()

    return textfile

if __name__ == "__main__":

    startpy()


