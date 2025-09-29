# k6wlr.com

personal website

## setup 

```
  install conda 
  conda update conda
  conda create --name envpelican python=3
  conda activate envpelican
  conda install --name envpelican beautifulsoup4 
  pip install pelican markdown typogrify smartypants 
```

Also usefull: 

```
  conda deactivate
  conda info --envs
  conda list
  conda search *
  conda env export > environment.yml
  conda env create -f environment.yml
```

Also usefull: virtualenv 

```
  virtualenv ~/virtualenvs/pelican
  cd ~/virtualenvs/pelican
  source bin/activate
  python -m pip install "pelican[markdown]"
  python -m pip install "beautifulsoup4 typogrify pytz"
  pip freeze > requirements.txt
  pip install -r requirements.txt
```

- note: conda not so full on mac-arm

## make 

html: (re)generate the web site  

devserver-global: regenerate and serve on 0.0.0.0:8000  

publish: generate useing production settings  

rsync_upload: upload the web site via rsync+ssh  

## dup to github

1. update SITEURL
2. make publish
3. cd ../jvbenavi.github.io; git add/commit/push

