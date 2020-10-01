# A Longitudinal Exploratory Study on the Impact of Refactoring in Android Application: Replication Package (IST 2020)
This repository contains all the material required to replicate our analysis, including (i) the raw input data (ii) the statistical analysis scripts, and (iii) the analysis results in form of data, plots, etc.



Data collection
---------------
The data used for this study can be obtained by executing the scripts available in Scripts Folder: 

* Repodriller : RepoDriller is a Java framework that helps developers on mining software repositories. With it, we extracted Commits ([Availaible here](https://github.com/mauricioaniche/repodriller)).
* RefactoringMiner: RefactoringMiner is a library/API written in Java that can detect refactorings applied in the history of a Java project ([Availaible here](https://github.com/tsantalis/RefactoringMiner))
* Checkout_commits.py: checkouts commits before and after each applied refactoring.
* SeparateCommit.py: Splits all_refactorings files (Results of RefactoringMiner) to multiple csv files and each one contains details of a single commit. 
* CalculRefactoring.py: Calculates the number of refactoring operations in each class.  
* aDoctor.py: Detects Android smells.
* Organic.py: Detects Object Oriented smells.
* Organic_JSON.to.CSV.py: Parses JSON files (returns of Organic) and converts them to CSV files.
* Calcul_diff_smells.py: Calculates the difference in smells before and after each refactoring commit.
* Ck-metrics.py: Calculates quality metrics.
* Calcul_diff_metrics.py: Calculates the difference in quality metrics before and after each refactoring commit.
* Merge.py: Merges CSV files. 
* AssociationMiningRule.py: Calculates support, confidence, lift, leverge and conviction.

Analysis replication
---------------
The totality of the statistical analysis scripts utilized for the study are available in Analysis_scripts folder: 

* RQ2-3_analysis.R: Performs all analysis related to RQ2 and RQ3.
* RQ4_analysis.R: Performs all analysis related to RQ4.
* RQ4_analysis_plots.R: Performs all analysis and plots results related to RQ4.

Raw input Data
---------------
The raw input data utilized for the analysis is available in Data folder where we found commits Data in the commits Folder, the list of refactorings, traditional
OO smells, Android smells, Quality metrics values before and after the application of refactoring in DataApps and the data for the first question in the DataForLastVersion folder.

Results and plots
---------------
The results produced in order to answer our research questions are provided in results folder. The totality of the results and plots generated during the analysis processes are provided.
