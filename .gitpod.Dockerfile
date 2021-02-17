FROM gitpod/workspace-full

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
RUN bash miniconda.sh -b -p ${HOME}/miniconda
RUN rm miniconda.sh

ENV PATH="${HOME}/miniconda/bin:${PATH}"

# WORKDIR /workspace/iris

# RUN conda env create --file=requirements/ci/py38.yml

# RUN conda config --set always_yes yes --set changeps1 no
# RUN conda config --set show_channel_urls True
# RUN conda config --add channels conda-forge
# RUN conda update --quiet --name base conda
# RUN conda install --quiet --name base nox pip
