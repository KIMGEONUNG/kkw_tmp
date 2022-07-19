__all__ = ['get', 'load']
import pickle


def save(obj, path="my_data.pkl"):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)
        # f.write(data)


def load(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
        return data

if __name__ == '__main__':
    import numpy as np
    a  = np.random.randn(10)
    save(a, "./here.pkl")
    b = load("./here.pkl")
    print(a)
    print(b)
