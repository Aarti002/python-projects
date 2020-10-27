from flask import Flask,redirect, url_for, render_template, request, flash

app=Flask(__name__,template_folder='template')

posts={
    0:{
        'post_id':0,
        'title':'Hello,there!!',
        'content':'Keep similing:)'
    }
}


@app.route('/')
def home():
    return render_template('home.jinja2',posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post=posts.get(post_id)
    if not post:
        return render_template('404.jinja2',message=f'The page {post_id}for which you are looking is not present, sorry!!!')
    return render_template('post1.jinja2',post=post)


@app.route('/post/create',methods=['GET','POST'])
def create():
    if request.method=='POST':
        title=request.form.get('title')
        content=request.form.get('text')
        post_len=len(posts)
        posts[post_len]={'post_id':post_len,'title': title, 'content': content}

        return redirect(url_for('post',post_id=post_len))
    return render_template('form.jinja2')



if __name__=='__main__':
    app.run(debug=True)