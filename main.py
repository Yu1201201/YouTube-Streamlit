import streamlit as st
import time

st.title('streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('ここは右カラム')


# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# condition = st.sidebar.slider('あなたの今の調子は?', 0, 100, 50)
# 'あなたの趣味：', text
# 'コンディション:', condition

# if st.checkbox('Show Image'):
#     img = Image.open('IMG_3557.jpeg')
#     st.image(img, caption = 'Yu Odashima', use_column_width = True)

