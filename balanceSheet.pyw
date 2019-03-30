import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('bs.csv', 
                 names=('ass', 'ass_value', 'lia', 'lia_value'), encoding="SHIFT-JIS")

Current = ["現預金", "売掛金", "流動負債", "その他流動資産"]
Long = ["有形固定資産", "無形固定資産", "投資その他の資産", "固定負債"]

# -----------------------------------------------------
length = 0
for value in df.ass_value:
    length += int(value.replace(",", ""))
    
def graph(x, data, data_name, color1, color2):
    cum = 0
    for i in range(0, len(data))[::-1]:
        if data_name[i] in Current:
            color = color1
        elif data_name[i] in Long:
            color = color2
        else :
            color = "#ffff7f"
        y = int(data[i].replace(",", ""))
        
        ax.bar(x, y, width=1.0, bottom=cum, color="{}".format(color), edgecolor="black")
        if y > length / 20:
            ax.text(x, cum+0.4*y, "{0}({1})".format(data_name[i], data[i]), 
                    ha='center', va='bottom', fontdict={'family': 'IPAexGothic'})
        cum += y

fig, ax = plt.subplots(figsize=(5, 4))
fig.suptitle("Total Assess:{:,}".format(length))
ax.set_xlim(-1, 1)
ax.set_ylim(0, length)
ax.tick_params(labelbottom=False, labelleft=False, left=False, bottom=False)

graph(-0.5, df.ass_value, df.ass, "#b2d8ff", "#7fbfff")
graph(0.5, df.lia_value, df.lia, "#ffb2b2", "#ff7f7f")

plt.show()