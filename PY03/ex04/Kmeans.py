import sys
from csvreader import CsvReader

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        if not isinstance(ncentroid, int) or not isinstance(max_iter, int):
            raise ValueError("max_iter and/or ncentroid are of wrong type")
        if max_iter <= 0 or ncentroid <= 0:
            raise ValueError("Negative or equal to zero parameters")
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []
    
    def fit(self, X):
        pass

    def predict(self, X):
        pass

def main():
    lst = sys.argv[1:]
    if len(lst) != 1 and len(lst) != 2 and len(lst) != 3:
        raise ValueError("Wrong number of arguments")
    else:
        kwlst = {"filepath" : "", "max_iter" : 20, "ncentroid": 4}
        for elem in lst:
            elem = elem.split("=")
            if elem[0] in kwlst:
                kwlst[elem[0]] = elem[1]
        print(kwlst)
        with CsvReader(kwlst["filepath"]) as file:
           data = file.getdata()
        print(data)
    hp = KmeansClustering(kwlst["max_iter"], kwlst["ncentroid"])

if __name__ == "__main__":
    try:
        main()
    except ValueError as err:
        print(err.args)