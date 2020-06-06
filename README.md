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
<br>

### Notes

#### Running

````bash
python src/main.py 
    https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml
````

Wherein [parameter.yml](https://raw.githubusercontent.com/greyhypotheses/dictionaries/develop/readerpython/parameters.yml) is an input argument example.

parameter | type | Descriptions
---  | ---  | ---
`sourceURL` | str | The root URL from whence files will be downloaded
`metadataFileURL` | str | A CSV file that includes a field of file names that would be downloaded
`fileStringsField` | str | The name of the field of file names
`fileStringsIncludeExt` | bool | Do the file names, in the file names field, include file extensions?
`archived` | bool | Archived files?  If true, they will be dearchived.  Presently, only zip files can be dearchived.
`ext` | str | File extension, e.g., .zip.  This parameter is mandatory if `fileStringsIncludeExt` is false.

<br>

#### In Progress or Upcoming

* The switch from `dask` to `multiprocessing`
* Dockerfile
* GitHub Actions .yml: For (a) automated pytest, coverage, and pylint tests, (b) building & deploying docker images.
* Automated Tests: GitHub Actions will highlight deficiencies w.r.t. tests and/or conventions
* Brief, but comprehensible, docstrings throughout

<br>

#### Packages

Refer to [filter.txt](./docs/filter.txt) & [requirements](requirements.txt)

* `pip freeze -r docs/filter.txt > requirements.txt`
* `conda install -c anaconda pillow==7.1.2`
