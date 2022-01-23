## Reader: Python

<dl>
    <dt>Objective</dt>
    <dd>A docker image that downloads data from the web into a volume.</dd>
</dl>

<dl>
    <dt>State</dt>
    <dd>In progress</dd>
</dl>

<br>

develop <br>
![Reader Project](https://github.com/greyhypotheses/readerpython/workflows/Reader%20Project/badge.svg?branch=develop)

master <br>
![Reader Project](https://github.com/greyhypotheses/readerpython/workflows/Reader%20Project/badge.svg?branch=master)

<br>
<br>

### Running

```bash
python src/main.py
    https://raw.githubusercontent.com/greyhypotheses/discourses/develop/
      reader/resources/images.yml
```

or

```bash
python src/main.py
    https://raw.githubusercontent.com/greyhypotheses/discourses/develop/
      reader/resources/images.yml --limit 31
```

<br>

Wherein [images.yml](https://raw.githubusercontent.com/greyhypotheses/discourses/develop/reader/resources/images.yml) is an input argument of parameters that guides the downloading of data files, whilst the optional argument `--limit` is used to specify the number of files to download.

parameter | type | Descriptions
---  | ---  | ---
`rootURL` | str | The root URL from whence files will be downloaded
`metadataFileURL` | str | A CSV file that includes a field of file names that would be downloaded
`fileStringsField` | str | The name of the field of file names
`fileStringsIncludeExt` | bool | Do the file names, in the file names field, include file extensions?
`archived` | bool | Archived files?  If true, they will be dearchived.  Presently, only zip files can be dearchived.
`ext` | str | File extension, e.g., .zip.  This parameter is mandatory if `fileStringsIncludeExt` is false.

<br>
<br>

### In Progress or Upcoming

* The switch from `dask` to `multiprocessing`

* Dockerfile

* GitHub Actions .yml: For (a) automated pytest, coverage, and pylint tests, (b) building & deploying docker images.

* Automated Tests: GitHub Actions will highlight deficiencies w.r.t. tests and/or conventions

* Brief, but comprehensible, docstrings throughout

<br>
<br>

### Considerations

* At present, data is always downloaded into a volume named `data`.  This set-up might be changed such that data is downloaded into a volume whose name is declared in the parameters file.


<br>
<br>

### Environment

The local environment is

* `.../reader`: `conda create --prefix .../reader`

and the requirements are summarised via [filter.txt](./docs/filter.txt) & [requirements](requirements.txt)

* `pip freeze -r docs/filter.txt > requirements.txt`

Note:

* `python-graphviz` can't be included in filter.txt/requirements.txt; the reason why GitHub Actions rejects it is unclear.

* Always ascertain that the `dask` setting in requirements.txt is `dask[complete]`; this avoids GitHub Actions errors.

<br>
<br>

### Packages

The explicitly installed packages are listed in [filter.txt](./docs/filter.txt).  Foremost

```bash
  conda activate reader
    
  conda install -c anaconda dask==2021.10.0
  conda install -c anaconda python==3.7.10
  conda install -c anaconda pytest coverage pytest-cov pylint
```

<br>

A few points w.r.t. Dask

* Dask installed an old version of Pillow that triggers a GitHub security alert, hence<br>
```bash
  pip install Pillow==9.0.0
```

* Dask installed an old version of Jinja2 that triggers a GitHub security alert, hence<br>
```bash
  # 2.11.2 > 2.11.3
  conda install -c anaconda jinja2==2.11.3
```

<br>

Finally

```bash
  conda install -c anaconda requests 
  pip install dotmap==1.3.23
  
  # python-graphviz installs graphviz & python-graphiz
  conda install -c anaconda python-graphviz
```

<br>
<br>

### References

* [Renaming conda environments](https://www.scivision.dev/rename-conda-python-environment/): However, deleting then re-creatings seems to be the effective option

<br>
<br>
