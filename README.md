
# Visibility Graphs in Python


Different implementations for computing the natural visibility graph (NVG) \[1\]
and the horizontal visibility graph (HVG) \[2\].
Here we only implement the undirected graphs versions.
For the original implementation in Fortran 90/94 of both directed and undirected
versions, please refer to \[3\].

Here we can find three different implementations to compute the NVG and HVG
of a given series of numbers:


	In " visibility_algorithms.py " :

		1. The original implementation proposed in [3]
		2. A divide and conquer (D&C) approach presented in [4]

	In "node_class.py" :

		3. Our new efficient method (BST) to compute visibility graphs (method "visibility")[5]

In the " example.py "  file one can find an example of how to call the different visibility graphs functions
and compare their computation time.


## About the paper "Online visibility graphs: Encoding visibility in a binary search tree"


All the code related to [this](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.2.023069) paper and necessary to run the experiments is available here.
The names of the python scripts are self-explanatory. For example,
run_exp01.py relates to the first experiment described in the paper and its results (results_exp01.csv), included in the
folder "results", can be displayed with plot_exp01_Figure04.py.


## References

\[1\]:"From time series to complex networks: the visibility graph"
 	Lucas Lacasa, Bartolo Luque, Fernando Ballesteros, Jordi Luque, Juan C. Nuno
 	PNAS, vol. 105, no. 13 (2008) 4972-4975

\[2\]:"Horizontal visibility graphs: exact results for random time series"
	Bartolo Luque, Lucas Lacasa, Jordi Luque, Fernando J. Ballesteros
	Physical Review E 80, 046103 (2009)

\[3\]: http://www.maths.qmul.ac.uk/~lacasa/Software.html

\[4\]:"Fast transformation from time series to visibility graphs"
	Xin Lan, Hongming Mo, Shiyu Chen, Qi Liu, and Yong decending
	Chaos 25, 083105 (2015); doi: 10.1063/1.4927835

\[5\]: "Online visibility graphs: Encoding visibility in a binary search tree"
 Delia Fano Yela, Florian Thalmann, Vincenzo Nicosia, Dan Stowell and Mark Sandler,
 Physical Review Research, (2020) : https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.2.023069
 
**If you use this work for your research please cite:**
```
 @article{fanoyela20,
  title = {Online visibility graphs: Encoding visibility in a binary search tree},
  author = {Fano Yela, Delia and Thalmann, Florian and Nicosia, Vincenzo and Stowell, Dan and Sandler, Mark},
  journal = {Phys. Rev. Research},
  volume = {2},
  issue = {2},
  pages = {023069},
  numpages = {9},
  year = {2020},
  month = {Apr},
  publisher = {American Physical Society},
  doi = {10.1103/PhysRevResearch.2.023069},
  url = {https://link.aps.org/doi/10.1103/PhysRevResearch.2.023069}
}
```



#### AUTHOR: Delia Fano Yela
#### DATE:  April 2020
#### CONTACT: d.fanoyela@qmul.ac.uk and most recently : delia.fano.yela@ri.se

## Disclaimer:
The author takes no responsability for this code. The code is checked for bugs but the author gives no guarantees there will be none left. The code has been optimised up to the necessary point for a research study.
