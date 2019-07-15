import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs, eigsh

#Definition of important constants
OMEGA = np.exp(2*np.pi*1j/3.)
OMEGA_CON = np.exp(-2*np.pi*1j/3.)

#Definition of matrices \sigma and \tau that satisfy \sigma.\tau=OMEGA \tau.sigma
# and their conjugates
sigma        = sparse.csr_matrix(np.array([[0,1,0],[0,0,1],[1,0,0]]))
sigma_dagger = sparse.csr_matrix(np.array([[0,0,1],[1,0,0],[0,1,0]]))
tau          = sparse.csr_matrix(np.array([[1,0,0],[0,OMEGA,0],[0,0,OMEGA_CON]]))
tau_dagger   = sparse.csr_matrix(np.array([[1,0,0],[0,OMEGA_CON,0],[0,0,OMEGA]]))

#Definition of nearest neighbor interaction
XX_dag  = sparse.kron(sigma,sigma_dagger)
X_dag_X = sparse.kron(sigma_dagger,sigma)
YY_dag  = sparse.kron(sigma.dot(tau),tau_dagger.dot(sigma_dagger))
Y_dag_Y = sparse.kron(tau_dagger.dot(sigma_dagger),sigma.dot(tau))
ZZ_dag  = sparse.kron(sigma.dot(tau_dagger),tau.dot(sigma_dagger))
Z_dag_Z = sparse.kron(tau.dot(sigma_dagger),sigma.dot(tau_dagger))

Identity    = lambda i: sparse.identity(i)S

#Definition of N site Hamiltonian (Open boundary conditions)
def Hamiltonian(N,t_perp):
    #Operators in the full Hilbert space
    
    Full_X      = lambda i: sparse.kron(Identity(3**i),sparse.kron(sigma,Identity(3**(N-1-i))))
    Full_Y      = lambda i: sparse.kron(Identity(3**i),sparse.kron(sigma.dot(tau),Identity(3**(N-1-i))))
    Full_Z      = lambda i: sparse.kron(Identity(3**i),sparse.kron(sigma.dot(tau_dagger),Identity(3**(N-1-i))))

    Full_X_dag  = lambda i: sparse.kron(Identity(3**i),sparse.kron(sigma_dagger,Identity(3**(N-1-i))))
    Full_Y_dag  = lambda i: sparse.kron(Identity(3**i),sparse.kron(tau_dagger.dot(sigma_dagger),Identity(3**(N-1-i))))
    Full_Z_dag  = lambda i: sparse.kron(Identity(3**i),sparse.kron(tau.dot(sigma_dagger),Identity(3**(N-1-i))))

    Full_XX_dag  = lambda i: sparse.kron(Identity(3**i),sparse.kron(XX_dag,Identity(3**(N-2-i))))
    Full_X_dag_X = lambda i: sparse.kron(Identity(3**i),sparse.kron(X_dag_X,Identity(3**(N-2-i))))
    Full_YY_dag  = lambda i: sparse.kron(Identity(3**i),sparse.kron(YY_dag,Identity(3**(N-2-i))))
    Full_Y_dag_Y = lambda i: sparse.kron(Identity(3**i),sparse.kron(Y_dag_Y,Identity(3**(N-2-i))))
    Full_ZZ_dag  = lambda i: sparse.kron(Identity(3**i),sparse.kron(ZZ_dag,Identity(3**(N-2-i))))
    Full_Z_dag_Z = lambda i: sparse.kron(Identity(3**i),sparse.kron(Z_dag_Z,Identity(3**(N-2-i))))
    Hamiltonian_int  = sparse.csr_matrix((3**N,3**N))
    Hamiltonian_0    = sparse.csr_matrix((3**N,3**N))
    
#Interaction Hamiltonian
    for i in range(0,N-1):
        Hamiltonian_int +=  Full_XX_dag(i)+Full_X_dag_X(i)+Full_YY_dag(i)+Full_Y_dag_Y(i)+Full_ZZ_dag(i)+Full_Z_dag_Z(i)

#t_perp Hamiltonian (t_perp is measured in units of t^2/2U)
    for i in range(0,N):
        Hamiltonian_0 += t_perp/(3*np.sqrt(2))*(2*(Full_X(i)+Full_X_dag(i))-Full_Y(i)-Full_Y_dag(i)-Full_Z(i)-Full_Z_dag(i))
    
    return Hamiltonian_0+Hamiltonian_int
from scipy.sparse.linalg import eigs, eigsh
with open("lowest_eigenvalues.txt", "w") as out_file:
    for N in range(10,11):
        evals_large, evecs_large = eigsh(Hamiltonian(N,0.2), 80, which='LM')
        out_file.write("N=%d\n" % N)
        np.savetxt(out_file,np.sort(evals_large)[0:40],delimiter=',')
        out_file.write("\n")
