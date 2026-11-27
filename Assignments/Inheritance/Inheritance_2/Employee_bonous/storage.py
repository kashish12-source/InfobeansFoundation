import pickle

def store_data(data):
    with open("employee.pkl",'a+b') as f:

        pickle.dump(data,f)
        print("Data added successfully")

def fetch_data():
    try: 
        with open("employee.pkl" , "rb") as f:
            while True:
                data = pickle.load(f)
                print(data)
    except EOFError as e:
        print("End of file .........")
    except OSError as e :
        print(e)