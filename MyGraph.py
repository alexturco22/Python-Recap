import matplotlib.pyplot as plt         #Step 1) Create a Virtual Environment (VE) in terminal
import numpy as np                              #for pc's use... py -3 -m venv (and then name of VE)

x = np.linspace(0, 20, 100)             #Step 3) Install 3rd party library/module bc there was an error "No module named matplotlib"
plt.plot(x, np.sin(x))                          #for pc's use... pip3 install (whatever library)
                                        #Step 2) Activate the VE
plt.show()                                      #for pc's use... myvenv/Scripts/activate

print("Hello World!")             #Won't work if you download with root interpreter vs the virtual environment.
