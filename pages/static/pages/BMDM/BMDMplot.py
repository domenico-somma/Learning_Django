import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def processing(df,name,word_sep="_"): #part of single_lineplot
    name=name.title()
    if isinstance(name, str):
        name=[name]
    try:
        sample=df.loc[name]
    except KeyError:
        return None
    s_or_i=sample.index.name
    sample=sample.reset_index()
#    print(sample)

    #########I don't know why sometimes is "index" others "symbol"###############
    sample2=pd.melt(sample, id_vars=[s_or_i], value_vars=sample.columns[1:])
    sample2["variable"]=[word[:-2] for word in sample2["variable"].tolist()] # serve per fare la St DEv!!!
#    print(sample2)
    cell=[]
    time=[]
    for a,b in [word.split(word_sep) for word in sample2["variable"].tolist()]:
        cell.append(a)
        time.append(b)
    sample2["Cell"]=cell
    sample2["Time"]=time
#    print(sample2)
    return sample2

def lineplot(df,name,word_sep="_"):
    name=name.title()
    sns.set("talk")
    sample2=processing(df,name,word_sep)

    if sample2 is None:
        return "Not found"
    f, ax = plt.subplots(figsize=(20, 6))

    ax = sns.pointplot(x=sample2["Time"], y=sample2["value"], data=sample2, hue=sample2["Cell"], ax=ax, stimator=np.median)
    ax = plt.suptitle(name,y=0.999)
    return ax
