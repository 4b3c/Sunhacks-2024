import pickle


with open('user.pkl', 'rb') as file:
                user = pickle.load(file)
print(user)