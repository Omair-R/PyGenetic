# PyGenetic
PyGenetic is a small project that I created to develop a better understanding of genetic algorithms, after all you can't code something you don't understand. I wanted to stop at the most basic implementation for the algorithm, but I grew to love it, and decided to explore further. The project is still greatly under developement with many features remine unfinished, some of which are: 
- String handling. 
- more crossover methods. 
- error handling and testing (I should have done them earlier I know XD)
- visualization. 
- ... and lot more that I might get to later. 

## usage: 
the project is not a pip package, and I am not sure if it ever will be, but you can simply clone the repository. then do something similar to: 

### optimization problem
``` python
import numpy as np
from PyGenetic import genetic_algorithms as pg

function_inputs = [4, -2, 3.5, 0.5, -10, -4.7]

desired_output = 69


def fitness_func(solution):

    output = np.sum(solution * function_inputs)
    fitness = 1.0 / (np.abs(output - desired_output) + 0.000000001)

    return fitness


ga = pg.GA(fitness_function=fitness_func,
           n_generations=100,
           n_genes=6,
           n_pool=100,
           n_parents=25,
           low_boundery=-2,
           high_boundery=5,
           mutation_prop=0.6,
           crossover_type="uniform",
           mutation_type = "swap")

solution, fitness = ga.run(verbose=True)

output = np.sum(solution * function_inputs)

print(
    f"best parent is: {solution}\nwith fitness score of {fitness} \nsolution: {output}"
)
```
### feature selection (binary)
``` python
from PyGenetic import genetic_algorithms as pg
import numpy as np
import pandas as pd


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer


cancer=load_breast_cancer()

df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
label=cancer["target"]

X_train, X_test, y_train, y_test = train_test_split(df, 
                                                    label, test_size=0.30, 
                                                    random_state=101)

logmodel = SVC()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)

print("Initail Accuracy = "+ str(accuracy_score(y_test,predictions)))

def fitness_func(solution):

    logmodel.fit(X_train.loc[:,solution],y_train)
    predictions = logmodel.predict(X_test.loc[:,solution])
    return accuracy_score(y_test,predictions)


ga = pg.GA(fitness_function=fitness_func,
           n_generations=50,
           n_genes=30,
           n_pool=100,
           n_parents=50,
           mutation_prop=0.2,
           crossover_type="uniform",
           mutation_type = "bit_flip",
           population_type = "binary")

solution, fitness = ga.run(verbose=True)

print(f"best features are: {list(df.columns[solution])} \n with an accuracy of {fitness}")

```
## requirements:
pretty much just numpy, I am using numpy==1.18.5
