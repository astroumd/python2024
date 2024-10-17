# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# #  Plotting in python
#
# We can do math $c^2 = a^2 + b^2$ inline as well as more complex
# $$
#    c^2 = a^2 + b^2
# $$
# or even
# $$
#    \ddot{ {\bf r}}_i \, = \, -G \sum_{j=1;\, j \not = \,i}^N {m_j \,({\bf r}_i - {\bf r}_j)  \over {(r_{ij}^2 + \epsilon^2)^{3/2} } }
# $$
#
#
# ## Scripting vs. Notebooks
#
# Magic ipython

# %%
#  autoreload for development
# %load_ext autoreload
# %autoreload 2

# widget (needs:    pip inatall ipympl
# %matplotlib widget   

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
#                          bogus colorful help
_help = """
this is some text
explaining in many lines
what are we doing here
"""

# %%
# %%time

n=100
x = np.random.normal(0.0,1.0,n)

y = x*x
plt.figure()
plt.plot(x,y,'+')
;


# %% [markdown]
# and lets *make* another **figure**

# %%
plt.figure()
plt.plot(x,y+1)
;

# %% [markdown]
# flip

# %%

y = -y


# %%
z2 = x + 2*y

# %%
