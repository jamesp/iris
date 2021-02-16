FROM continuumio/miniconda3

RUN conda env create --file=requirements/ci/py38.yml