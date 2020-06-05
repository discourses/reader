## Reader: Python

Objective
A docker image that downloads data from the web into a docker volume.  


### Notes

Continuously updated ...

#### Running
An input argument example
* https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml

````bash
python src/main.py https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml
````

<br>

#### In Progress or Upcoming

* The switch from `dask` to `multiprocessing`
* Dockerfile
* GitHub Actions .yml: For (a) pytest, coverage, and pylint tests, (b) building & deploying docker images.  Continuing deploying images to docker hub
* Tests: GitHub Actions will highlight deficiencies w.r.t. tests and/or conventions
* Brief, but comprehensible, docstrings throughout


