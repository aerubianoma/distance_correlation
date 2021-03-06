import sys
from Linked_list import *
sys.path.append("..")
from lib.lib import *
class Distance_correlation_list():
    def __init__(self):
        # Cuando se instancie el objeto, se deben cargar estos vectores usando la clase anterior
        self.x = LinkedList()
        self.y = LinkedList()
        # Matrices de distancias
        self.matrix_distances_x = LinkedList();
        self.matrix_distances_y = LinkedList();
        # Promedios a calcular de estas matrices
        self.row_average_x = LinkedList();
        self.column_average_x = LinkedList();
        self.total_average_x = 0.;
        self.row_average_y = LinkedList();
        self.column_average_y = LinkedList();
        self.total_avergae_y = 0.;
        # Matrices usadas para calcular la distancia de covariancia
        self.A = LinkedList();
        self.B = LinkedList();
        # Valores necesarios para calcular la distancia de correlacion
        self.distance_covariance_x_y = 0.;
        self.distance_covariance_x_x = 0.;
        self.distance_covariance_y_y = 0.;
        self.distance_correlation = 0.;
    # Se llena la matriz de distancias
    def fillDistanceMatrix(self,n):
        fillMatrixZero(self.matrix_distances_x,n);
        fillMatrixZero(self.matrix_distances_y,n);
        current_distances_x = self.matrix_distances_x.head;
        current_distances_y = self.matrix_distances_y.head;
        current_x = self.x.head;
        current_y = self.y.head;
        for i in range(n):
            current_2_distances_x = current_distances_x.getData().head;
            current_2_distances_y = current_distances_y.getData().head;
            current_2_x = self.x.head;
            current_2_y = self.y.head;
            for j in range(n):
                current_2_distances_x.setData(np.linalg.norm(current_x.getData()-current_2_x.getData()));
                current_2_distances_y.setData(np.linalg.norm(current_y.getData()-current_2_y.getData()));
                current_2_distances_x = current_2_distances_x.getNext();
                current_2_distances_y = current_2_distances_y.getNext();
                current_2_x = current_2_x.getNext()
                current_2_y = current_2_y.getNext()        
            current_distances_x = current_distances_x.getNext();
            current_distances_y = current_distances_y.getNext();
            current_x = current_x.getNext();
            current_y = current_y.getNext();
    # Se calculan los promedios de las matrices anteriores
    def generateAditionalValues(self,n):
        current_distances_x = self.matrix_distances_x.head;
        current_distances_y = self.matrix_distances_y.head;
        for i in range(n):
            count_x = 0;
            count_y = 0;
            current_2_distances_x = current_distances_x.getData().head;
            current_2_distances_y = current_distances_y.getData().head;
            for j in range(n):
                count_x += current_2_distances_x.getData()
                count_y += current_2_distances_y.getData()
                current_2_distances_x = current_2_distances_x.getNext();
                current_2_distances_y = current_2_distances_y.getNext();
            self.row_average_x.append(count_x/n);
            self.column_average_x.append(count_x/n);
            self.row_average_y.append(count_y/n);
            self.column_average_y.append(count_y/n);
            current_distances_x = current_distances_x.getNext();
            current_distances_y = current_distances_y.getNext();
        current_row_x = self.row_average_x.head;
        current_row_y = self.row_average_y.head;
        for i in range(n):
            count_x = 0;
            count_y = 0;
            current_2_row_x = self.row_average_x.head;
            current_2_row_y = self.row_average_y.head;
            for j in range(n):
                count_x += current_2_row_x.getData();
                count_y += current_2_row_y.getData();
                current_2_row_x = current_2_row_x.getNext();
                current_2_row_y = current_2_row_y.getNext();
            self.total_average_x = count_x/n;
            self.total_average_y = count_y/n;
            current_row_x = current_row_x.getNext();
            current_row_y = current_row_y.getNext();
    # Se rellena la matriz a usar para calcular la distancia de covarianza
    def fillCenteredMatrix(self,n):
        fillMatrixZero(self.A,n);
        fillMatrixZero(self.B,n);
        current_A = self.A.head;
        current_B = self.B.head;
        current_distances_x = self.matrix_distances_x.head;
        current_distances_y = self.matrix_distances_y.head;
        current_row_x = self.row_average_x.head;
        current_row_y = self.row_average_y.head;
        current_column_x = self.column_average_x.head;
        current_column_y = self.column_average_y.head;
        for i in range(n):
            current_2_A = current_A.getData().head;
            current_2_B = current_B.getData().head;
            current_2_distances_x = current_distances_x.getData().head;
            current_2_distances_y = current_distances_y.getData().head;
            for j in range(n):
                current_2_A.setData(current_2_distances_x.getData() - current_row_x.getData() - current_column_x.getData() + self.total_average_x);
                current_2_B.setData(current_2_distances_y.getData() - current_row_y.getData() - current_column_y.getData() + self.total_average_y);
                current_2_A = current_2_A.getNext()
                current_2_B = current_2_B.getNext() 
                current_column_x = current_column_x.getNext();
                current_column_y = current_column_y.getNext();
                current_2_distances_x = current_2_distances_x.getNext();
                current_2_distances_y = current_2_distances_y.getNext();
            current_A = current_A.getNext();
            current_B = current_B.getNext();
            current_row_x = current_row_x.getNext();
            current_row_y = current_row_y.getNext();
            current_distances_x = current_distances_x.getNext();
            current_distances_y = current_distances_y.getNext();
            current_column_x = self.column_average_x.head;
            current_column_y = self.column_average_y.head;
    # Se calculan las distancia de covarianza 
    def calculateDistanceCovariance(self,n):
        current_A = self.A.head;
        current_B = self.B.head;
        for i in range(n):
            current_2_A = current_A.getData().head;
            current_2_B = current_B.getData().head;
            for j in range(n):
                self.distance_covariance_x_y +=  (current_2_A.getData())*(current_2_B.getData());
                self.distance_covariance_x_x +=  (current_2_A.getData())**2;
                self.distance_covariance_y_y +=  (current_2_B.getData())**2;
                current_2_A = current_2_A.getNext()
                current_2_B = current_2_B.getNext() 
            current_A = current_A.getNext();
            current_B = current_B.getNext();
        self.distance_covariance_x_y = self.distance_covariance_x_y*(1/n**2);
        self.distance_covariance_x_x = self.distance_covariance_x_x*(1/n**2);
        self.distance_covariance_y_y = self.distance_covariance_y_y*(1/(n**2));
    # Se calcula la distancia de correlacion
    def calculateDistanceCorrelation(self,n):
        self.fillDistanceMatrix(n);
        self.generateAditionalValues(n);
        self.fillCenteredMatrix(n);
        self.calculateDistanceCovariance(n);     
        if self.distance_covariance_x_x*self.distance_covariance_y_y != 0:
            self.distance_correlation = math.sqrt((self.distance_covariance_x_y)/(math.sqrt(self.distance_covariance_x_x*self.distance_covariance_y_y)));
        else:
            self.distance_correlation = 0;
        print("The distance correlation is: "+str(self.distance_correlation));
