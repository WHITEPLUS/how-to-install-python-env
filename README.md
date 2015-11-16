# Pythonのはじめかた

Pythonをはじめるにあたって、最初に行うOS標準のPythonに依存しない環境構築の解説とサンプルコードになります。

この環境を利用することでプロジェクトや目的に応じて様々なバージョンのPython実行環境とライブラリを使い分けることができます。

手っ取り早く環境を構築したい人はdirenv、Pythonz、Virtualenvをインストールして
[このサンプルコードについて](#about_this)
を見てください。

## 前提の環境
* MacOSX
* Homebrewインストール済み

## システムにインストールするツール
* [direnv](https://github.com/direnv/direnv)

    プロジェクトのディレクトリに cd するだけで、自動的に環境を切り替えする

* [Pythonz](http://saghul.github.io/pythonz/)

    様々なバージョンのPythonをOS標準とは別にインストールする
* [Virtualenv](https://virtualenv.readthedocs.org/en/latest)

    システムとは別にプロジェクト用のPythonライブラリをインストールする

## direnvのインストールと初期設定
インストール

    $ brew install direnv

初期設定、bashの場合は~/.bashrcに下記を追記

    # ~/.bashrc
    
    eval "$(direnv hook bash)"
    # zshrcの場合の追記内容
    # eval "$(direnv hook zsh)"

## <a name="lets_setup_python"> PythonzとVirtualenvのインストールと初期設定

    $ curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python # システムにpipが入ってなければ
    $ pip install virtualenv
    $ pip install virtualenvwrapper
    $ curl -kL https://raw.github.com/saghul/pythonz/master/pythonz-install | bash

下記をbashrcかzshrcに追記する

    # ~/.bashrc
    
    [[ -s $HOME/.pythonz/etc/bashrc ]] && source $HOME/.pythonz/etc/bashrc

## <a name="lets_make_env"> 環境を作ってみる

bashrc(もしくはzshrcとか)設定後、設定のリロードをしてない場合は読み込んでおく

    $ source ~/.bashrc

お好みのバージョンのPythonをPythonzでインストールしておく

    $ pythonz install 2.7.9

これで`~/.pythonz/pythons/CPython-2.7.9/`に指定したバージョンのPythonがインストールされる

次にプロジェクト用のディレクトリを作成して新たにインストールしたPythonの環境として初期化する

    $ mkdir -p ~/your/project/root
    $ virtualenv -p ~/.pythonz/pythons/CPython-2.7.9/bin/python ~/your/project/root
    $ # direnvを設定
    $ cat << EOT > ~/your/project/root/.envrc
    PATH_add bin
    sh bin/activate
    EOT

これでcdするとプロジェクト設定が読み込まれてカスタマイズされた環境でPythonを実行できます。

    $ cd ~/your/project/root
    direnv: loading .envrc
    direnv: export ~PATH

`.envrc is blocked.`ってエラーが出る場合は`direnv allow .`する

    $ cd ~/your/project/root
    direnv: error .envrc is blocked. Run `direnv allow` to approve its content.
    $ direnv allow .
    direnv: loading .envrc
    direnv: export ~PATH

## .gitignoreの設定

ローカルのパスへのリンクとかがあるためVirtualenvがつくったファイルとかはgitにコミットしない方が良さそうなので.gitignoreで除外しておくケースが多いかもしれない。

    # .gitignore
    /bin
    /include
    /lib
    .envrc

## IntellijIDEAの設定
つくったディレクトリを適当にエディタでオープンすれば設定されると思います、多分。。

## <a name="about_this"> このサンプルコードについて

direnvがインストール済みであれば、cdするだけで[PythonzとVirtualenvのインストールと初期設定](#lets_setup_python)と
[環境を作ってみる](#lets_make_env)の内容を自動で行うので手っ取り早くpythonの環境が手に入ります。

start.shでウェブサーバーのサンプルを実行します。

    git clone https://github.com/WHITEPLUS/how-to-start-python.git
    cd python-env-sample
    ./start.sh # サーバーを起動してブラウザを開きます


