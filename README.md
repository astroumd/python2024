# python2024

Some notes on python - 2024 style


## Lecture summary

In this hands-on lecture on the Python Ecosystem we will assume you
are already (somewhat) familiar with python. Ideally you will already
have a python environment on your laptop, so you can play along with
the examples, but this is not required.

We will cover

* ipython (briefly)
* the spyder GUI
* Jupyter Notebooks, both running local and remote
* VS Code (if time permits)


A github repo https://github.com/astroumd/python2024 will be available
with example codes covered in the lecture.  This repo also contains
the **install_anaconda3** script, to simplify installation on various unix
flavors. You can also head over to https://www.anaconda.com/ and do it
yourself.

There is even a lightweight **install_miniconda3** script, in case you
want a handcrafted version that installs in 15 seconds.

### Slides

A link to the slides is here, with the caveat of course I'm probably working
on them as you read this:


https://docs.google.com/presentation/d/1m7E1YHG9R1uwwJS7i7MHGwpsL3pILK6vvhLpTr1KUIg/edit?usp=sharing\


## IPython

* magic
* profiles
* ...

## Spyder

* plot
* fontsize
* ...
* Sync/Link a spyder python (py) file with a notebook (ipynb)

## Jupyter Lab and Notebook

*  **jupyter-lab** : the Lab
*  **jupyter notebook** : notebook browser
*  **anaconda-navigator** : the Anaconda Portal


## Running a remote jupyter notebook

If the resources on your laptop are not enough, but your remote X display is too slow too (or not working),
or even even VNC/x2go is not a solution, running a remote notebook may be the solution.

Here is a sample session:

       # login on the remote
       local% ssh user@remote

       # set up your python environment on the remote, YMMV
       remote% source anaconda3/python_start.sh

       # start up a notebook without local browser, but pick a free port number
       # watch the URL to be loaded later
       remote% jupyter notebook --no-browser --port=8086

       # set up port forwarding between laptop and remote, this will leave an open shell on remote
       local% ssh -L 8086:localhost:8086 user@remote
       local%

       # 
       local%  xdg-open http://localhost:8086/tree?token=blablablabla

## Fun Things?

* **The Vesuvius Challenge**  :  https://scrollprize.org/
  * https://scrollprize.org/data
  * https://colab.research.google.com/github/ScrollPrize/vesuvius/blob/main/notebooks/example1_data_access.ipynb
