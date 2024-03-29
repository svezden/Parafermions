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

Identity    = lambda i: sparse.identity(i)

#Definition of N site Hamiltonian (Open boundary conditions)
t_perp =0.1
def Hamiltonian(N,y,z):
    #Operators in the full Hilbert space
    
    Full_tau     = lambda i: sparse.kron(Identity(3**i),sparse.kron(tau,Identity(3**(N-1-i))))
    Full_tau_dag = lambda i: sparse.kron(Identity(3**i),sparse.kron(tau_dagger,Identity(3**(N-1-i))))

    Full_XX_dag  = lambda i: sparse.kron(Identity(3**i),sparse.kron(XX_dag,Identity(3**(N-2-i))))
    Full_X_dag_X = lambda i: sparse.kron(Identity(3**i),sparse.kron(X_dag_X,Identity(3**(N-2-i))))

    Full_YY_dag  = lambda i: sparse.kron(Identity(3**i),sparse.kron(YY_dag,Identity(3**(N-2-i))))
    Full_Y_dag_Y = lambda i: sparse.kron(Identity(3**i),sparse.kron(Y_dag_Y,Identity(3**(N-2-i))))

    Full_ZZ_dag  = lambda i: sparse.kron(Identity(3**i),sparse.kron(ZZ_dag,Identity(3**(N-2-i))))
    Full_Z_dag_Z = lambda i: sparse.kron(Identity(3**i),sparse.kron(Z_dag_Z,Identity(3**(N-2-i))))

    Hamiltonian_int  = -100.*Identity(3**N)
    Hamiltonian_0    = -100.*Identity(3**N)
    Hamiltonian_diag = -100.*Identity(3**N)
    
    #Interaction Hamiltonian
    for i in range(0,N-1):
        Hamiltonian_int += -(Full_XX_dag(i)+Full_X_dag_X(i)+y*(Full_YY_dag(i)+Full_Y_dag_Y(i))+z*(Full_ZZ_dag(i)+Full_Z_dag_Z(i)))

    #t_perp Hamiltonian (t_perp is measured in units of t^2/2U)
    for i in range(0,N):
        Hamiltonian_0 += -t_perp*(Full_tau(i)+Full_tau_dag(i))
    
    return Hamiltonian_0+Hamiltonian_int

for i in range(0,25):
    with open("new_XYZ_(1,"+str(0.85+0.05*int(i/5))+","+str(0.2*(i%5))+").txt", "w") as out_file:
        for N in range(5,13):
            evals_large, evecs_large = eigsh(Hamiltonian(N,0.85+0.05*int(i/5),0.2*(i%5)), 41, which='LM')
            out_file.write("N=%d, t_perp=%5.3f \n" % (N,0.1))
            np.savetxt(out_file,np.sort(evals_large)[0:40],delimiter=',')
            out_file.write("\n")
