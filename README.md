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

Also usefull: virtualenv venv 

- note: conda not so full on mac-arm

## make 

html: (re)generate the web site  

publish: generate sring production settings  

serve-global: serve (as root) to "0.0.0.0":8000  
```
    pelican ~/r/k6wlr-source/content -o ~/r/k6wlr.com -s ~/r/k6wlr-source/pelicanconf.py -l -b 0.0.0.0  
```

devserver-global: regenerate and serve on 0.0.0.0:8000  

rsync_upload: upload the web site via rsync+ssh  

## dup to github

1. update SITEURL
2. make publish
3. cd ../jvbenavi.github.io; git add/commit/push

