import numpy as np


def sigmoid(x):
    ## fonction d'activation sigmoide f(x)= 1/(1+e^(-x))
    return 1/(1 + np.exp(-x)) 

def deriv_sigmoid(x): 
    # f'(x) = f(x)*( 1 - f(x))
    fx = sigmoid(x)
    return fx* (1 - fx)

def mse_loss(y_true, y_pred):
  # y_true and y_pred are numpy arrays of the same length.
  return ((y_true - y_pred) ** 2).mean()
#definition d un neurone comme une classe de membre : weights , bias 
class Neuron : 
    def __init__(self , weights, bias):
        self.weights = weights
        self.bias = bias 

    def feedforward(self , inputs) : 
        #weight inputs , add bias , then use the activation function
        total=np.dot(self.weights,inputs) + self.bias  # c est juste un produit scalaire 
        return sigmoid(total)
    

#teste avec l exemple du cours 
weights = np.array([0, 1])
bias = 4 

n = Neuron(weights , bias)

X = np.array([2, 3])

print(n.feedforward(X)) ## afiche 0.99 sur le terminale 




##coding e Neural Network : Feedforward 

class OurNeuralNetwork: 
    '''
    A neural network with : 
    -2 inputs 
    - a hidden layer with 2 neurons ( h1 , h2)
    -an output layer with 1 neuron (o1)

    Each neuron has the same wight and bias w= [0, 1] , b = 0
    '''
    def __init__(self):
        # Weights
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

    # Biases
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    def feedforward(self, x):
    # x is a numpy array with 2 elements.
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1
    
    def train(self , data, y_trues): 
        '''
        -data est un tableau de dim (n*2) , n = nombre d echantillon
        -y_trues avec n elements '''

        learn_rate = 0.1 # vitesse d entrainement 
        epochs = 1000 # nombre de fois qu'il faut parcourir en boucle l'ensemble des données

        for epoch in range(epochs): 
            for x , y_true in zip(data , y_trues): 
                # faut faire un feedforward
                sum_h1 = self.w1*x[0]+self.w2 * x[1] +self.b1
                h1 =sigmoid(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)
                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                y_pred = o1

                #on calcule les dérivées partielles

                d_L_d_ypred = -2 *( y_true - y_pred)
                
                #neuron o1 
                d_ypred_d_w5 = h1*deriv_sigmoid(sum_o1)

                d_ypred_d_w6 = h2*deriv_sigmoid(sum_o1)
                d_ypred_d_b3 = deriv_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w5*deriv_sigmoid(sum_o1)
                d_ypred_d_h2 =self.w6 *deriv_sigmoid(sum_o1)

                # Neuron h1
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
                d_h1_d_b1 = deriv_sigmoid(sum_h1)


                #neuron h2 

                d_h2_d_w3 = x[0]*deriv_sigmoid(h2)
                d_h2_d_w4 = x[1]*deriv_sigmoid(h2)

                d_h2_d_b2 = deriv_sigmoid(sum_h2)


                #on met a jour les poids et biais 
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                # Neuron h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

                # Neuron o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3
            
            # on peut donc calculer la Loss total a la fin de chaque epoch
            if epochs % 10 == 0 : 
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = mse_loss(y_trues, y_preds)
                print("Epoch %d loss: %.3f" % (epoch, loss))

network = OurNeuralNetwork()
x = np.array([2, 3])
w =np.array([0, 1])
b = 0 

print(network.feedforward(x)) ## affiche 0.72 


## We gonna a Neural Network 

##la fonction loss , importante pour l entrainement 


#def mse_loss( y_true , y_pred):
 #   return ((y_true - y_pred)**2).mean()

#on teste 
#y_true = np.array([1, 0, 0, 1])
#y_pred = np.array([0, 0, 0, 0])

#print( mse_loss(y_true , y_pred)) ## affiche 0.5 


## etape de l 'entrainement 

# teste du reseau entrainé 

#notre data set
data = np.array([
  [-2, -1],  # Alice
  [25, 6],   # Bob
  [17, 4],   # Charlie
  [-15, -6], # Diana
])

all_y_trues = np.array([
  1, # Alice
  0, # Bob
  0, # Charlie
  1, # Diana
])

# Train our neural network!
network = OurNeuralNetwork()
network.train(data, all_y_trues)


# Make some predictions -> predict the gender 0= homme  1 = femme
emily = np.array([-7, -3])
frank = np.array([20, 2]) 
print("Emily: %.3f" % network.feedforward(emily)) # 0.951 - F
print("Frank: %.3f" % network.feedforward(frank)) # 0.039 - M