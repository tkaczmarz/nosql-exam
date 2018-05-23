from matplotlib import pyplot as plt


def read_data(filename, keys=["Primary_Type", "value"]):
    with open(filename, "r") as file:
        documents = [[], []]
        file.readline()  # skip separator line
        for line in file:
            values = line.split(",")
            documents[0].append(values[0])
            documents[1].append(values[1])
        return documents


def generate_bar_chart():
    plt.bar(data[0], data[1])
    plt.xlabel("Type of crime")
    plt.ylabel("Amount of crimes commited")
    plt.savefig("./static/mapreduce1.png")


def generate_charts():
    pass


if __name__ == "__main__":
    data = read_data("crimes-mr.csv")
    data[0] = data[0][-5:]
    data[1] = data[1][-5:]
    print(data)
    generate_bar_chart()
