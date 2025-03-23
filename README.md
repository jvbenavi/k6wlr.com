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

html  
    pelican ~/r/k6wlr.com/content -o ~/r/k6wlr.com/output -s ~/r/k6wlr.com/pelicanconf.py 

serve  
    #pelican ~/r/k6wlr.com/content -l ~/r/k6wlr.com/output -s ~/r/k6wlr.com/publishconf.py -b 0.0.0.0
    pelican --listen -b 0.0.0.0

publish  
    pelican ~/r/k6wlr.com/content -o ~/r/k6wlr.com/output -s ~/r/k6wlr.com/publishconf.py 

rsync  
    rsync -e "ssh -p 22" -P -rvzc --include tags --cvs-exclude --delete ~/r/k6wlr.com/output/ k6wlr.com:/var/www/k6wlr.com/public_html




