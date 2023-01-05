# the sole purpose of this file is to test things before implementing them in the main file
# it's not intended to stay in the final product
import pandas as pd
import os

def open_results(results_file):
    list = pd.read_html(results_file)
    df = pd.DataFrame(list[0])
        
open_results("results.html")