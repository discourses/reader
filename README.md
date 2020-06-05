## Reader: Python

<dl>
    <dt>Objective</dt>
    <dd>A docker image that downloads data from the web into a volume. </dd>
</dl>

<dl>
    <dt>State</dt>
    <dd>In progress</dd>
</dl>

<br>
<br>

### Notes

#### Running
An input argument example
* https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml

````bash
python src/main.py 
    https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml
````

<br>

#### In Progress or Upcoming

* The switch from `dask` to `multiprocessing`
* Dockerfile
* GitHub Actions .yml: For (a) automated pytest, coverage, and pylint tests, (b) building & deploying docker images.  Continuing deploying images to docker hub
* Automated Tests: GitHub Actions will highlight deficiencies w.r.t. tests and/or conventions
* Brief, but comprehensible, docstrings throughout

<br>

#### Packages

Refer to [filter.txt](./docs/filter.txt) & [requiremnts](requirements.txt)

* `pip freeze -r docs/filter.txt > requirements.txt`
* `conda install -c anaconda pillow==7.1.2`
