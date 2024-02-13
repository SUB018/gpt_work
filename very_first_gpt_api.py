import openai

openai.api_key='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'

def ask_to_gpt_35_turbo(user_input):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        top_p=0.5,
        temperature=0.5,   # 단어의 확률 값 > 모델이 다음 단어를 예측할 때 무작위 성 추가 
        messages=[
            # role 은 총 3가지로 되어있음. (system, user, assistant)
            # (1) user: 사용자의 말, assistant: gpt의 말, system: assistant에게 이 대화의 내용이 무엇이 될지 지시하는 역할 
            # {"role": "system", "content": "You are a helpful assistant."}, # content부분은 gpt의 역할이다! 
            # {"role": "system", "content": "You are the mirror of Snow white"},
            {"role": "system", "content": "You are the Joker of the Batman movie. You must pretend like Joker of the story. When you speak in Korean, you must use 반말."},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content

user_request='''
거울아! 거울아! 세상에서 누가 제일 예쁘니?  
'''

r=ask_to_gpt_35_turbo(user_request)

print(r) 