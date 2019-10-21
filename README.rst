================
C3Pred - Web App
================


Software project of the iGEM Team Tübingen 2019

`Our Wiki
<https://2019.igem.org/Team:Tuebingen/Software/>`_


C3Pred is an easy-to-use software tool, to predict the transport effectivity of cell-penetrating peptides (CPP).  CPPs are short 4-30 amino acids long peptides, which possess the ability to transport different cargo over the cell membrane. These cargos include proteins, nanobodies, DNA molecules, and small molecule drugs. In recent years, numerous promising clinical and pre-clinical trials have been launched, with CPPs as a carrier for pharmacologically active small molecules. C3Pred allows scientists to make design choices for their CPP-utilizing system based on quantitative transport activity scores.

C3Pred accepts three possible input formats for protein data:

* FASTA-formatted sequences
* UniProtKB Accession Number
* iGEM Part ID
C3Pred automatically fetches and parses the information about the given identifiers using the UniProt website REST API or using the iGEM Registry API, respectively.

C3Pred was released as:

* Web application with an intuitive browser-based graphical user interface 
* Python package / Command-line tool 


Live version of our tool:
https://igem-tuebingen.com/c3pred/


The Python package / Command-line tool can be found here:
https://github.com/igemsoftware2019/Tuebingen_c3pred




Installation and Usage
----------------------

Documentation: https://c3pred.readthedocs.io.



Demonstration
-------------

.. image:: https://2019.igem.org/wiki/images/4/4b/T--Tuebingen--c3pred_demo_1.gif
    :alt: demo of c3pred




License
-------

Free software: MIT license

