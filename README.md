# Parafermions
Exact Diagonalization of Parafermion model in high energy limit

The file Exact_Diagonalization_Parafermions.py contains the code that defines the Hamiltonian H of the three leg
spinless electron system at filling 1/3 and in the large interleg interaction limit. The code also performs exact diagonalization
of the system. I use an offset in the Hamiltonian, such that the routine eighs gives only the lowest 40 eigenvalues. This offset is 
H - 100*Id, where Id has the dimension of the Hilbert space.

The file ED_Parafermions_Fendley.py defines a generalization of the Parafermion model defined by Fendley in 
https://arxiv.org/abs/1209.0472. (Note that the definition of \sigma and \tau is interchanged in the code, so \tau is the diagonal 
operator). This generalization is given by J_x X_i X_{i+1}^\dagger + J_y Y_i Y_{i+1}^\dagger+ J_z Z_i Z_{i+1}^\dagger+ h.c. where
X =\sigma, Y=\sigma\tau and Z=\sigma\tau^\dagger and returns the lowest 40 eigenvalues for different system sizes.

The File Degeneracy_GS.py is used to plot the results obtained from Exact_Diagonalization_Parafermions.py and 
ED_Parafermions_Fendley.py. It receives the data files to be plot from the terminal. It receives 25 files.
