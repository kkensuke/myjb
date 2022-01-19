# Linux/Unix

You can find many Linux cheat sheets using Google.
## Basic

Ctrl + C 処理の強制終了\
Ctrl + Z 処理の休止\
Ctrl + S 画面出力の停止\
Ctrl + Q 画面出力の再開\
Ctrl + L 画面クリア\
Ctrl + D ログアウト

Ctrl + A 行頭へ\
Ctrl + E 行末へ\
Ctrl + W 単語の先頭まで消す\
Ctrl + U 行頭まで消す\
Ctrl + K 行末まで消す\
Ctrl + Y 上で消去した内容の貼り付け

/	root dir\
\.	current dir\
\.\.	parent dir\
~	home dir

pwd:	show current directory\
ls:		directory listing

`mkdir`:		make directory
```zsh
mkdir ~/tmp
```

`cd`:		change directory
```zsh
cd ~/tmp
```

`touch`:		file を作る
```zsh
touch file
```

`ls`: dir内のファイルやディレクトリを表示する
```zsh
ls
# file
```

ここで階層を持った dir 構造をtmp内に作る
```zsh
mkdir -p dir/subdir/ssubdir
ls
# file dir
```

`rm`:		file を消去\
`rm -r`:	directory を消去
```zsh
rm file
rm -r dir
```

cf.
```zsh
rm -v file # show filename when removed
rm -i file # comfirm whether to rmove
rm -f file # force remove
```

`rmdir`:		remove empty directory
```zsh
mkdir dir
ls
# dir
rmdir dir
ls
# (nothing)
```

cf.
```zsh
rmdir -p dir/subdir/ssubdir
```


`echo`:
1. 環境変数などを表示する．
```zsh
echo $PATH
```
2. ファイルを作る．
- 新規 or 上書き
```zsh
echo [ファイルに書き出したい文字列] > [書き込みファイル名]
```
- 追記
```zsh
echo [ファイルに書き出したい文字列] >> [書き込みファイル名]
```

`cat`:	file の内容を表示
```zsh
touch file1
echo hello > file1
cat file1
# hello
```

```zsh
cat >> file2
asdf  (入力状態になるので何か入力する)
Ctrl + D(入力終了)
cat file2
# asdf
```

```zsh
cp file1 file3
cat file3
# hello
```

`cp`:		file or dir を copy
```zsh
mkdir dir1
touch dir1/file4
cp -r dir1 dir2
ls dir2
# file4
```

```{note}
`cp file1 file2`において，file2が既に存在するときは上書きするか聞かれる．
`cp -r dir1 dir2`において，dir2がまだ存在しない時，dir1の中身がdir2内にコピーされる．dir2が存在するときはdir1がdir2内にコピーされる．
```

`mv`:	file or dir を move\
もし file5 が存在しなければ，次の操作は rename
```zsh
mv file1 file5
mkdir dir3
mv file5 dir3
```
この時 file5 は dir3 に入る

もし dir4 が存在しなければ，次の操作は rename
```zsh
mv dir1 dir4
```
存在する場合，dir1がdir4内に移る．

`tree`: ファイル・ディレクトリをツリー状に表示する
zshではまずインストールする必要がある．
```zsh
brew install tree
```

```zsh
tree      pwd以下の全てを表示
test
├── dir2
│   └── file4
├── dir3
│   └── file5
├── dir4
│   └── file4
├── file2
└── file3
```

```zsh
tree -d   ディレクトリのみ表示
tree -L 2 2階層だけ表示
```

## 
`chomd`: 権限
```zsh
chmod モード file
```

モードは，所有者，グループ，他人に対して
それぞれ，rwx(読み取り，書き込み，実行)のどれを許可するか
3bitsで指定
全員に全て許可するなら 777\
所有者に全て(rwx)、グループ内の人とそれ以外の他人に読み取りだけ(r--)許可する場合、744

あるいは，
```
変更対象	意味
u	ユーザー
g	グループ
o	その他
a	すべて

変更方法	意味
=	指定した権限にする
+	指定した権限を付与する
-	指定した権限を除去する

変更内容	意味
r	読み取り
w	書き込み
x	実行
```
を用いて，
```zsh
$ chmod u+x file
```
のように変更もできる．

## Use symbolic links instead of alias
```zsh
ln -s original-dir/file where/to/put/SymboliLink
```


