import streamlit as st

menu=st.sidebar.selectbox('MENU',['로그인','회원가입'])

if menu=='로그인':
    
    db_id='test'
    db_pw='123'
    #st.title("로그인")
    # st.title("TEST")
    id=st.text_input('아이디',placeholder='아이디를 입력하세요')
    pw=st.text_input('비밀번호',type='password')
    login=st.button('로그인')

    if login:
        if db_id==id and db_pw==pw:
            st.success('로그인성공')
            st.balloons()
            
    else:
        st.error('로그인실패')
        st.snow()
elif menu=='회원가입':
    st.title=('회원가입')
    st.video('https://www.youtube.com/watch?v=siXXQID3MXQ&ab_channel=%EB%B9%B5%EB%8A%90' )

# check1=st.checkbox('선택')
# if check1:
#     st.write('선택하셨습니다.')
#     st.write(check) #선택이라는 문자가 체크에 들어감.
# sum=0
# check2=st.checkbox('짜장면(5000원)')
# check3=st.checkbox('짬뽕(7000원)')
# check4=st.checkbox('탕수육(15000원)')
# if check2:
#     sum=sum+5000
# if check3:
#     sum=sum+7000
# if check4:
#     sum=sum+15000
# st.subheader(f'선택한 가격은 {sum}')

# 과목 = st.selectbox("과목을 선택하세요",
#                     ["확률과 통계",
#                      "미분과 적분",
#                      "기하와 벡터"])
# st.subheader(f"당신이 선택한 과목은 {과목}입니다.")
# 과목=st.selectbox("과목선택", ['확률','미분','기하'])
# st.subheader(f'당신이선택한 과목은{과목}입니다.')

# 버튼=st.button('버튼')
# if 버튼:   #이벤트 실행 내용 중 타이틀 바꾸고 싶을때 타이틀이 위에 코드되어 있으면 수정할 수 없다. 밑에 있는 내용만 수정 가능 
#     st.write('버튼을 눌렀습니다.')

# st.title("Title🍔")  #윈도우 점 하면 아이콘
# st.header("Header")
# st.subheader('subheader')
# st.write('작은 글씨')
# st.markdown('**스트림잇**을 :red[배워]봅시다!!') #**굵게 :red[]
