  function getParam(name) {
    url = new URL(window.location.href);
    params = new URLSearchParams(url.search);
    return params.getAll(name)
  }
  function getQuestions(data){
    show_comments = ""
    
    for(let i = 0; i < data.questions.length; i++) {
      obj = data.questions[i]
      show_comments += obj.resolved ? "<div class='comment solvedQuestion'>":"<div class='comment unsolvedQuestion'>"
      show_comments += "<div class='row'>"
      show_comments += "<div>"
      show_comments += "  <h2>コメント数</h2>"
      show_comments += "  <h1>"+obj.answerNum+"</h1>"
      show_comments += "</div>"
      show_comments += "<div>"
      show_comments += "  <div class='row'>"
      show_comments += "    <div class='name' id="+obj.id+">"+obj.author+"</div>"
      show_comments += "    <div class='time' >"+obj.created_at+"</div>"
      show_comments += "  </div>"
      show_comments += "  <h3 class='message'>"+obj.message+"</h3>"
      show_comments += "  <a class='buttonDetail' href=create_answer?question="+obj.id+"></a> "
      show_comments += data.myquestions.includes(obj.id) ? "<a class='buttonSolved' href='create_question?solved="+obj.id+"&subject="+getParam('subject')+"'>解決済みにする</a> ":" "
      show_comments += obj.resolved ? "解決済み":""
      show_comments += "</div>"
      show_comments += "</div>"
      show_comments += "</div>"
    }
    if(data.questions.length == 0){
      show_comments += "<div class='comment'>質問が投稿されていません。</div>"
    }
    show_comments += "<div class='box'></div>"//余白用

    return (show_comments)
  }
  function initialize() {
    str = "";
    show_comments = ""
    path = 'getQuestion?'
    querySubject = getParam('subject')
    querySubject.forEach(element=>
      path += "subject="+element+"&"
    )
    queryUser = getParam('user')
    queryUser.forEach(element=>
      path += "user="+element+"&"
    )
    
    if(getParam('sort').length>0){
      if(getParam('sort')[0]=="comment"){
        path += 'sort=comment'
       
      }
    }
    fetch(path)
    .then(response => {

      // (1) 通信が成功したか確認する
      if (!response.ok) {

        // (2) 通信に失敗したときはエラーを発生させる
        throw new Error('Not ok');
      }
      // (3) レスポンスデータからJSONデータを取得
      return response.json();
    })
    .then(data => {
      // console.log(data.tasks);
      
      
      const list = document.getElementById('questions');
      list.innerHTML = getQuestions(data) ;
      // list.scrollTo(0, list.scrollHeight);
    })
    .catch(error => {
      console.error(error);
    });
  
  }
  function load_data() {
    str = "";
    show_comments = ""
    path = 'getQuestion?'
    querySubject = getParam('subject')
    querySubject.forEach(element=>
      path += "subject="+element+"&"
    )
    queryUser = getParam('user')
    queryUser.forEach(element=>
      path += "user="+element+"&"
    )
    if(getParam('sort')[0]){
      if(getParam('sort')[0]=="comment"){
        path += 'sort=comment'
       
      }

    }
   
    fetch(path)
    .then(response => {

      // (1) 通信が成功したか確認する
      if (!response.ok) {

        // (2) 通信に失敗したときはエラーを発生させる
        throw new Error('Not ok');
      }
      // (3) レスポンスデータからJSONデータを取得
      return response.json();
    })
    .then(data => {
      // console.log(data.tasks);
      
      

      const list = document.getElementById('questions');
      list.innerHTML =  getQuestions(data) ;
    })
    .catch(error => {
      console.error(error);
    });


    setTimeout(function() {load_data()},1000);//todo websocketで必要なときだけデータを受け取る仕様に変更したい
  }
  function save_question(){
    
    message = document.getElementById('message').value
    select = document.getElementById('select').value

    path = "create_question?subject="+getParam('subject')[0]+"&message="+message+"&select="+select
    console.log(path)
    fetch(path)
        .then(response => {

          // (1) 通信が成功したか確認する
          if (!response.ok) {

            // (2) 通信に失敗したときはエラーを発生させる
            throw new Error('Not ok');
          }
          // (3) レスポンスデータからJSONデータを取得
          return response.json();
        })
        .then(data => {
          initialize();
          
        })
        .catch(error => {
          console.error(error);
        });
  }
  
  function delete_all_comments(){
    
    
    path = "getLog?subject="+getParam('subject')+"&delete=all"
    alert(path)
    fetch(path)
        .then(response => {

          // (1) 通信が成功したか確認する
          if (!response.ok) {

            // (2) 通信に失敗したときはエラーを発生させる
            throw new Error('Not ok');
          }
          // (3) レスポンスデータからJSONデータを取得
          return response.json();
        })
        .then(data => {
          console.log(data);
          
        })
        .catch(error => {
          console.error(error);
        });
  }
  document.addEventListener
  ('DOMContentLoaded', function () { 
        initialize();
        setTimeout(function() {load_data()},1000);//todo websocketで必要なときだけデータを受け取る仕様に変更したい
  })