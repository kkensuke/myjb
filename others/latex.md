# How to use latex in VScode

## Install TexLive

Download `install-tl-unx.tar.gz`
```zsh
$ curl -OL http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
```

Open `install-tl-unx.tar.gz`
```zsh
$ tar xvf install-tl-unx.tar.gz
```



```zsh
$ cd install-tl-2*
```


```zsh
$ sudo ./install-tl -no-gui -repository http://mirror.ctan.org/systems/texlive/tlnet/
```



```zsh
Actions:
 <I> start installation to hard disk
 <H> help
 <Q> quit
Enter command: I
```

```zsh
$ sudo /usr/local/texlive/????/bin/*/tlmgr path add
```

<!--
install-tl-unx.tar.gz をダウンロードします．
$ curl -OL http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz

install-tl-unx.tar.gz を展開します．
$ tar xvf install-tl-unx.tar.gz

展開したインストーラのディレクトリに移動します．
$ cd install-tl-2*

root 権限でインストーラを実行します． デフォルトでは Tcl/Tk による GUI インストーラが起動します．-no-gui オプションでテキストモードで起動します．-repository オプションでダウンロードするリポジトリを指定できます．
$ sudo ./install-tl -no-gui -repository http://mirror.ctan.org/systems/texlive/tlnet/
...
Actions:
 <I> start installation to hard disk
 <H> help
 <Q> quit
Enter command: I
I を入力してインストールを開始します． サーバーの接続エラーが発生したり，何らかの理由により取得したアーカイブに問題があったりした場合はインストールが途中でストップします． この場合は，以下のコマンドで途中から再開できたりできなかったりします．

$ sudo ./install-tl -no-gui -profile installation.profile
再開できない場合は接続先を変更するか，または ISO ファイルをミラーサイトからダウンロードしてインストールしてください．

インストールが終了したら /usr/local/bin ディレクトリ配下にシンボリックリンクを追加します．
$ sudo /usr/local/texlive/????/bin/*/tlmgr path add

上記の ???? は 2021，* は universal-darwin にマッチすることが想定されていますがうまく動作しない場合は以下のようにして具体的なディレクトリ名を指定してください．
$ sudo /usr/local/texlive/2021/bin/universal-darwin/tlmgr path add

-->
## Setting for Japanese








