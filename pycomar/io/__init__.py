__all__ = ['get', 'load']
import pickle


def save(obj, path="my_data.pkl"):
  with open(path, 'wb') as f:
    pickle.dump(obj, f)
    # f.write(data)


def load(path="my_data.pkl"):
  with open(path, 'rb') as f:
    data = pickle.load(f)
    return data


def hello():
    print('hello world')

if __name__ == '__main__':
  import numpy as np
  a = np.random.randn(10)
  save(a, "./here.pkl")
  b = load("./here.pkl")
  print(a)
  print(b)
