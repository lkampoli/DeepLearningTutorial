#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Maziar Raissi
"""

import autograd.numpy as np
import matplotlib.pyplot as plt
from VariationalAutoencoders import VariationalAutoencoders
from Utilities import Normalize

np.random.seed(1234)
    
if __name__ == "__main__":
    
    N = 1000
    Y_dim = 2
    Z_dim = 2
    
    layers_encoder = np.array([Y_dim,100,50,Z_dim])
    layers_decoder = np.array([Z_dim,50,100,Y_dim])
        
    # generate synthetic data    
    def f(z):
        return z/10 + z/np.linalg.norm(z,2,axis = 1, keepdims = True)
    
    Z = np.random.randn(N,2)
    Y = f(Z)
    
    Normalize_data = 1
        
    #  Normalize Output Data
    if Normalize_data == 1:
        Y_m = np.mean(Y, axis = 0)
        Y_s = np.std(Y, axis = 0)   
        Y = Normalize(Y, Y_m, Y_s)
    
    # Model creation
    model = VariationalAutoencoders(Y, layers_encoder, layers_decoder, 
                 max_iter = 5000, N_batch = 200, monitor_likelihood = 10, 
                 lrate = 1e-3)
        
    model.train()
        
    mean_star, var_star = model.generate_samples(1000)
    
    plt.figure(figsize=(10,5))
    plt.rcParams.update({'font.size': 14})
    
    plt.subplot(1, 2, 1)
    plt.scatter(Y[:,0], Y[:,1], color='blue')
    plt.xlabel('$y_1$')
    plt.ylabel('$y_2$')
    plt.axis('equal')
    plt.title('Traning Data')
    
    plt.subplot(1, 2, 2)
    plt.scatter(mean_star[:,0], mean_star[:,1], color='red')
    plt.xlabel('$y_1$')
    plt.ylabel('$y_2$')
    plt.axis('equal')
    plt.title('Generated Samples')
    
    plt.tight_layout()
    
    plt.savefig('Example_VAE.eps', format='eps', dpi=1000)
