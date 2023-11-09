from flask import Flask, render_template
from flask import Flask, request, jsonify
import openai
# 设置 OpenAI API 密钥
openai.api_key = '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'
data_dict = {"如果使用者輸入內容跟興趣專長無關":"回覆：請輸入興趣或是專長","桌球":"1.桌球教練2.桌球販賣店3.國小老師4.5."}
data=str(data_dict)
def chatgpt(msg):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是可以利用專長興趣來幫使用者分析適合的職業"},
            {"role": "system", "content": data},
            {"role": "user", "content": "幫我回答30字以內我的專長和興趣適合什麼職業（列出來職業名稱即可1.2.3.4.5.）以下是我的專長興趣" + msg},
        ]
    )
    return completion['choices'][0]['message']['content']
app = Flask(__name__, static_folder='/Users/lipinze/Desktop/RachelWeb/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/service.html')
def service():
    return render_template('service.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/jobs.html')
def jobs():
    return render_template('jobs.html')

@app.route('/events.html')
def events():
    return render_template('events.html')

@app.route('/knowledge.html')
def knowledge():
    return render_template('knowledge.html')

@app.route('/talents.html')
def talents():
    return render_template('talents.html')


@app.route('/companies.html')
def companies():
    return render_template('companies.html')

@app.route('/training.html')
def training():
    return render_template('training.html')

@app.route('/company.html')
def company():
    return render_template('company.html')



@app.route('/api/chat', methods=['POST'])
def chat_with_backend():
    user_message = request.json.get('message')
    bot_response = chatgpt(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(port=1024)
