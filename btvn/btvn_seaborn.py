import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

df = sns.load_dataset("penguins")
print(df)
sns.barplot(data=df, x="island", y="body_mass_g")
plt.show()
