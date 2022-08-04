import streamlit as st
import numpy as np
import pandas as pd

st.title("Udemy streamlit test")

st.write("DataFrame")

df = pd.DataFrame({
    "一列目":[1,2,3,4],
    "二列目":[10,20,30,40]
})

#st.writeまたはst.dataframeで表を表示できる。
#st.dataframeだとwidthとheightを引数として入れられる。

# st.write(df)

st.dataframe(df.style.highlight_max(axis=0))

#dataframe以外に表を作成するもう一個の方法→st.table。
#tableはstatic
st.table(df)

# グラフの書き方
df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)
st.line_chart(df2) #折れ線グラフの表示。
st.area_chart(df2) #領域図示
st.bar_chart(df2)

#APIリファレンスにいろいろあるので読んでみよ。

"""
# 章
## 説
### 項


```python
import streamlit as st
import numpy as np
import pandas as pd
```
このほか、Latexなども利用可能。referenceを読むべし。

"""

# 地図上へのマッピング
df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=["lat","lon"]
)
st.map(df3)

# 画像の表示
# Display mediaで画像の表示以外にもオーディオ、ビデオなど各メディアを表示させることができる。

from PIL import Image
#st.write("Display Image")
#img =Image.open("EIKEN_Pre-1_uchidatakumi.png")
#st.image(img,caption='証明書',use_column_width=True) #use_column_width=Trueでアプリの大きさに合わせてくれる。


st.title("インタラクティブなウィジェット")
#チェックボックスを用いた表示可否
if st.checkbox("Show Image"):
    img =Image.open("EIKEN_Pre-1_uchidatakumi.png")
    st.image(img,caption='証明書',use_column_width=True)


# セレクトボックスを用いた表示可否
#リスト型で指定する。
option = st.selectbox(
    "あなたの好きな数字は何ですか",
    options = list(range(1,11))
)

"あなたの選んだ数字は",option,"です。"

# テキスト入力
text = st.text_input("あなたは休日に何をしますか")
"あなたの趣味",text

#スライダー
#スライダーの第一引数と第二引数でrangeを指定、第三引数はデフォルトの値
condition = st.slider("あなたの調子は？",0,100,50)
"コンディション",condition

#他のウィジェットもAPIの中から探してしまおう

st.title("レイアウトを整える")

#sidebarを作成する。
# st.sidebarと続けるだけ。
option2 = st.sidebar.selectbox(
    "あなたの体重はいくつですか",
    options =list(range(10,150,10))
)
"私の体重は",option2,"です。"

text2 = st.sidebar.text_input(
    "あなたは自分は痩せていると思いますか"
)
"私は",text2,"だと思います。"
 

#2列（2columns)のレイアウトにする方法
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button :
    right_column.write("ここは右カラムです。")
left_column.write("これは左カラムですか")
right_column.write("右？")


# expander
expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ回答1")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ回答2")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ回答3")

# プログレスバーの表示
import time
st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty() #ここはまずは空
bar = st.progress(0) #int or float型で与える

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.02)

"Done!!!" 
#programは上から下に実行されるので
#for文が終わってから
