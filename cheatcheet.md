# cheatsheet



0. Always check with python version and environment you have loaded.

       python --version
       which python


0. To install anaconda with the **install_anaconda3** script:

       ./install_anaconda [-h] [dir=anaconda3] [version=2024.06-1]
       source anaconda3/python_start.sh
      

1. To start the anaconda navigator, from which many things can be loaded

      
       anaconda-navigator


2. Or use their CLI equivalents

       jupyter notebook your_notebook.ipynb
       spyder your_notebook.py



3. Conversion of notebooks to pure python ( *"File -> Download as -> Python (.py)"*
   in the browser environment will also do it)

       jupyter nbconvert --to script your_notebook.ipynb

   you can now exectute it, and run it

       chmod +x your_notebook.py
       ./your_notebook.py

   and not tried yet


        pip install spyder-notebook

6. more to come...
