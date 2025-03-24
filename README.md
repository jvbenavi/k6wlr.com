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

## make 

serve-global  
```
    pelican ~/r/k6wlr-source/content -o ~/r/k6wlr.com -s ~/r/k6wlr-source/pelicanconf.py -l -b 0.0.0.0  
```

devserver-global  

publish  

rsync_upload  

## dup to github

1. update SITEURL
2. make publish
3. cd ../jvbenavi.github.io; git add/commit/push

