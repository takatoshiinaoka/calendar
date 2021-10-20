aaaaabbbbb

# calender 環境設定の手順

## 1. はじめに
今回は2021年クラウドアプリ開発入門講座を受講し，独自のアプリ開発をすることになった．その報告会に向けた成果物として今回のカレンダープロジェクトを行っていく．
しかし，クラウドアプリ開発の期間では完成させることができなかったため，プロジェクト型演習でその続きを行っていく．
* 全員すること
    * [クラウドアプリ開発講座2021の開発環境をダウンロードする](Document/make_env.md)
    * githubアカウントを作る
    * gitのインストールする
* リポジトリ作る人がすること
    * [キャッシュファイル読み込み無効化](https://note.com/masato1230/n/na63ac4e7ccdd)
    * [キャッシュの削除](https://qiita.com/fuwamaki/items/3ed021163e50beab7154)


## 2. 自分のリポジトリにフォークする
右上の **Folk** から **自分のリポジトリにフォーク** してください．それをクローンしてください．


## 3. ローカルにリポジトリを保存する(cloneする)
エクスプローラーのリポジトリを入れたいフォルダで検索欄に「cmd」と入力する。今回はvscode/Workspaceのディレクトリをカレントディレクトリにする。コマンドプロンプトが開くので、以下のコードを入力する。
    

    git clone https://github.com/takatoshiinaoka/calendar.git
    
## 4.VScodeの開き方
1. vscode/VisualStudioCode.batファイルをクリック。すると、VSCodeが開く!
2. ファイル → Open Folder → vscode/Workspace/calendarを選択。
3. ターミナルを開き、「powershell」になっている人は、「cmd」に変更！
4. 「cmd」になっている事を確認したら、activate envのコマンドを打つ!      

        activate env

4. clone後**初めて**VSCodeを開く場合は、以下のコマンドを打つ!(2回目以降はしなくてよい)
   
        python manage.py migrate
5. 以下のコマンドを打ちサーバを立ち上げる!

        python manage.py runserver

    


## 5. pushするために必要な作業(VScodeのターミナルで実行する)
1.Githubのアカウント　(VSCodeのターミナル)  
例：git config --global user.name "takathosiinaoka"

    git config --global user.name "Githubアカウント名"  　 


2.メールアドレス(VSCodeのターミナル)  
例：git config --global user.email heavenhayao2316@gmail.com  

    git config --global user.email メールアドレス

## 6.編集履歴の表示(TortoiseGit or Gitlog)
エクスプローラーで緑のチェックが入ったフォルダを右クリックし、「TortoiseGit」の「ログを表示」より閲覧できる。  
また、VSCodeのターミナルで確認することもできる。以下のコードより確認できる。Enterキーを押すと過去のログが参照できる。「q」キーで終了する。


    git log
   
## 7.フォークしたリポジトリを最新化する
[フォークしたリポジトリを最新化する方法](https://qiita.com/Nossa/items/ace2ab802adc85f86b20)


1.GitHubのフォーク元のリポジトリをリモートブランチに追加する

    git remote add upstream https://github.com/takatoshiinaoka/calendar.git

2.フォーク元のmainブランチの変更差分を持ってくる

    git fetch upstream

3.mainブランチに移動し，フォーク元の差分をマージする

    git merge upstream/main

  

  
   

   
   
